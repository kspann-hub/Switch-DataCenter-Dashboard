import streamlit as st

# ─── Page Config (MUST be first) ─────────────────────────
st.set_page_config(
    page_title="CriticalArc Dashboard",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Global CSS ──────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600&family=Barlow+Condensed:wght@500;600;700&family=DM+Mono:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Barlow', sans-serif;
        color: #F0F0F0;
    }
    .main { background-color: #23262B; }

    section[data-testid="stSidebar"] {
        background-color: #2D3035;
        border-right: 1px solid #3E4248;
    }
    section[data-testid="stSidebar"] * { color: #C8CDD4 !important; }
    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] .element-container p,
    section[data-testid="stSidebar"] .stMarkdown p {
        font-size: 11px !important;
        letter-spacing: 1px !important;
    }
    section[data-testid="stSidebar"] .stSelectbox div {
        font-size: 13px !important;
    }

    .kpi-card {
        background: #2D3035;
        border: 1px solid #3E4248;
        border-radius: 10px;
        padding: 20px 24px;
        text-align: center;
        transition: border-color 0.2s;
    }
    .kpi-card:hover { border-color: #8A8F98; }
    .kpi-label {
        font-family: 'Barlow Condensed', sans-serif;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #8A8F98;
        margin-bottom: 8px;
    }
    .kpi-value {
        font-family: 'DM Mono', monospace;
        font-size: 32px;
        font-weight: 500;
        line-height: 1;
        margin-bottom: 4px;
    }
    .kpi-sub { font-size: 12px; color: #8A8F98; }
    .kpi-red    { color: #E04040; }
    .kpi-yellow { color: #F4B942; }
    .kpi-green  { color: #39B54A; }
    .kpi-blue   { color: #4A90D9; }
    .kpi-white  { color: #F0F0F0; }

    .section-header {
        font-family: 'Barlow Condensed', sans-serif;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #39B54A;
        margin: 24px 0 12px 0;
        padding-bottom: 8px;
        border-bottom: 1px solid #3E4248;
    }

    div[data-testid="stPills"] { width: 100% !important; }
    div[data-testid="stPills"] > div {
        display: flex !important;
        gap: 8px !important;
        width: 100% !important;
    }
    div[data-testid="stPills"] button {
        flex: 1 1 0 !important;
        justify-content: center !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        padding: 8px 12px !important;
        border: 1px solid #3E4248 !important;
        border-radius: 8px !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: #2D3035;
        padding: 4px;
        border-radius: 10px;
        border: 1px solid #3E4248;
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 6px;
        color: #8A8F98;
        font-family: 'Barlow Condensed', sans-serif;
        font-weight: 600;
        font-size: 13px;
        letter-spacing: 0.5px;
        padding: 8px 16px;
    }
    .stTabs [aria-selected="true"] {
        background: #34383E !important;
        color: #39B54A !important;
    }

    .stButton > button {
        font-family: 'Barlow Condensed', sans-serif;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        background: transparent;
        color: #F0F0F0;
        border: 1px solid #3E4248;
        border-radius: 6px;
        transition: background 0.15s, border-color 0.15s;
    }
    .stButton > button:hover {
        background: #34383E;
        border-color: #8A8F98;
        color: #F0F0F0;
    }

    .ca-brand {
        font-family: 'Barlow Condensed', sans-serif;
        font-size: 20px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        color: #F0F0F0;
        border-bottom: 2px solid #39B54A;
        padding-bottom: 12px;
        margin-bottom: 20px;
    }
    .ca-brand-sub {
        font-size: 11px;
        color: #8A8F98;
        letter-spacing: 1px;
        margin-top: 2px;
    }
</style>
""", unsafe_allow_html=True)

# ─── Navigation ──────────────────────────────────────────
home = st.Page("pages/CxA Tools.py", title="CxA Tools", icon="📐")
dashboard = st.Page("pages/dashboard.py", title="Dashboard", icon="📊", default=True)

pg = st.navigation([home, dashboard])
pg.run()