import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Personal Projects", page_icon="📊", layout="wide")
st.title("📊 Personal Projects")
st.caption("Self-directed dashboards and analyses, in the order I built them")

st.markdown(
    "Smaller, self-directed work — mostly Tableau and Canva — built to practice a specific skill "
    "or explore a dataset that interested me, outside of any client or coursework brief. The "
    "Tableau dashboards are embedded live below; the Canva pieces open in a new tab."
)

st.divider()

st.header("1. Attribution Analytics")
st.markdown(
    "A dashboard exploring what drives employee attrition — job satisfaction and work-life "
    "balance as the two lenses on why people leave."
)
components.iframe(
    "https://public.tableau.com/views/onwork/Dashboard1?:showVizHome=no&:embed=true",
    height=650, scrolling=True,
)


st.divider()

st.header("1. Attribution Analytics")
st.markdown(
    "A dashboard exploring what drives employee attrition — job satisfaction and work-life "
    "balance as the two lenses on why people leave."
)
components.iframe(
    "https://public.tableau.com/views/onwork/Dashboard1?:showVizHome=no&:embed=true",
    height=1000, scrolling=True,
)

st.divider()

st.header("2. Global Power Plant")
st.markdown(
    "Built on 2022 global power generation data: a detailed dashboard breaking down power "
    "generation and major fuel sources by country, across the globe."
)
components.iframe(
    "https://public.tableau.com/views/GlobalPowerPlant_17201742036450/Dashboard1?:showVizHome=no&:embed=true",
    height=650, scrolling=True,
)

st.divider()

st.header("3. School Dropout Rates")
st.markdown(
    "Analyzed student dropout rates across Indian states by educational level — Primary through "
    "Higher Secondary — from 2012 to 2015, using the government's 'Drop-out data' dataset."
)
st.link_button("Open in Canva →", "https://www.canva.com/design/DAGIqEBo8Dc/xR47D3sMk_dWzQxOuF3X-A/view")

st.divider()

st.header("4. Netflix Business Case")
st.markdown(
    "Used Python to analyze Netflix's revenue model over a 10-year span, with visualizations "
    "built to support a recommendation on increasing viewership."
)
st.link_button("Open in Canva →", "https://www.canva.com/design/DAGIvbSUo3c/mDXJg252CJebkGfPECFZ5w/view")

st.divider()

st.header("5. Annual Greenhouse Gas Index")
st.markdown(
    "A companion piece to the Global Power Plant dashboard: the same 2022 global generation "
    "data, read through the lens of the Annual Greenhouse Gas Index (AGGI) and each fuel "
    "source's contribution to it."
)
components.iframe(
    "https://public.tableau.com/views/AnnualGreenhouseGasIndexAGGI_17067037671620/Dashboard1?:showVizHome=no&:embed=true",
    height=650, scrolling=True,
)

st.caption(
    "If an embed above doesn't load (Tableau Public occasionally blocks iframes), open it "
    "directly on Tableau Public — links are in each section's title area of the static site."
)
