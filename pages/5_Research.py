import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from utils.theme import MOSS, BRASS, SAGE, MUTED, REGION_COLORS, style_fig
from utils.nav import section_selector

st.set_page_config(page_title="Research", page_icon="🔬", layout="wide")
st.title("🔬 Research")
st.caption("Digital inclusion, AI governance, and simulation — MSc Social Data Science, UCD")

st.markdown(
    "Coursework and research from my MSc at University College Dublin: human values and digital "
    "inclusion using the European Social Survey, a quantitative text analysis of global AI "
    "regulation, and an agent-based model of regulatory compliance."
)

SECTIONS = ["Human Values & ESS", "AI Regulatory Landscape", "AI Regulation — ABM Simulator"]
section = section_selector(SECTIONS, param="section")
st.divider()

# ---------------------------------------------------------------------------
if section == "Human Values & ESS":
    st.subheader("Human values & internet engagement — European Social Survey")
    st.markdown(
        """
**Context** — Does what people *value* — not just their age or education — shape how they engage
with the internet? Tested this in Ireland using four rounds of the European Social Survey
(2016–2023): 24,250 respondents overall, narrowing to 4,677 in the final regression sample.

**Method** — Weighted descriptives, a three-model OLS sequence (values-only baseline → demographic
controls → full Schwartz value decomposition), an ordinal logistic regression, and six interaction
models testing whether the values effect concentrated in a particular age, gender, or education
group.

**Result** — Conservation values, not openness, were the value dimension that mattered: holding more
conservative values predicted meaningfully lower internet engagement even after controlling for
age, education, gender, and income (β = −0.065, p < .01). That effect was small next to the
demographic controls — R² went from 0.042 to 0.233 once controls were added — and none of the six
interaction tests found the effect concentrated in a particular group.
"""
    )
    st.link_button("Open the companion dashboard →", "https://essround11viz.streamlit.app/")

# ---------------------------------------------------------------------------
elif section == "AI Regulatory Landscape":
    st.subheader("Mapping the Global AI Regulatory Landscape")
    st.markdown(
        """
**Context** — Most comparative AI-regulation research looks only at the EU, US, and China. Built a
quantitative text analysis covering 33 jurisdictions across six regions, using
[White & Case's AI Watch Global Regulatory Tracker](https://www.whitecase.com/insight-our-thinking/ai-watch-global-regulatory-tracker).

**Method** — Word-frequency and keyness analysis; a domain-specific dictionary from the MIT sAIpien
Glossary (55 AI concepts, 5 categories) to measure technical-vocabulary coverage; cosine similarity
to the EU AI Act to test the "Brussels Effect"; an ethics-vs-technical framing index; and a
restrictive-vs-permissive tone classifier.
"""
    )

    @st.cache_data
    def load_qta():
        return pd.read_csv("data/qta_summary_33_countries.csv")

    qta = load_qta()

    metric_labels = {
        "coverage_pct": "AI terminology coverage (%)",
        "ethics_pct": "Ethics & governance framing (%)",
        "framing_index": "Ethics vs. technical framing index",
        "sim_to_EU": "Similarity to EU AI Act (cosine)",
    }
    metric = st.selectbox("Metric", list(metric_labels.keys()), format_func=lambda k: metric_labels[k])

    regions = sorted(qta["region"].unique())
    selected_regions = st.multiselect("Filter by region", regions, default=regions)
    filtered = qta[qta["region"].isin(selected_regions)].sort_values(metric, ascending=True)

    fig = px.bar(
        filtered, x=metric, y="country", orientation="h", color="region",
        color_discrete_map=REGION_COLORS,
        height=max(400, len(filtered) * 22),
    )
    style_fig(fig, title=f"{metric_labels[metric]} — 33 regulatory frameworks")
    fig.update_yaxes(title="")
    fig.update_xaxes(title=metric_labels[metric])
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "**Result** — Ethics-and-governance language dominates technical language in 28 of the 33 "
        "frameworks — not just European ones. The Brussels Effect test found real but partial "
        "diffusion: similarity to the EU AI Act ranges narrowly from 0.18 to 0.33 across all 33 "
        "jurisdictions, with South Korea, Taiwan, Germany, and Italy closest."
    )

# ---------------------------------------------------------------------------
elif section == "AI Regulation — ABM Simulator":
    st.subheader("Adoption of AI Regulation — live Agent-Based Model")
    st.markdown(
        """
**Context** — The EU AI Act places the heaviest compliance burden on General-Purpose AI (GPAI)
providers like OpenAI, Anthropic, Google, and Meta — but providers responded unevenly to the
voluntary Code of Practice. This model (originally built in NetLogo) tests which regulatory design
choices actually drive that compliance decision. **Adjust the sliders below to re-run the exact
model live.**
"""
    )

    col_a, col_b = st.columns([1, 2])
    with col_a:
        population_size = st.slider("Number of GPAI providers (agents)", 20, 300, 150, step=10)
        base_penalty = st.slider("Base penalty", 0.0, 1.0, 0.5, step=0.05)
        base_burden = st.slider("Documentation burden", 0.0, 1.0, 0.3, step=0.05)
        regulator_strictness = st.slider("Regulator strictness", 0.0, 1.0, 0.5, step=0.05)
        seed = st.number_input("Random seed (agent traits)", value=42, step=1)
        st.caption(
            "In the original model, regulator strictness isn't actually wired into any agent's "
            "compliance decision — try moving it on its own and watch the outcome barely change. "
            "That's the paper's own finding: strictness alone doesn't drive compliance."
        )

    rng = np.random.default_rng(int(seed))
    trust = rng.random(population_size)
    innovation_priority = rng.random(population_size)
    compliance_cost_sensitivity = rng.random(population_size)

    penalty_impact = base_penalty * trust
    burden_impact = base_burden * compliance_cost_sensitivity
    innovation_pressure = innovation_priority

    cp = penalty_impact - burden_impact - 0.4 * innovation_pressure
    cp = np.clip(cp, 0, 1)

    r = rng.random(population_size)
    status = np.where(r < cp, "Complier", np.where(r < cp + 0.2, "Partial", "Resistant"))

    with col_b:
        counts = pd.Series(status).value_counts().reindex(["Complier", "Partial", "Resistant"]).fillna(0)
        color_map = {"Complier": MOSS, "Partial": BRASS, "Resistant": "#B0413E"}

        fig = go.Figure(go.Bar(
            x=counts.index, y=counts.values,
            marker_color=[color_map[s] for s in counts.index],
            text=counts.values, textposition="outside",
        ))
        style_fig(fig, title="Agent status distribution", height=380)
        fig.update_yaxes(title="# of agents", range=[0, population_size])
        fig.update_xaxes(title="")
        st.plotly_chart(fig, use_container_width=True)

        m1, m2, m3 = st.columns(3)
        m1.metric("Compliers", f"{counts['Complier']:.0f}", f"{counts['Complier']/population_size:.0%}")
        m2.metric("Partial", f"{counts['Partial']:.0f}", f"{counts['Partial']/population_size:.0%}")
        m3.metric("Resistant", f"{counts['Resistant']:.0f}", f"{counts['Resistant']/population_size:.0%}")

        scatter = pd.DataFrame({
            "trust": trust, "innovation_priority": innovation_priority, "status": status,
        })
        fig2 = px.scatter(
            scatter, x="trust", y="innovation_priority", color="status",
            color_discrete_map=color_map,
        )
        style_fig(fig2, title="Agents by trust in regulator vs. innovation priority", height=380)
        fig2.update_xaxes(title="Trust in regulator")
        fig2.update_yaxes(title="Innovation priority")
        st.plotly_chart(fig2, use_container_width=True)

    st.info(
        "**Result from the original 60-run factorial experiment** — Penalty strength was the "
        "strongest positive driver of compliance; documentation burden was consistently the "
        "strongest negative driver, suppressing compliance even under the highest penalty tested; "
        "regulator strictness barely moved the outcome on its own. Try pushing penalty to 1.0 and "
        "burden to 0.0 above — that's the model's best case for compliance, and even then, "
        "resistant agents don't disappear."
    )
