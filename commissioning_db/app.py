"""
Inbetriebnahme-Wissensdatenbank - Streamlit Webanwendung
=========================================================
Hauptanwendung zur Dokumentation, Analyse und Wiederverwendung
von Inbetriebnahme-Erkenntnissen im Automotive-Umfeld.

Start: streamlit run app.py
"""

import streamlit as st
import pandas as pd
from datetime import date, datetime
import os
import sys
import io

# Pfad für lokale Imports setzen
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import (
    init_db, create_fehlerfall, update_fehlerfall, delete_fehlerfall,
    get_fehlerfall, get_all_fehlerfaelle, get_latest_fehlerfaelle,
    count_by_status, top_steuergeraete, top_ursachen, suche,
    filter_fehlerfaelle, finde_aehnliche_faelle, get_dataframe,
    insert_example_data
)

# ============================================================
# Konfiguration
# ============================================================

st.set_page_config(
    page_title="Inbetriebnahme-Wissensdatenbank",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Dunkles Theme und benutzerdefiniertes CSS
st.markdown("""
<style>
    /* Globales Styling */
    .main .block-container {
        padding-top: 1rem;
        max-width: 1400px;
    }

    /* Status-Farben */
    .status-offen { color: #ff4b4b; font-weight: bold; }
    .status-analyse { color: #ffa500; font-weight: bold; }
    .status-geloest { color: #00cc66; font-weight: bold; }
    .status-nicht-reproduzierbar { color: #888888; font-weight: bold; }

    /* Metrikkarten */
    .metric-card {
        background: linear-gradient(135deg, #1e1e2e 0%, #2d2d44 100%);
        border: 1px solid #3d3d5c;
        border-radius: 10px;
        padding: 1.2rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-card h3 {
        color: #a0a0c0;
        font-size: 0.85rem;
        margin-bottom: 0.3rem;
    }
    .metric-card .value {
        font-size: 2rem;
        font-weight: bold;
        color: #ffffff;
    }

    /* Tabellen-Styling */
    .dataframe { font-size: 0.85rem; }

    /* Header */
    .app-header {
        background: linear-gradient(90deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 1rem 2rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        border: 1px solid #1f4068;
    }
    .app-header h1 {
        color: #e0e0ff;
        margin: 0;
        font-size: 1.8rem;
    }
    .app-header p {
        color: #8888aa;
        margin: 0.3rem 0 0 0;
        font-size: 0.9rem;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0e1117;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# Datenbank initialisieren
# ============================================================

init_db()
insert_example_data()

# ============================================================
# Konstanten
# ============================================================

KOMMUNIKATIONSARTEN = [
    "Ethernet", "CAN", "CAN-FD", "LIN", "FlexRay",
    "DoIP", "SOME/IP", "UDS", "Sonstiges"
]

TOOLS = [
    "CANoe", "CANalyzer", "Wireshark", "DTS Monaco", "ODIS",
    "DiagRA", "Vector VT System", "Xentry", "Python Script", "Sonstige"
]

ROOT_CAUSE_KATEGORIEN = [
    "Software", "Hardware", "Parametrierung", "Ethernet Konfiguration",
    "CAN Konfiguration", "Flashfehler", "Verkabelung",
    "Lieferantenfehler", "Bedienfehler", "unbekannt"
]

STATUS_OPTIONEN = ["Offen", "In Analyse", "Gelöst", "Nicht reproduzierbar"]

STATUS_FARBEN = {
    "Offen": "🔴",
    "In Analyse": "🟠",
    "Gelöst": "🟢",
    "Nicht reproduzierbar": "⚪",
}


# ============================================================
# Hilfsfunktionen
# ============================================================

def status_badge(status: str) -> str:
    """Gibt einen farbigen Status-Badge als HTML zurück."""
    farben = {
        "Offen": "#ff4b4b",
        "In Analyse": "#ffa500",
        "Gelöst": "#00cc66",
        "Nicht reproduzierbar": "#888888",
    }
    farbe = farben.get(status, "#888888")
    return f'<span style="background-color:{farbe};color:white;padding:2px 8px;border-radius:4px;font-size:0.8rem;">{status}</span>'


def fehlerfall_to_dict(f) -> dict:
    """Konvertiert ein Fehlerfall-Objekt in ein Dictionary."""
    return {
        "id": f.id,
        "datum": f.datum,
        "projekt": f.projekt,
        "baureihe": f.baureihe,
        "fahrzeugnummer": f.fahrzeugnummer,
        "vin": f.vin,
        "softwarestand_fahrzeug": f.softwarestand_fahrzeug,
        "verantwortlicher": f.verantwortlicher,
        "steuergeraet": f.steuergeraet,
        "teilenummer": f.teilenummer,
        "softwarestand_steuergeraet": f.softwarestand_steuergeraet,
        "kommunikationsart": f.kommunikationsart,
        "fehlerbeschreibung": f.fehlerbeschreibung,
        "fehlersymptome": f.fehlersymptome,
        "logs": f.logs,
        "diagnosecodes": f.diagnosecodes,
        "dateien": f.dateien,
        "verwendete_tools": f.verwendete_tools,
        "durchgefuehrte_schritte": f.durchgefuehrte_schritte,
        "messergebnisse": f.messergebnisse,
        "beobachtungen": f.beobachtungen,
        "kommunikationsanalyse": f.kommunikationsanalyse,
        "ursache": f.ursache,
        "root_cause_kategorie": f.root_cause_kategorie,
        "loesung": f.loesung,
        "lessons_learned": f.lessons_learned,
        "status": f.status,
        "tags": f.tags,
    }


# ============================================================
# Sidebar Navigation
# ============================================================

st.sidebar.markdown("## 🔧 Navigation")
seite = st.sidebar.radio(
    "Seite wählen:",
    [
        "📊 Dashboard",
        "➕ Neuer Fehlerfall",
        "🔍 Suche & Filter",
        "📋 Alle Fälle",
        "📤 Export",
    ],
    label_visibility="collapsed",
)

# ============================================================
# Header
# ============================================================

st.markdown("""
<div class="app-header">
    <h1>🔧 Inbetriebnahme-Wissensdatenbank</h1>
    <p>Automotive | E/E-Architektur | Gesamtfahrzeug | Steuergeräteintegration</p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# SEITE: Dashboard
# ============================================================

if seite == "📊 Dashboard":
    # Statistiken laden
    status_counts = count_by_status()
    offen = status_counts.get("Offen", 0)
    analyse = status_counts.get("In Analyse", 0)
    geloest = status_counts.get("Gelöst", 0)
    nicht_repro = status_counts.get("Nicht reproduzierbar", 0)

    # Metrikkarten
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🔴 Offene Fälle", offen)
    with col2:
        st.metric("🟠 In Analyse", analyse)
    with col3:
        st.metric("🟢 Gelöste Fälle", geloest)
    with col4:
        st.metric("⚪ Nicht reproduzierbar", nicht_repro)

    st.divider()

    # Top 10 Charts
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("🏆 Top 10 Steuergeräte")
        top_sg = top_steuergeraete()
        if top_sg:
            df_sg = pd.DataFrame(top_sg, columns=["Steuergerät", "Anzahl"])
            st.bar_chart(df_sg.set_index("Steuergerät"))
        else:
            st.info("Noch keine Daten vorhanden.")

    with col_right:
        st.subheader("🔍 Top 10 Fehlerursachen")
        top_rc = top_ursachen()
        if top_rc:
            df_rc = pd.DataFrame(top_rc, columns=["Kategorie", "Anzahl"])
            st.bar_chart(df_rc.set_index("Kategorie"))
        else:
            st.info("Noch keine Daten vorhanden.")

    st.divider()

    # Letzte 20 Einträge
    st.subheader("📋 Letzte 20 Einträge")
    letzte = get_latest_fehlerfaelle(20)
    if letzte:
        data = []
        for f in letzte:
            data.append({
                "ID": f.id,
                "Datum": f.datum,
                "Projekt": f.projekt,
                "Steuergerät": f.steuergeraet,
                "Kommunikation": f.kommunikationsart,
                "Status": f"{STATUS_FARBEN.get(f.status, '')} {f.status}",
                "Fehlerbeschreibung": f.fehlerbeschreibung[:80] + "..." if len(f.fehlerbeschreibung or "") > 80 else f.fehlerbeschreibung,
            })
        df_letzte = pd.DataFrame(data)
        st.dataframe(df_letzte, use_container_width=True, hide_index=True)

        # Detailansicht
        st.subheader("📄 Detailansicht")
        selected_id = st.selectbox(
            "Fall-ID auswählen:",
            options=[f.id for f in letzte],
            format_func=lambda x: f"ID {x} - {next((f.steuergeraet for f in letzte if f.id == x), '')}"
        )
        if selected_id and st.button("Details anzeigen", key="dashboard_details"):
            st.session_state["detail_id"] = selected_id
            st.session_state["show_detail"] = True

    else:
        st.info("Noch keine Einträge vorhanden. Legen Sie einen neuen Fehlerfall an.")

    # Detailansicht anzeigen
    if st.session_state.get("show_detail"):
        detail_id = st.session_state.get("detail_id")
        fall = get_fehlerfall(detail_id)
        if fall:
            st.divider()
            st.markdown(f"### 📄 Detailansicht - Fall #{fall.id}")

            # Fahrzeuginformationen
            with st.expander("🚗 Fahrzeuginformationen", expanded=True):
                c1, c2, c3 = st.columns(3)
                c1.write(f"**Datum:** {fall.datum}")
                c1.write(f"**Projekt:** {fall.projekt}")
                c1.write(f"**Baureihe:** {fall.baureihe}")
                c2.write(f"**Fahrzeugnummer:** {fall.fahrzeugnummer}")
                c2.write(f"**VIN:** {fall.vin}")
                c2.write(f"**SW Fahrzeug:** {fall.softwarestand_fahrzeug}")
                c3.write(f"**Verantwortlicher:** {fall.verantwortlicher}")
                c3.write(f"**Steuergerät:** {fall.steuergeraet}")
                c3.write(f"**Teilenummer:** {fall.teilenummer}")

            # Fehlerbeschreibung
            with st.expander("⚠️ Fehlerbeschreibung", expanded=True):
                st.write(f"**Kommunikation:** {fall.kommunikationsart}")
                st.write(f"**SW Steuergerät:** {fall.softwarestand_steuergeraet}")
                st.write("**Fehlerbeschreibung:**")
                st.write(fall.fehlerbeschreibung)
                st.write("**Symptome:**")
                st.write(fall.fehlersymptome)
                if fall.diagnosecodes:
                    st.write(f"**DTCs:** {fall.diagnosecodes}")
                if fall.logs:
                    st.write("**Logs:**")
                    st.code(fall.logs)

            # Analyse
            with st.expander("🔬 Analyse", expanded=True):
                st.write(f"**Tools:** {fall.verwendete_tools}")
                st.write("**Durchgeführte Schritte:**")
                st.write(fall.durchgefuehrte_schritte)
                if fall.messergebnisse:
                    st.write(f"**Messergebnisse:** {fall.messergebnisse}")
                if fall.beobachtungen:
                    st.write(f"**Beobachtungen:** {fall.beobachtungen}")
                if fall.kommunikationsanalyse:
                    st.write(f"**Kommunikationsanalyse:** {fall.kommunikationsanalyse}")

            # Ursache & Lösung
            with st.expander("✅ Ursache & Lösung", expanded=True):
                st.write(f"**Ursache:** {fall.ursache}")
                st.write(f"**Root Cause Kategorie:** {fall.root_cause_kategorie}")
                st.write(f"**Lösung:** {fall.loesung}")
                st.write(f"**Lessons Learned:** {fall.lessons_learned}")
                st.write(f"**Status:** {STATUS_FARBEN.get(fall.status, '')} {fall.status}")
                st.write(f"**Tags:** {fall.tags}")

        if st.button("Detailansicht schließen"):
            st.session_state["show_detail"] = False
            st.rerun()


# ============================================================
# SEITE: Neuer Fehlerfall
# ============================================================

elif seite == "➕ Neuer Fehlerfall":
    st.subheader("➕ Neuen Fehlerfall anlegen")

    with st.form("neuer_fehlerfall"):
        # Allgemeine Informationen
        st.markdown("#### 📋 Allgemeine Informationen")
        col1, col2, col3 = st.columns(3)
        with col1:
            datum = st.date_input("Datum", value=date.today())
            projekt = st.text_input("Projekt *", placeholder="z.B. eBus")
            baureihe = st.text_input("Baureihe", placeholder="z.B. W206")
        with col2:
            fahrzeugnummer = st.text_input("Fahrzeugnummer", placeholder="z.B. Fahrzeug_001")
            vin = st.text_input("VIN", placeholder="17-stellige VIN", max_chars=17)
            softwarestand_fahrzeug = st.text_input("Softwarestand Fahrzeug")
        with col3:
            verantwortlicher = st.text_input("Verantwortlicher Ingenieur")

        st.divider()

        # Technische Informationen
        st.markdown("#### 🔌 Technische Informationen")
        col1, col2, col3 = st.columns(3)
        with col1:
            steuergeraet = st.text_input("Steuergerät *", placeholder="z.B. BGW, ICC, ZGW")
            teilenummer = st.text_input("Teilenummer")
        with col2:
            softwarestand_sg = st.text_input("Softwarestand Steuergerät")
            kommunikationsart = st.selectbox("Kommunikationsart", KOMMUNIKATIONSARTEN)
        with col3:
            tags = st.text_input("Tags (kommasepariert)", placeholder="Ethernet,BGW,Kommunikation")

        st.divider()

        # Fehlerbeschreibung
        st.markdown("#### ⚠️ Fehlerbeschreibung")
        fehlerbeschreibung = st.text_area("Fehlerbeschreibung *", height=100,
                                          placeholder="Beschreiben Sie den Fehler...")
        fehlersymptome = st.text_area("Fehlersymptome", height=80,
                                      placeholder="Welche Symptome treten auf?")
        col1, col2 = st.columns(2)
        with col1:
            logs = st.text_area("Logs", height=80, placeholder="Relevante Log-Auszüge...")
        with col2:
            diagnosecodes = st.text_area("Diagnosecodes (DTCs)", height=80,
                                         placeholder="z.B. U0100, P0600...")

        st.divider()

        # Analyseweg
        st.markdown("#### 🔬 Analyseweg")
        verwendete_tools = st.multiselect("Verwendete Tools", TOOLS)
        durchgefuehrte_schritte = st.text_area("Durchgeführte Schritte", height=100,
                                               placeholder="Welche Analyseschritte wurden durchgeführt?")
        col1, col2 = st.columns(2)
        with col1:
            messergebnisse = st.text_area("Messergebnisse", height=80)
            beobachtungen = st.text_area("Beobachtungen", height=80)
        with col2:
            kommunikationsanalyse = st.text_area("Kommunikationsanalyse", height=80)

        st.divider()

        # Ursache und Lösung
        st.markdown("#### ✅ Ursache und Lösung")
        ursache = st.text_area("Ursache", height=80, placeholder="Was ist die Ursache des Fehlers?")
        root_cause_kategorie = st.selectbox("Root Cause Kategorie", ROOT_CAUSE_KATEGORIEN)
        loesung = st.text_area("Lösung", height=80, placeholder="Wie wurde der Fehler behoben?")
        lessons_learned = st.text_area("Lessons Learned", height=80,
                                       placeholder="Was kann man für die Zukunft lernen?")
        status = st.selectbox("Status", STATUS_OPTIONEN)

        st.divider()

        # Formular absenden
        submitted = st.form_submit_button("💾 Fehlerfall speichern", use_container_width=True)

        if submitted:
            if not projekt:
                st.error("❌ Bitte geben Sie ein Projekt an.")
            elif not steuergeraet:
                st.error("❌ Bitte geben Sie ein Steuergerät an.")
            elif not fehlerbeschreibung:
                st.error("❌ Bitte geben Sie eine Fehlerbeschreibung an.")
            else:
                data = {
                    "datum": datum,
                    "projekt": projekt,
                    "baureihe": baureihe,
                    "fahrzeugnummer": fahrzeugnummer,
                    "vin": vin,
                    "softwarestand_fahrzeug": softwarestand_fahrzeug,
                    "verantwortlicher": verantwortlicher,
                    "steuergeraet": steuergeraet,
                    "teilenummer": teilenummer,
                    "softwarestand_steuergeraet": softwarestand_sg,
                    "kommunikationsart": kommunikationsart,
                    "fehlerbeschreibung": fehlerbeschreibung,
                    "fehlersymptome": fehlersymptome,
                    "logs": logs,
                    "diagnosecodes": diagnosecodes,
                    "dateien": "",
                    "verwendete_tools": ",".join(verwendete_tools),
                    "durchgefuehrte_schritte": durchgefuehrte_schritte,
                    "messergebnisse": messergebnisse,
                    "beobachtungen": beobachtungen,
                    "kommunikationsanalyse": kommunikationsanalyse,
                    "ursache": ursache,
                    "root_cause_kategorie": root_cause_kategorie,
                    "loesung": loesung,
                    "lessons_learned": lessons_learned,
                    "status": status,
                    "tags": tags,
                }
                create_fehlerfall(data)
                st.success("✅ Fehlerfall erfolgreich gespeichert!")
                st.balloons()

    # Wissensdatenbank: Ähnliche Fälle anzeigen
    st.divider()
    st.markdown("#### 🧠 Wissensdatenbank - Ähnliche Fälle")
    st.caption("Geben Sie oben Steuergerät und Fehlerbeschreibung ein, um ähnliche Fälle zu finden.")

    # Ähnliche Fälle suchen basierend auf aktuellen Eingaben
    if st.button("🔍 Ähnliche Fälle suchen"):
        # Wir nutzen Session-State nicht in Formularen - stattdessen manuelle Suche
        st.info("Nutzen Sie die Suchfunktion im Menü 'Suche & Filter' für eine detaillierte Ähnlichkeitssuche.")


# ============================================================
# SEITE: Suche & Filter
# ============================================================

elif seite == "🔍 Suche & Filter":
    st.subheader("🔍 Suche & Filter")

    # Globale Suche
    st.markdown("#### 🔎 Globale Suche")
    suchbegriff = st.text_input(
        "Suchbegriff eingeben:",
        placeholder="Fahrzeugnummer, VIN, Steuergerät, Fehlertext, Ursache, Lösung, Tags..."
    )

    if suchbegriff:
        ergebnisse = suche(suchbegriff)
        st.info(f"**{len(ergebnisse)}** Ergebnis(se) gefunden für: *{suchbegriff}*")
        if ergebnisse:
            data = []
            for f in ergebnisse:
                data.append({
                    "ID": f.id,
                    "Datum": f.datum,
                    "Projekt": f.projekt,
                    "Steuergerät": f.steuergeraet,
                    "Kommunikation": f.kommunikationsart,
                    "Status": f"{STATUS_FARBEN.get(f.status, '')} {f.status}",
                    "Fehler": f.fehlerbeschreibung[:60] + "..." if len(f.fehlerbeschreibung or "") > 60 else f.fehlerbeschreibung,
                    "Ursache": f.ursache[:60] + "..." if len(f.ursache or "") > 60 else f.ursache,
                })
            st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)

    st.divider()

    # Erweiterte Filter
    st.markdown("#### 🎛️ Erweiterte Filter")

    # Daten für Dropdowns laden
    alle_faelle = get_all_fehlerfaelle()
    projekte = sorted(set(f.projekt for f in alle_faelle if f.projekt))
    baureihen = sorted(set(f.baureihe for f in alle_faelle if f.baureihe))
    steuergeraete = sorted(set(f.steuergeraet for f in alle_faelle if f.steuergeraet))
    verantwortliche = sorted(set(f.verantwortlicher for f in alle_faelle if f.verantwortlicher))

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        f_zeitraum_von = st.date_input("Von:", value=None, key="filter_von")
        f_projekt = st.selectbox("Projekt:", ["Alle"] + projekte)
    with col2:
        f_zeitraum_bis = st.date_input("Bis:", value=None, key="filter_bis")
        f_baureihe = st.selectbox("Baureihe:", ["Alle"] + baureihen)
    with col3:
        f_steuergeraet = st.selectbox("Steuergerät:", ["Alle"] + steuergeraete)
        f_kommunikation = st.selectbox("Kommunikationsart:", ["Alle"] + KOMMUNIKATIONSARTEN)
    with col4:
        f_status = st.selectbox("Status:", ["Alle"] + STATUS_OPTIONEN)
        f_verantwortlicher = st.selectbox("Verantwortlicher:", ["Alle"] + verantwortliche)

    f_root_cause = st.selectbox("Root Cause Kategorie:", ["Alle"] + ROOT_CAUSE_KATEGORIEN)

    if st.button("🔍 Filter anwenden", use_container_width=True):
        gefiltert = filter_fehlerfaelle(
            zeitraum_von=f_zeitraum_von,
            zeitraum_bis=f_zeitraum_bis,
            projekt=f_projekt,
            baureihe=f_baureihe,
            steuergeraet=f_steuergeraet,
            kommunikationsart=f_kommunikation,
            status=f_status,
            verantwortlicher=f_verantwortlicher,
            root_cause=f_root_cause,
        )
        st.info(f"**{len(gefiltert)}** Ergebnis(se) gefunden.")
        if gefiltert:
            data = []
            for f in gefiltert:
                data.append({
                    "ID": f.id,
                    "Datum": f.datum,
                    "Projekt": f.projekt,
                    "Steuergerät": f.steuergeraet,
                    "Kommunikation": f.kommunikationsart,
                    "Status": f"{STATUS_FARBEN.get(f.status, '')} {f.status}",
                    "Fehler": f.fehlerbeschreibung[:60] + "..." if len(f.fehlerbeschreibung or "") > 60 else f.fehlerbeschreibung,
                })
            st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)

    st.divider()

    # Ähnlichkeitssuche (Wissensdatenbank)
    st.markdown("#### 🧠 Ähnlichkeitssuche (Wissensdatenbank)")
    st.caption("Finden Sie ähnliche Fälle basierend auf Steuergerät, Kommunikationsart und Beschreibung.")

    col1, col2 = st.columns(2)
    with col1:
        ws_steuergeraet = st.text_input("Steuergerät:", key="ws_sg", placeholder="z.B. BGW")
        ws_kommunikation = st.selectbox("Kommunikationsart:", [""] + KOMMUNIKATIONSARTEN, key="ws_komm")
    with col2:
        ws_tags = st.text_input("Tags:", key="ws_tags", placeholder="z.B. Ethernet,Kommunikation")
        ws_beschreibung = st.text_input("Fehlerbeschreibung (Stichwörter):", key="ws_beschr",
                                        placeholder="z.B. Kommunikation instabil")

    if st.button("🧠 Ähnliche Fälle suchen", use_container_width=True):
        aehnliche = finde_aehnliche_faelle(
            steuergeraet=ws_steuergeraet,
            kommunikationsart=ws_kommunikation,
            fehlerbeschreibung=ws_beschreibung,
            tags=ws_tags,
        )
        if aehnliche:
            st.success(f"**{len(aehnliche)}** ähnliche(r) Fall/Fälle gefunden:")
            for f in aehnliche:
                with st.expander(f"Fall #{f.id} - {f.steuergeraet} ({f.kommunikationsart}) - {f.status}"):
                    st.write(f"**Projekt:** {f.projekt} | **Datum:** {f.datum}")
                    st.write(f"**Fehler:** {f.fehlerbeschreibung}")
                    st.write(f"**Ursache:** {f.ursache}")
                    st.write(f"**Lösung:** {f.loesung}")
                    st.write(f"**Lessons Learned:** {f.lessons_learned}")
        else:
            st.warning("Keine ähnlichen Fälle gefunden.")


# ============================================================
# SEITE: Alle Fälle
# ============================================================

elif seite == "📋 Alle Fälle":
    st.subheader("📋 Alle Fehlerfälle")

    alle_faelle = get_all_fehlerfaelle()

    if alle_faelle:
        # Suchfeld oberhalb der Tabelle
        suche_tabelle = st.text_input("🔎 Schnellsuche in Tabelle:", key="tabelle_suche",
                                      placeholder="Filtern nach Text...")

        data = []
        for f in alle_faelle:
            row = {
                "ID": f.id,
                "Datum": f.datum,
                "Projekt": f.projekt,
                "Baureihe": f.baureihe,
                "Fahrzeugnr.": f.fahrzeugnummer,
                "Steuergerät": f.steuergeraet,
                "Kommunikation": f.kommunikationsart,
                "Status": f"{STATUS_FARBEN.get(f.status, '')} {f.status}",
                "Ursache": f.root_cause_kategorie,
                "Fehler": f.fehlerbeschreibung[:50] + "..." if len(f.fehlerbeschreibung or "") > 50 else f.fehlerbeschreibung,
            }
            data.append(row)

        df = pd.DataFrame(data)

        # Schnellsuche anwenden
        if suche_tabelle:
            mask = df.apply(lambda row: row.astype(str).str.contains(suche_tabelle, case=False).any(), axis=1)
            df = df[mask]

        st.dataframe(df, use_container_width=True, hide_index=True)
        st.caption(f"Gesamt: {len(df)} Einträge")

        # Detailansicht und Bearbeitung
        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            detail_id = st.number_input("Fall-ID für Details/Bearbeitung:", min_value=1, step=1, key="alle_detail_id")
        with col2:
            action = st.radio("Aktion:", ["Details anzeigen", "Bearbeiten", "Löschen"], horizontal=True)

        if st.button("Ausführen", key="alle_action"):
            fall = get_fehlerfall(int(detail_id))
            if not fall:
                st.error(f"Fall mit ID {detail_id} nicht gefunden.")
            elif action == "Details anzeigen":
                st.markdown(f"### 📄 Fall #{fall.id} - {fall.steuergeraet}")
                with st.expander("🚗 Fahrzeuginformationen", expanded=True):
                    c1, c2, c3 = st.columns(3)
                    c1.write(f"**Datum:** {fall.datum}")
                    c1.write(f"**Projekt:** {fall.projekt}")
                    c1.write(f"**Baureihe:** {fall.baureihe}")
                    c2.write(f"**Fahrzeugnummer:** {fall.fahrzeugnummer}")
                    c2.write(f"**VIN:** {fall.vin}")
                    c2.write(f"**SW Fahrzeug:** {fall.softwarestand_fahrzeug}")
                    c3.write(f"**Verantwortlicher:** {fall.verantwortlicher}")
                    c3.write(f"**Steuergerät:** {fall.steuergeraet}")
                    c3.write(f"**Teilenummer:** {fall.teilenummer}")

                with st.expander("⚠️ Fehlerbeschreibung", expanded=True):
                    st.write(f"**Kommunikation:** {fall.kommunikationsart}")
                    st.write(f"**SW Steuergerät:** {fall.softwarestand_steuergeraet}")
                    st.write(f"**Fehlerbeschreibung:** {fall.fehlerbeschreibung}")
                    st.write(f"**Symptome:** {fall.fehlersymptome}")
                    if fall.diagnosecodes:
                        st.write(f"**DTCs:** {fall.diagnosecodes}")
                    if fall.logs:
                        st.code(fall.logs)

                with st.expander("🔬 Analyse", expanded=True):
                    st.write(f"**Tools:** {fall.verwendete_tools}")
                    st.write(f"**Schritte:** {fall.durchgefuehrte_schritte}")
                    if fall.messergebnisse:
                        st.write(f"**Messergebnisse:** {fall.messergebnisse}")
                    if fall.beobachtungen:
                        st.write(f"**Beobachtungen:** {fall.beobachtungen}")
                    if fall.kommunikationsanalyse:
                        st.write(f"**Kommunikationsanalyse:** {fall.kommunikationsanalyse}")

                with st.expander("✅ Ursache & Lösung", expanded=True):
                    st.write(f"**Ursache:** {fall.ursache}")
                    st.write(f"**Root Cause:** {fall.root_cause_kategorie}")
                    st.write(f"**Lösung:** {fall.loesung}")
                    st.write(f"**Lessons Learned:** {fall.lessons_learned}")
                    st.write(f"**Status:** {STATUS_FARBEN.get(fall.status, '')} {fall.status}")
                    st.write(f"**Tags:** {fall.tags}")

            elif action == "Löschen":
                if delete_fehlerfall(int(detail_id)):
                    st.success(f"✅ Fall #{detail_id} wurde gelöscht.")
                    st.rerun()
                else:
                    st.error("Fehler beim Löschen.")

            elif action == "Bearbeiten":
                st.session_state["edit_id"] = int(detail_id)
                st.session_state["edit_mode"] = True

    else:
        st.info("Noch keine Fehlerfälle vorhanden.")

    # Bearbeitungsmodus
    if st.session_state.get("edit_mode"):
        edit_id = st.session_state["edit_id"]
        fall = get_fehlerfall(edit_id)
        if fall:
            st.divider()
            st.markdown(f"### ✏️ Fall #{edit_id} bearbeiten")

            with st.form("edit_form"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    e_datum = st.date_input("Datum", value=fall.datum, key="e_datum")
                    e_projekt = st.text_input("Projekt", value=fall.projekt, key="e_projekt")
                    e_baureihe = st.text_input("Baureihe", value=fall.baureihe or "", key="e_baureihe")
                with col2:
                    e_fahrzeugnummer = st.text_input("Fahrzeugnummer", value=fall.fahrzeugnummer or "", key="e_fznr")
                    e_vin = st.text_input("VIN", value=fall.vin or "", key="e_vin")
                    e_sw_fz = st.text_input("SW Fahrzeug", value=fall.softwarestand_fahrzeug or "", key="e_sw_fz")
                with col3:
                    e_verantw = st.text_input("Verantwortlicher", value=fall.verantwortlicher or "", key="e_verantw")
                    e_sg = st.text_input("Steuergerät", value=fall.steuergeraet, key="e_sg")
                    e_tn = st.text_input("Teilenummer", value=fall.teilenummer or "", key="e_tn")

                e_sw_sg = st.text_input("SW Steuergerät", value=fall.softwarestand_steuergeraet or "", key="e_sw_sg")
                komm_idx = KOMMUNIKATIONSARTEN.index(fall.kommunikationsart) if fall.kommunikationsart in KOMMUNIKATIONSARTEN else 0
                e_komm = st.selectbox("Kommunikationsart", KOMMUNIKATIONSARTEN, index=komm_idx, key="e_komm")
                e_fehler = st.text_area("Fehlerbeschreibung", value=fall.fehlerbeschreibung or "", key="e_fehler")
                e_symptome = st.text_area("Symptome", value=fall.fehlersymptome or "", key="e_symptome")
                e_logs = st.text_area("Logs", value=fall.logs or "", key="e_logs")
                e_dtcs = st.text_area("DTCs", value=fall.diagnosecodes or "", key="e_dtcs")

                # Tools
                current_tools = [t.strip() for t in (fall.verwendete_tools or "").split(",") if t.strip()]
                e_tools = st.multiselect("Tools", TOOLS, default=[t for t in current_tools if t in TOOLS], key="e_tools")

                e_schritte = st.text_area("Durchgeführte Schritte", value=fall.durchgefuehrte_schritte or "", key="e_schritte")
                e_mess = st.text_area("Messergebnisse", value=fall.messergebnisse or "", key="e_mess")
                e_beob = st.text_area("Beobachtungen", value=fall.beobachtungen or "", key="e_beob")
                e_komm_analyse = st.text_area("Kommunikationsanalyse", value=fall.kommunikationsanalyse or "", key="e_komm_a")

                e_ursache = st.text_area("Ursache", value=fall.ursache or "", key="e_ursache")
                rc_idx = ROOT_CAUSE_KATEGORIEN.index(fall.root_cause_kategorie) if fall.root_cause_kategorie in ROOT_CAUSE_KATEGORIEN else 9
                e_rc = st.selectbox("Root Cause", ROOT_CAUSE_KATEGORIEN, index=rc_idx, key="e_rc")
                e_loesung = st.text_area("Lösung", value=fall.loesung or "", key="e_loesung")
                e_ll = st.text_area("Lessons Learned", value=fall.lessons_learned or "", key="e_ll")

                st_idx = STATUS_OPTIONEN.index(fall.status) if fall.status in STATUS_OPTIONEN else 0
                e_status = st.selectbox("Status", STATUS_OPTIONEN, index=st_idx, key="e_status")
                e_tags = st.text_input("Tags", value=fall.tags or "", key="e_tags")

                if st.form_submit_button("💾 Änderungen speichern", use_container_width=True):
                    update_data = {
                        "datum": e_datum,
                        "projekt": e_projekt,
                        "baureihe": e_baureihe,
                        "fahrzeugnummer": e_fahrzeugnummer,
                        "vin": e_vin,
                        "softwarestand_fahrzeug": e_sw_fz,
                        "verantwortlicher": e_verantw,
                        "steuergeraet": e_sg,
                        "teilenummer": e_tn,
                        "softwarestand_steuergeraet": e_sw_sg,
                        "kommunikationsart": e_komm,
                        "fehlerbeschreibung": e_fehler,
                        "fehlersymptome": e_symptome,
                        "logs": e_logs,
                        "diagnosecodes": e_dtcs,
                        "verwendete_tools": ",".join(e_tools),
                        "durchgefuehrte_schritte": e_schritte,
                        "messergebnisse": e_mess,
                        "beobachtungen": e_beob,
                        "kommunikationsanalyse": e_komm_analyse,
                        "ursache": e_ursache,
                        "root_cause_kategorie": e_rc,
                        "loesung": e_loesung,
                        "lessons_learned": e_ll,
                        "status": e_status,
                        "tags": e_tags,
                    }
                    update_fehlerfall(edit_id, update_data)
                    st.success("✅ Änderungen gespeichert!")
                    st.session_state["edit_mode"] = False
                    st.rerun()


# ============================================================
# SEITE: Export
# ============================================================

elif seite == "📤 Export":
    st.subheader("📤 Daten exportieren")

    df = get_dataframe()

    if df.empty:
        st.info("Keine Daten zum Exportieren vorhanden.")
    else:
        st.write(f"**{len(df)}** Datensätze verfügbar.")
        st.dataframe(df.head(10), use_container_width=True, hide_index=True)

        st.divider()

        col1, col2, col3 = st.columns(3)

        # CSV Export
        with col1:
            st.markdown("#### 📄 CSV Export")
            csv_data = df.to_csv(index=False, sep=";", encoding="utf-8-sig")
            st.download_button(
                label="⬇️ CSV herunterladen",
                data=csv_data,
                file_name=f"inbetriebnahme_export_{date.today().isoformat()}.csv",
                mime="text/csv",
                use_container_width=True,
            )

        # Excel Export
        with col2:
            st.markdown("#### 📊 Excel Export")
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                df.to_excel(writer, index=False, sheet_name="Fehlerfälle")
            st.download_button(
                label="⬇️ Excel herunterladen",
                data=buffer.getvalue(),
                file_name=f"inbetriebnahme_export_{date.today().isoformat()}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True,
            )

        # PDF Export
        with col3:
            st.markdown("#### 📑 PDF Export")
            if st.button("📑 PDF generieren", use_container_width=True):
                try:
                    from fpdf import FPDF

                    pdf = FPDF()
                    pdf.add_page(orientation="L")
                    pdf.set_font("Helvetica", "B", 14)
                    pdf.cell(0, 10, "Inbetriebnahme-Wissensdatenbank - Export", ln=True)
                    pdf.set_font("Helvetica", "", 8)
                    pdf.cell(0, 6, f"Exportiert am: {datetime.now().strftime('%d.%m.%Y %H:%M')}", ln=True)
                    pdf.ln(5)

                    # Tabellenkopf
                    pdf.set_font("Helvetica", "B", 7)
                    col_widths = [10, 20, 25, 25, 30, 30, 40, 40, 30]
                    headers = ["ID", "Datum", "Projekt", "Steuergeraet", "Kommunikation",
                               "Status", "Fehler", "Ursache", "Root Cause"]  # ASCII for PDF compatibility

                    for i, header in enumerate(headers):
                        pdf.cell(col_widths[i], 6, header, border=1)
                    pdf.ln()

                    # Daten
                    pdf.set_font("Helvetica", "", 6)
                    for _, row in df.iterrows():
                        values = [
                            str(row.get("ID", "")),
                            str(row.get("Datum", "")),
                            str(row.get("Projekt", ""))[:15],
                            str(row.get("Steuergeraet", ""))[:15],
                            str(row.get("Kommunikation", ""))[:18],
                            str(row.get("Status", ""))[:18],
                            str(row.get("Fehlerbeschreibung", ""))[:25],
                            str(row.get("Ursache", ""))[:25],
                            str(row.get("Root Cause", ""))[:18],
                        ]
                        for i, val in enumerate(values):
                            pdf.cell(col_widths[i], 5, val, border=1)
                        pdf.ln()

                    pdf_output = pdf.output()
                    st.download_button(
                        label="⬇️ PDF herunterladen",
                        data=pdf_output,
                        file_name=f"inbetriebnahme_export_{date.today().isoformat()}.pdf",
                        mime="application/pdf",
                        use_container_width=True,
                    )
                except ImportError:
                    st.error("PDF-Export benötigt das Paket 'fpdf2'. Bitte installieren: pip install fpdf2")


# ============================================================
# Footer
# ============================================================

st.divider()
st.markdown("""
<div style="text-align:center; color:#666; font-size:0.8rem; padding:1rem;">
    🔧 Inbetriebnahme-Wissensdatenbank | Automotive E/E | v1.0
</div>
""", unsafe_allow_html=True)
