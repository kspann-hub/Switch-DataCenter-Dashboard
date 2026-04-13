import streamlit as st


st.title("CxA Tools")

# ── Embedded Google Doc ──
st.markdown("### RN0O4 Batters Box")
google_doc_url = "https://docs.google.com/spreadsheets/d/1tcmhvgGq-sEFPgM3eYUrggoFBhOTUTfr_I2So9B3AMo/edit?usp=sharing"  # use /pub not /edit
st.components.v1.iframe(google_doc_url, height=600, scrolling=True)


# ── Embedded Google Doc ──
st.markdown("### RN0O4 Equipment Status Tracker")
google_doc_url = "https://docs.google.com/spreadsheets/d/1vMbYOMoYhNbuAV-NhJ4aEjqKUpJDIEwqtOz-tG2u5YM/edit?usp=sharing"  # use /pub not /edit
st.components.v1.iframe(google_doc_url, height=600, scrolling=True)