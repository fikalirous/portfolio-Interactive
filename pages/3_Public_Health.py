import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Public Health", page_icon="🏥", layout="wide")
st.title("🏥 Public Health")
st.caption("District-level TB surveillance database design and dashboarding")

st.markdown(
    "Contract work with the National Institute for Research in Tuberculosis, via Piramal Swasthya, "
    "designing the data model behind a district-level annual TB survey."
)

st.divider()

st.header("TB survey database design — NIRT / Piramal Swasthya")
st.markdown(
    """
**Context** — India's National Tuberculosis Elimination Programme is targeting an 80% reduction in
new TB cases by 2025. Because disease burden varies hugely across India's 753 districts, the
programme introduced District Level Annual Surveys (DLAS) and a subnational certification scheme.

**Role** — Designed the database supporting the 2022 District Level Annual Survey, and handled
ongoing data coordination with the field data-collection team.

**Method** — Data modeling for a household survey run through the WHO India Android app —
household screening, symptom checks, TB treatment history, and sputum sample results.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Households visited", "2.7M")
c2.metric("People interviewed", "8.99M")
c3.metric("Eligible for sputum", "121,045")
c4.metric("TB cases confirmed", "1,599")

st.markdown(
    "**Result** — The database held up at genuinely large scale, feeding directly into a "
    "certification scheme that rated districts Gold, Silver, or Bronze, and named Ladakh and "
    "Jammu & Kashmir the programme's first TB-free zones."
)

st.divider()

st.header("Metabase & Looker Studio dashboards")
st.markdown(
    "**Context** — A survey database is only useful if state and district teams can see where they "
    "stand without writing a SQL query. Built dashboards in Metabase (internal monitoring) and "
    "Looker Studio (public-facing reporting) on the same survey database."
)
st.markdown("The dashboard below is the actual live, public report — try clicking a bar in it.")

components.iframe(
    "https://datastudio.google.com/embed/reporting/7fb5c851-f868-4ca6-a866-6fa89939ce34/page/p_page",
    height=700,
    scrolling=True,
)
st.caption(
    "If the embed above doesn't load (Looker Studio sometimes blocks iframes), open it directly: "
    "https://datastudio.google.com/reporting/7fb5c851-f868-4ca6-a866-6fa89939ce34"
)

st.divider()

st.header("Mapping approaches for district-level health data")
st.markdown(
    """
**Context** — District-level health dashboards live or die on whether people can see where a
problem sits on a map. Compared three Python mapping approaches side-by-side on the same
state-level dataset.

**Method** — The same shapefile-plus-tabular-data merge, rendered three ways — Matplotlib (static,
full styling control), GeoPandas/GeoPlot (projection-aware static choropleths), and Folium
(interactive, Leaflet-based web maps).

**Result** — Each approach earned its keep for a different situation: Matplotlib for a static report
figure, GeoPlot when projection accuracy matters, and Folium when the map needs to be interactive
and embeddable — directly shaping which library to reach for on later district-level mapping work.
"""
)
