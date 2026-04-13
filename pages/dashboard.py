import streamlit as st
import os
import sys
import pandas as pd
import importlib.util
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils.cxalloy import load_all_projects, load_project_data
from background_sync import start_background_sync

start_background_sync()

# ─── Utils ────────────────────────────────────────────────
def safe_get(sheets, key):
    val = sheets.get(key) if sheets else None
    return val if val is not None else pd.DataFrame()

# ─── Load Projects ────────────────────────────────────────
projects_df = load_all_projects()

# ─── Sidebar ─────────────────────────────────────────────
with st.sidebar:
    if projects_df.empty:
        st.error("No projects found.")
        st.stop()

    project_names = dict(zip(projects_df['project_id'], projects_df['name']))

    selected_project_id = st.selectbox(
        "Select Project",
        options=list(project_names.keys()),
        format_func=lambda k: project_names[k]
    )

    st.markdown("---")
    st.markdown("**Filters**")

    try:
        with st.spinner("Loading data..."):
            all_sheets     = load_project_data(selected_project_id)
            issues_raw     = safe_get(all_sheets, 'Issues')
            checklists_raw = safe_get(all_sheets, 'Checklists')
            tests_raw      = safe_get(all_sheets, 'Tests')
            equipment_raw  = safe_get(all_sheets, 'Equipment')
            companies_raw  = safe_get(all_sheets, 'Companies')
    except Exception as e:
        st.warning(f"Could not load data: {e}")
        issues_raw     = pd.DataFrame()
        checklists_raw = pd.DataFrame()
        tests_raw      = pd.DataFrame()
        equipment_raw  = pd.DataFrame()
        companies_raw  = pd.DataFrame()
        all_sheets     = {}

    disciplines = ["All"]
    if not equipment_raw.empty and "discipline" in equipment_raw.columns:
        disciplines += sorted([
            d for d in equipment_raw["discipline"].dropna().unique()
            if d and str(d) not in ['0', 'nan', 'None', '']
        ])

    contractors = ["All"]
    if not companies_raw.empty and "name" in companies_raw.columns:
        contractors += sorted([
            c for c in companies_raw["name"].dropna().unique()
            if c and str(c) not in ['0', 'nan', 'None', '']
        ])

    filters = {
        "discipline": st.selectbox("Division / Discipline", disciplines, key="filter_discipline"),
        "contractor": st.selectbox("Contractor / Assigned To", contractors, key="filter_contractor")
    }

    st.markdown("---")
    st.markdown(
        f"<div style='font-size:11px; color:#8A8F98;'>Refreshed: {datetime.now().strftime('%b %d %H:%M')}</div>",
        unsafe_allow_html=True
    )
    if st.button("🔄 Refresh Data"):
        st.cache_data.clear()
        st.rerun()

# ─── Header ──────────────────────────────────────────────
project_name = project_names.get(selected_project_id, "Project Dashboard")

st.html(f"""
<div style="padding: 8px 0 0 0; display: flex; justify-content: space-between; align-items: flex-start;">
    <div>
        <div style="
            font-family: 'Barlow Condensed', sans-serif;
            font-size: 42px;
            font-weight: 700;
            letter-spacing: 1px;
            color: #2D3035;
            text-transform: uppercase;
            line-height: 1.1;
        ">{project_name}</div>
        <div style="
            font-family: 'Barlow', sans-serif;
            font-size: 14px;
            color: #8A8F98;
            margin-top: 4px;
            letter-spacing: 0.5px;
        ">Commissioning Progress Dashboard</div>
        <div style="
            font-family: 'Barlow', sans-serif;
            font-size: 12px;
            color: #5A5F68;
            margin-top: 6px;
            letter-spacing: 0.5px;
        ">Data last refreshed: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</div>
    </div>
    <img src="YOUR_LOGO_URL" alt="CriticalArc" style="
        height: 60px;
        object-fit: contain;
        margin-top: 4px;
    ">
</div>
<hr style="border: none; border-top: 1px solid #3E4248; margin-top: 16px;">
""")

# ─── Render Layout ───────────────────────────────────────
layout_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "layout.py")
spec = importlib.util.spec_from_file_location("layout", layout_path)
layout_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(layout_mod)
layout_mod.render(
    {"project_id": selected_project_id, "project_name": project_names[selected_project_id]},
    filters,
    all_sheets
)