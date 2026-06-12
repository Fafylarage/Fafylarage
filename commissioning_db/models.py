"""
Datenmodelle für die Inbetriebnahme-Wissensdatenbank.
Definiert die SQLAlchemy ORM-Modelle für alle Fehlerfälle.
"""

from sqlalchemy import Column, Integer, String, Text, Date, DateTime, create_engine
from sqlalchemy.orm import declarative_base
from datetime import datetime, date

Base = declarative_base()


class Fehlerfall(Base):
    """
    Hauptmodell für einen Inbetriebnahme-Fehlerfall.
    Enthält alle Informationen von der Fehlerbeschreibung bis zur Lösung.
    """
    __tablename__ = "fehlerfaelle"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # Allgemeine Informationen
    datum = Column(Date, default=date.today, nullable=False)
    projekt = Column(String(200), nullable=False)
    baureihe = Column(String(200), default="")
    fahrzeugnummer = Column(String(200), default="")
    vin = Column(String(17), default="")
    softwarestand_fahrzeug = Column(String(200), default="")
    verantwortlicher = Column(String(200), default="")

    # Technische Informationen
    steuergeraet = Column(String(200), nullable=False)
    teilenummer = Column(String(200), default="")
    softwarestand_steuergeraet = Column(String(200), default="")
    kommunikationsart = Column(String(100), default="")

    # Fehlerbeschreibung
    fehlerbeschreibung = Column(Text, default="")
    fehlersymptome = Column(Text, default="")
    logs = Column(Text, default="")
    diagnosecodes = Column(Text, default="")
    dateien = Column(Text, default="")  # Komma-separierte Dateipfade

    # Analyseweg
    verwendete_tools = Column(Text, default="")  # Komma-separierte Tools
    durchgefuehrte_schritte = Column(Text, default="")
    messergebnisse = Column(Text, default="")
    beobachtungen = Column(Text, default="")
    kommunikationsanalyse = Column(Text, default="")

    # Ursache und Lösung
    ursache = Column(Text, default="")
    root_cause_kategorie = Column(String(100), default="unbekannt")
    loesung = Column(Text, default="")
    lessons_learned = Column(Text, default="")

    # Status
    status = Column(String(50), default="Offen")

    # Tags für die Suche
    tags = Column(Text, default="")

    # Metadaten
    erstellt_am = Column(DateTime, default=datetime.now)
    aktualisiert_am = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"<Fehlerfall(id={self.id}, projekt='{self.projekt}', steuergeraet='{self.steuergeraet}', status='{self.status}')>"
