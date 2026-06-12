"""
Datenbankmodul für die Inbetriebnahme-Wissensdatenbank.
Verwaltet die SQLite-Datenbankverbindung und CRUD-Operationen.
"""

import os
from datetime import date, datetime
from sqlalchemy import create_engine, or_, func
from sqlalchemy.orm import sessionmaker, Session
from models import Base, Fehlerfall
import pandas as pd

# Datenbankpfad relativ zum Skript
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "commissioning.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

# Engine und Session erstellen
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)


def init_db():
    """Erstellt alle Tabellen in der Datenbank."""
    Base.metadata.create_all(engine)


def get_session() -> Session:
    """Gibt eine neue Datenbank-Session zurück."""
    return SessionLocal()


def create_fehlerfall(data: dict) -> Fehlerfall:
    """
    Erstellt einen neuen Fehlerfall in der Datenbank.

    Args:
        data: Dictionary mit allen Felddaten

    Returns:
        Der erstellte Fehlerfall
    """
    session = get_session()
    try:
        fehlerfall = Fehlerfall(**data)
        session.add(fehlerfall)
        session.commit()
        session.refresh(fehlerfall)
        return fehlerfall
    finally:
        session.close()


def update_fehlerfall(fehlerfall_id: int, data: dict) -> Fehlerfall:
    """
    Aktualisiert einen bestehenden Fehlerfall.

    Args:
        fehlerfall_id: ID des zu aktualisierenden Falls
        data: Dictionary mit aktualisierten Felddaten

    Returns:
        Der aktualisierte Fehlerfall
    """
    session = get_session()
    try:
        fehlerfall = session.query(Fehlerfall).filter(Fehlerfall.id == fehlerfall_id).first()
        if fehlerfall:
            for key, value in data.items():
                setattr(fehlerfall, key, value)
            fehlerfall.aktualisiert_am = datetime.now()
            session.commit()
            session.refresh(fehlerfall)
        return fehlerfall
    finally:
        session.close()


def delete_fehlerfall(fehlerfall_id: int) -> bool:
    """
    Löscht einen Fehlerfall aus der Datenbank.

    Args:
        fehlerfall_id: ID des zu löschenden Falls

    Returns:
        True bei Erfolg, False wenn nicht gefunden
    """
    session = get_session()
    try:
        fehlerfall = session.query(Fehlerfall).filter(Fehlerfall.id == fehlerfall_id).first()
        if fehlerfall:
            session.delete(fehlerfall)
            session.commit()
            return True
        return False
    finally:
        session.close()


def get_fehlerfall(fehlerfall_id: int) -> Fehlerfall:
    """Gibt einen einzelnen Fehlerfall anhand seiner ID zurück."""
    session = get_session()
    try:
        return session.query(Fehlerfall).filter(Fehlerfall.id == fehlerfall_id).first()
    finally:
        session.close()


def get_all_fehlerfaelle() -> list:
    """Gibt alle Fehlerfälle zurück."""
    session = get_session()
    try:
        return session.query(Fehlerfall).order_by(Fehlerfall.datum.desc()).all()
    finally:
        session.close()


def get_latest_fehlerfaelle(limit: int = 20) -> list:
    """Gibt die letzten N Fehlerfälle zurück."""
    session = get_session()
    try:
        return session.query(Fehlerfall).order_by(Fehlerfall.datum.desc()).limit(limit).all()
    finally:
        session.close()


def count_by_status() -> dict:
    """Zählt Fehlerfälle gruppiert nach Status."""
    session = get_session()
    try:
        results = session.query(
            Fehlerfall.status, func.count(Fehlerfall.id)
        ).group_by(Fehlerfall.status).all()
        return {status: count for status, count in results}
    finally:
        session.close()


def top_steuergeraete(limit: int = 10) -> list:
    """Gibt die häufigsten Steuergeräte zurück."""
    session = get_session()
    try:
        results = session.query(
            Fehlerfall.steuergeraet, func.count(Fehlerfall.id).label("anzahl")
        ).group_by(Fehlerfall.steuergeraet).order_by(
            func.count(Fehlerfall.id).desc()
        ).limit(limit).all()
        return results
    finally:
        session.close()


def top_ursachen(limit: int = 10) -> list:
    """Gibt die häufigsten Root-Cause-Kategorien zurück."""
    session = get_session()
    try:
        results = session.query(
            Fehlerfall.root_cause_kategorie, func.count(Fehlerfall.id).label("anzahl")
        ).filter(Fehlerfall.root_cause_kategorie != "").group_by(
            Fehlerfall.root_cause_kategorie
        ).order_by(func.count(Fehlerfall.id).desc()).limit(limit).all()
        return results
    finally:
        session.close()


def suche(suchbegriff: str) -> list:
    """
    Globale Volltextsuche über alle relevanten Felder.

    Args:
        suchbegriff: Der Suchbegriff

    Returns:
        Liste der gefundenen Fehlerfälle
    """
    session = get_session()
    try:
        pattern = f"%{suchbegriff}%"
        results = session.query(Fehlerfall).filter(
            or_(
                Fehlerfall.fahrzeugnummer.ilike(pattern),
                Fehlerfall.vin.ilike(pattern),
                Fehlerfall.steuergeraet.ilike(pattern),
                Fehlerfall.softwarestand_steuergeraet.ilike(pattern),
                Fehlerfall.softwarestand_fahrzeug.ilike(pattern),
                Fehlerfall.fehlerbeschreibung.ilike(pattern),
                Fehlerfall.ursache.ilike(pattern),
                Fehlerfall.loesung.ilike(pattern),
                Fehlerfall.tags.ilike(pattern),
                Fehlerfall.projekt.ilike(pattern),
                Fehlerfall.baureihe.ilike(pattern),
                Fehlerfall.fehlersymptome.ilike(pattern),
            )
        ).order_by(Fehlerfall.datum.desc()).all()
        return results
    finally:
        session.close()


def filter_fehlerfaelle(
    zeitraum_von: date = None,
    zeitraum_bis: date = None,
    projekt: str = None,
    baureihe: str = None,
    steuergeraet: str = None,
    kommunikationsart: str = None,
    status: str = None,
    verantwortlicher: str = None,
    root_cause: str = None,
) -> list:
    """
    Filtert Fehlerfälle nach verschiedenen Kriterien.

    Args:
        Alle Parameter sind optional und werden als AND-Bedingungen verknüpft.

    Returns:
        Liste der gefilterten Fehlerfälle
    """
    session = get_session()
    try:
        query = session.query(Fehlerfall)

        if zeitraum_von:
            query = query.filter(Fehlerfall.datum >= zeitraum_von)
        if zeitraum_bis:
            query = query.filter(Fehlerfall.datum <= zeitraum_bis)
        if projekt and projekt != "Alle":
            query = query.filter(Fehlerfall.projekt == projekt)
        if baureihe and baureihe != "Alle":
            query = query.filter(Fehlerfall.baureihe == baureihe)
        if steuergeraet and steuergeraet != "Alle":
            query = query.filter(Fehlerfall.steuergeraet == steuergeraet)
        if kommunikationsart and kommunikationsart != "Alle":
            query = query.filter(Fehlerfall.kommunikationsart == kommunikationsart)
        if status and status != "Alle":
            query = query.filter(Fehlerfall.status == status)
        if verantwortlicher and verantwortlicher != "Alle":
            query = query.filter(Fehlerfall.verantwortlicher == verantwortlicher)
        if root_cause and root_cause != "Alle":
            query = query.filter(Fehlerfall.root_cause_kategorie == root_cause)

        return query.order_by(Fehlerfall.datum.desc()).all()
    finally:
        session.close()


def finde_aehnliche_faelle(steuergeraet: str, kommunikationsart: str,
                           fehlerbeschreibung: str, tags: str, limit: int = 5) -> list:
    """
    Findet ähnliche Fehlerfälle basierend auf Steuergerät, Kommunikationsart,
    Tags und Fehlerbeschreibung.

    Args:
        steuergeraet: Name des Steuergeräts
        kommunikationsart: Art der Kommunikation
        fehlerbeschreibung: Beschreibung des Fehlers
        tags: Tags für den Fall
        limit: Maximale Anzahl der Ergebnisse

    Returns:
        Liste ähnlicher Fehlerfälle
    """
    session = get_session()
    try:
        conditions = []

        if steuergeraet:
            conditions.append(Fehlerfall.steuergeraet.ilike(f"%{steuergeraet}%"))
        if kommunikationsart:
            conditions.append(Fehlerfall.kommunikationsart == kommunikationsart)
        if tags:
            for tag in tags.split(","):
                tag = tag.strip()
                if tag:
                    conditions.append(Fehlerfall.tags.ilike(f"%{tag}%"))
        if fehlerbeschreibung:
            # Suche nach Schlüsselwörtern aus der Fehlerbeschreibung
            words = fehlerbeschreibung.split()
            for word in words[:5]:  # Maximal 5 Wörter verwenden
                if len(word) > 3:
                    conditions.append(Fehlerfall.fehlerbeschreibung.ilike(f"%{word}%"))

        if not conditions:
            return []

        results = session.query(Fehlerfall).filter(
            or_(*conditions)
        ).order_by(Fehlerfall.datum.desc()).limit(limit).all()
        return results
    finally:
        session.close()


def get_dataframe() -> pd.DataFrame:
    """Gibt alle Fehlerfälle als Pandas DataFrame zurück."""
    session = get_session()
    try:
        fehlerfaelle = session.query(Fehlerfall).all()
        if not fehlerfaelle:
            return pd.DataFrame()

        data = []
        for f in fehlerfaelle:
            data.append({
                "ID": f.id,
                "Datum": f.datum,
                "Projekt": f.projekt,
                "Baureihe": f.baureihe,
                "Fahrzeugnummer": f.fahrzeugnummer,
                "VIN": f.vin,
                "SW Fahrzeug": f.softwarestand_fahrzeug,
                "Verantwortlicher": f.verantwortlicher,
                "Steuergerät": f.steuergeraet,
                "Teilenummer": f.teilenummer,
                "SW Steuergerät": f.softwarestand_steuergeraet,
                "Kommunikation": f.kommunikationsart,
                "Fehlerbeschreibung": f.fehlerbeschreibung,
                "Symptome": f.fehlersymptome,
                "Tools": f.verwendete_tools,
                "Ursache": f.ursache,
                "Root Cause": f.root_cause_kategorie,
                "Lösung": f.loesung,
                "Lessons Learned": f.lessons_learned,
                "Status": f.status,
                "Tags": f.tags,
            })
        return pd.DataFrame(data)
    finally:
        session.close()


def insert_example_data():
    """Fügt einen Beispieldatensatz ein, wenn die Datenbank leer ist."""
    session = get_session()
    try:
        count = session.query(Fehlerfall).count()
        if count == 0:
            example = Fehlerfall(
                datum=date(2026, 6, 12),
                projekt="eBus",
                baureihe="",
                fahrzeugnummer="Fahrzeug_001",
                vin="",
                softwarestand_fahrzeug="",
                verantwortlicher="",
                steuergeraet="BGW",
                teilenummer="",
                softwarestand_steuergeraet="",
                kommunikationsart="Ethernet",
                fehlerbeschreibung="BGW kann nicht stabil mit ICC kommunizieren.",
                fehlersymptome="Ethernet Link instabil\nPing nicht erfolgreich\nDiagnose nicht erreichbar",
                logs="",
                diagnosecodes="",
                dateien="",
                verwendete_tools="Wireshark,CANoe,Xentry",
                durchgefuehrte_schritte="IP-Konfiguration geprüft\nEthernet Link geprüft\nSoftwarestände verglichen\nRouting analysiert\nLogs ausgewertet",
                messergebnisse="",
                beobachtungen="",
                kommunikationsanalyse="",
                ursache="Softwarestand BGW nicht kompatibel mit ICC.",
                root_cause_kategorie="Software",
                loesung="BGW auf freigegebenen Softwarestand geflasht.",
                lessons_learned="Vor jedem Fahrzeug-Flash Kompatibilitätsmatrix prüfen.",
                status="Gelöst",
                tags="Ethernet,BGW,ICC,Kommunikation",
            )
            session.add(example)
            session.commit()
    finally:
        session.close()
