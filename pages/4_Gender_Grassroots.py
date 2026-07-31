import streamlit as st
import pandas as pd
import plotly.express as px

from utils.theme import MOSS, BRASS, SAGE, style_fig

st.set_page_config(page_title="Gender & Grassroots", page_icon="🤝", layout="wide")
st.title("🤝 Gender & Grassroots")
st.caption("Mapping women- and trans-led organizations across Indian states")

st.markdown(
    "A short consulting engagement with the South Asia Women's Fund India, combining directory "
    "scraping with interview-based fieldwork to map grassroots organizations led by women and "
    "trans people."
)

st.divider()

st.header("Women- and trans-led organization database — SAWF India")
st.markdown(
    """
**Context** — SAWF India needed a working database of women- and trans-led organizations across
Indian states to identify potential grant recipients and partners — no comprehensive directory of
this kind existed for the states in scope.

**Role** — Built the scraping pipeline and sector classification behind the database, covering
Odisha, Chhattisgarh, and Rajasthan.

**Method** — Python (BeautifulSoup) scraping of India's NGO Darpan registry, state by state,
followed by sector-wise classification to identify which sectors most directly involve women.
"""
)

counts = pd.read_csv("data/sawf_ngo_counts.csv").sort_values("ngo_count", ascending=True)
fig = px.bar(counts, x="ngo_count", y="state", orientation="h",
             color_discrete_sequence=[MOSS], text="ngo_count")
style_fig(fig, title="NGOs scraped from the Darpan registry, by state", height=320)
fig.update_traces(textposition="outside")
fig.update_xaxes(title="NGOs scraped")
fig.update_yaxes(title="")
fig.update_layout(showlegend=False)
st.plotly_chart(fig, use_container_width=True)

st.markdown("**Sectors identified as most directly relevant to women's development:**")
sectors = {
    "Women's Development & Empowerment": "Skills training, microfinance support, legal aid, and advocacy for women's rights.",
    "Health & Family Welfare": "Maternal health, reproductive rights, and child nutrition.",
    "Microfinance (SHGs)": "Women-led self-help groups: collective savings, credit access, small-scale entrepreneurship.",
    "Micro, Small & Medium Enterprises": "Women entrepreneurs in handicrafts, food production, and retail.",
    "Nutrition": "Programs addressing malnutrition, maternal and child health, and food security.",
}
for name, desc in sectors.items():
    st.markdown(f"- **{name}** — {desc}")

st.info(
    "**Result** — The scrape covered 3,100 organizations across three states, giving SAWF's team a "
    "starting point that combined real breadth with the judgment needed to separate genuinely "
    "women-focused organizations from Darpan's broader registry. That directory fed directly into "
    "the interview-based fieldwork that followed."
)
