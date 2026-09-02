import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy.stats import kruskal

from utils.theme import MOSS, BRASS, SAGE, MUTED, CATEGORICAL, style_fig
from utils.nav import section_selector

st.set_page_config(page_title="Policy & Rights", page_icon="⚖️", layout="wide")
st.title("⚖️ Policy & Rights")
st.caption("Disability rights, CSR, and AI-adoption research at Pacta")

st.markdown(
    "Quantitative research in disability, law, and CSR at Pacta, a Bengaluru-based law firm and "
    "think tank — built on web scraping, EDA, and NLP applied to policy implementation gaps."
)

SECTIONS = [
    "UDID", "CCPD", "Gates Foundation", "AI Adoption", "UDISE+",
    "CSR & Sports", "eCourts", "TAN",
]
section = section_selector(SECTIONS, param="section")
st.divider()

# ---------------------------------------------------------------------------
if section == "UDID":
    st.subheader("UDID Implementation Study")
    st.markdown(
        "**Context** — The Unique Disability ID (UDID) is India's national digital identity system "
        "for persons with disabilities. Pacta studied how well it works on the ground, surveying "
        "PwDs and caregivers about applying for and receiving certification.\n\n"
        "**Method** — Data cleaning and EDA on 393 survey responses: demographic and disability-type "
        "breakdowns split by who reported (self vs. caregiver), rural/urban comparisons, and text "
        "cleaning of open-ended issue reports."
    )

    disab = pd.read_csv("data/udid_disability_by_reporter.csv")
    disab = disab.rename(columns={
        "Person with Disability": "Self-reported",
        "Parent/Caregiver to a Person with Disability": "Caregiver-reported",
    })
    disab = disab[disab["disability_type"] != "Not Sure"]
    disab["total"] = disab["Self-reported"] + disab["Caregiver-reported"]
    disab = disab.sort_values("total", ascending=True)

    view = st.radio("View", ["Split by reporter", "Rural vs. urban issues"], horizontal=True, key="udid_view")

    if view == "Split by reporter":
        fig = go.Figure()
        fig.add_trace(go.Bar(y=disab["disability_type"], x=disab["Self-reported"], name="Self-reported",
                              orientation="h", marker_color=MOSS))
        fig.add_trace(go.Bar(y=disab["disability_type"], x=disab["Caregiver-reported"], name="Caregiver-reported",
                              orientation="h", marker_color=BRASS))
        fig.update_layout(barmode="group")
        style_fig(fig, title="Disability type, by who reported it", height=480)
        st.plotly_chart(fig, use_container_width=True)
        st.caption(
            "Parents report far more Autism Spectrum Disorder (70) than self-reporting respondents "
            "do (3) — a gap worth flagging for anyone designing the intake form."
        )
    else:
        issues = pd.read_csv("data/udid_issues_by_area.csv")
        fig = px.bar(issues, x="area", y="count", color="issue_type", barmode="stack",
                     color_discrete_sequence=[BRASS, MOSS, SAGE])
        style_fig(fig, title="UDID application issues by area", height=480)
        fig.update_xaxes(title="")
        fig.update_yaxes(title="Issues logged")
        st.plotly_chart(fig, use_container_width=True)
        st.caption(
            "Urban respondents logged more total issues (78) than rural ones (60) — cutting against "
            "the assumption that access problems are purely a rural gap."
        )

    st.info(
        "**Result** — The self-report vs. caregiver-report divergence in disability type pointed to "
        "a real weakness in how the UDID form collects diagnosis data. Raw survey data (birth dates, "
        "city, diagnosis) isn't shipped here — only these aggregate counts."
    )

# ---------------------------------------------------------------------------
elif section == "CCPD":
    st.subheader("CCPD disability & subject-matter profiling")
    st.markdown(
        "**Context** — The Office of the Chief Commissioner for Persons with Disabilities (CCPD) is "
        "India's statutory grievance redressal body. Pacta analyzed a year of CCPD case data — 369 "
        "complaints filed in 2023 — to see who files complaints and what they're about.\n\n"
        "**Method** — Cross-tabulations of complainant profile against disability type, subject "
        "matter, and state."
    )

    profile_disab = pd.read_csv("data/ccpd_profile_disability.csv")
    profile_subj = pd.read_csv("data/ccpd_profile_subjectmatter.csv")
    state_disab = pd.read_csv("data/ccpd_state_disability.csv")

    view = st.radio("View", ["By disability type", "By subject matter", "By state"], horizontal=True, key="ccpd_view")

    if view == "By disability type":
        top = profile_disab.groupby("Disability")["count"].sum().sort_values(ascending=False).head(10)
        fig = px.bar(top, orientation="h", color_discrete_sequence=[MOSS])
        style_fig(fig, title="Top 10 disability types in CCPD complaints", height=450)
        fig.update_layout(showlegend=False)
        fig.update_yaxes(title="")
        fig.update_xaxes(title="Cases")
        st.plotly_chart(fig, use_container_width=True)
    elif view == "By subject matter":
        top = profile_subj.groupby("Category")["count"].sum().sort_values(ascending=False)
        fig = px.bar(top, orientation="h", color_discrete_sequence=[BRASS])
        style_fig(fig, title="CCPD complaints by subject matter", height=400)
        fig.update_layout(showlegend=False)
        fig.update_yaxes(title="")
        fig.update_xaxes(title="Cases")
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Employment/livelihood complaints (204 cases) dwarf every other category combined.")
    else:
        top = state_disab.groupby("State_UT")["count"].sum().sort_values(ascending=False).head(15)
        fig = px.bar(top, orientation="h", color_discrete_sequence=[SAGE])
        style_fig(fig, title="Top 15 states/UTs by CCPD case count", height=500)
        fig.update_layout(showlegend=False)
        fig.update_yaxes(title="")
        fig.update_xaxes(title="Cases")
        st.plotly_chart(fig, use_container_width=True)

    st.info(
        "**Result** — Employment and livelihood complaints dominate the CCPD caseload, filed "
        "overwhelmingly by persons with disabilities themselves rather than caregivers or advocates."
    )
    st.caption("Referenced in a [LinkedIn post](https://www.linkedin.com/posts/disabilityrights-accessibility-inclusion-share-7376214743419822080-yp-S/) crediting the analysis.")

# ---------------------------------------------------------------------------
elif section == "Gates Foundation":
    st.subheader("Gates Foundation grants database (BMGF)")
    st.markdown(
        "**Context** — Where does Gates Foundation health-tech money actually land in India? "
        "Scraped the public [Committed Grants Database](https://www.gatesfoundation.org/about/committed-grants) "
        "— 36,564 grants worldwide, filtered to India's tech-in-health subset.\n\n"
        "**Method** — Python scraping and cleaning; successive filtering (global → India → health → "
        "tech-in-health); grouped by state."
    )

    bmgf = pd.read_csv("data/bmgf_statewise_tech.csv").sort_values("Total_Amount_Committed", ascending=True)
    metric = st.radio("Sort/size by", ["Amount committed", "Project count"], horizontal=True, key="bmgf_metric")
    col = "Total_Amount_Committed" if metric == "Amount committed" else "Tech_Project_Count"
    bmgf_sorted = bmgf.sort_values(col, ascending=True)

    fig = px.bar(
        bmgf_sorted, x=col, y="State", orientation="h",
        color_discrete_sequence=[MOSS],
        hover_data={"Total_Amount_Committed": ":,.0f", "Tech_Project_Count": True},
    )
    style_fig(fig, title=f"Gates Foundation tech-in-health grants by state — {metric.lower()}", height=500)
    fig.update_layout(showlegend=False)
    fig.update_yaxes(title="")
    fig.update_xaxes(title="USD committed" if metric == "Amount committed" else "Projects")
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "**Result** — Delhi alone accounts for over $200M of tech-in-health commitments — more than "
        "Telangana, Tamil Nadu, and Karnataka combined — despite having far fewer people than those "
        "states. Money follows headquarters and implementing-partner presence, not necessarily need."
    )

# ---------------------------------------------------------------------------
elif section == "AI Adoption":
    st.subheader("AI readiness & adoption in the nonprofit sector — with Giving Tuesday")
    st.markdown(
        "**Context** — GivingTuesday's Generosity AI Working Group surveyed 930 nonprofits worldwide "
        "on AI readiness in 2024, with a 251-organization India supplement. I built an independent "
        "statistical layer testing whether region, role, or org size actually predict an "
        "individual's comfort with AI.\n\n"
        "**Method** — Kruskal-Wallis tests for AI comfort against region, role, and organization size "
        "across 230 India responses."
    )

    stats = pd.read_csv("data/ai_comfort_summary_stats.csv")

    group_choice = st.selectbox("Break down comfort by", ["india_rural_urban", "role", "org_size"],
                                 format_func=lambda x: {"india_rural_urban": "Region (rural/urban/metro)",
                                                         "role": "Respondent role", "org_size": "Organization size"}[x],
                                 key="ai_group")
    sub = stats[stats["group_var"] == group_choice].sort_values("median")

    fig = go.Figure()
    fig.add_trace(go.Box(
        q1=sub["q1"], median=sub["median"], q3=sub["q3"],
        lowerfence=sub["min"], upperfence=sub["max"],
        x=sub["group"], name="", marker_color=MOSS,
        boxpoints=False,
    ))
    style_fig(fig, title="AI comfort (0–10) by group — India respondents", height=450)
    fig.update_yaxes(title="Self-reported AI comfort (0–10)")
    fig.update_xaxes(title="")
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

    # Reconstruct an approximate Kruskal-Wallis from the summary stats isn't exact,
    # so show the pre-computed reference result for region (from the original analysis).
    if group_choice == "india_rural_urban":
        st.caption("Kruskal-Wallis p = 0.27 across rural/urban/metro (n=210) — no significant difference.")
    elif group_choice == "role":
        st.caption("Kruskal-Wallis p = 0.26 across roles (n=211) — no significant difference.")
    else:
        st.caption("Kruskal-Wallis p = 0.07 across org sizes (n=211) — borderline, not significant at p<.05.")

    st.info(
        "**Result** — None of the usual org-level predictors held up statistically at the individual "
        "level. The published 'early vs. late adopter' story (built on organizational capacity) "
        "explains which *organizations* move first, but not which *people* feel comfortable with AI."
    )

# ---------------------------------------------------------------------------
elif section == "UDISE+":
    st.subheader("UDISE+ education data analysis")
    st.markdown(
        "**Context** — UDISE+ is India's national school database. Used it to check how well the "
        "school system serves Children with Special Needs (CWSN) — not just enrollment, but whether "
        "they stay enrolled.\n\n"
        "**Method** — Aggregated enrollment by grade, gender, and disability type across all districts, "
        "plus a district-level correlation between special-educator staffing and CwD enrollment."
    )

    view = st.radio("View", ["Enrollment by grade & gender", "Disability type"], horizontal=True, key="udise_view")

    if view == "Enrollment by grade & gender":
        enr = pd.read_csv("data/udise_enrollment.csv")
        order = enr["grade"].tolist()
        show_total = st.checkbox("Show total instead of gender split", value=False)
        fig = go.Figure()
        if show_total:
            enr["total"] = enr["boys"] + enr["girls"]
            fig.add_trace(go.Bar(x=enr["grade"], y=enr["total"], marker_color=MOSS))
        else:
            fig.add_trace(go.Bar(x=enr["grade"], y=enr["boys"], name="Boys", marker_color=MOSS))
            fig.add_trace(go.Bar(x=enr["grade"], y=enr["girls"], name="Girls", marker_color=BRASS))
        fig.update_xaxes(categoryorder="array", categoryarray=order, tickangle=-45)
        style_fig(fig, title="CWSN enrollment by grade", height=450)
        fig.update_yaxes(title="# of students")
        st.plotly_chart(fig, use_container_width=True)
        st.caption(
            "Enrollment climbs to a peak of ~280,000 at Class V, then falls 82% by Class XII — and "
            "girls are outnumbered by boys at every single grade."
        )
    else:
        dtype = pd.read_csv("data/udise_disability_type.csv").sort_values("pct", ascending=False)
        fig = px.pie(dtype, names="disability_type", values="pct", color_discrete_sequence=CATEGORICAL)
        style_fig(fig, title="CWSN enrollment by disability type", height=450)
        st.plotly_chart(fig, use_container_width=True)

    st.info(
        "**Result** — District-level special-educator staffing correlates moderately with CwD "
        "enrollment (r = 0.47 across 747 districts) — not proof of causation, but consistent with "
        "educator availability being one real lever behind whether children with disabilities stay "
        "in school."
    )

# ---------------------------------------------------------------------------
elif section == "CSR & Sports":
    st.subheader("CSR & sports development analysis")
    st.markdown(
        """
**Context** — CSR spending has been legally mandated in India since 2014, but almost no one had
traced how much reaches sports. Pacta partnered with the Sports and Society Accelerator to build
that picture across the mandate's first decade (2014–2023).

**Method** — Selenium/requests scraping of India's official CSR portal across four fiscal years,
company-level deep dives, and comparative analysis of listed vs. unlisted companies and state-wise
spending.

**Output** — *CSR and Sports in India — The First Decade*, co-published with the Sports and Society
Accelerator, presented across two public Data Walk sessions, [announced on
LinkedIn](https://www.linkedin.com/posts/gokulnath-g-l-13071a178_csr-sports-in-india-pacta-june-2025-activity-7349091829461508096-7ubI/).

**Result** — The combined dataset spanned over 1,000 companies' sports-related CSR disclosures
across a decade, identifying where CSR-to-sports funding concentrates and where it's structurally
thin.
"""
    )

# ---------------------------------------------------------------------------
elif section == "eCourts":
    st.subheader("eCourts case-completion database")
    st.markdown(
        """
**Context** — After a personal experience of losing a court case with little visibility into how it
was progressing, the idea was to build a public database of completed cases by state using India's
[eCourts](https://ecourts.gov.in/ecourts2.0/) system.

**Method** — `requests`/BeautifulSoup for static pages, Selenium for JavaScript-rendered case-status
tables, generalized from a single district court into a district-list-driven scraper.

**Result** — The proof of concept held up at state scale (all of Karnataka's district courts),
validating the approach before the harder problem of scaling nationally.
"""
    )
    st.caption(
        "Only the scraping methodology is described here — case-level data (which includes "
        "petitioner and respondent names) isn't published, even though the source records are public."
    )

# ---------------------------------------------------------------------------
elif section == "TAN":
    st.subheader("TAN — The Accessibility Network M&E framework")
    st.markdown(
        """
**Context** — The Accessibility Network (TAN) is a Tech Mahindra Foundation platform connecting
persons with disabilities to service providers, with at least four stakeholders who each need a
different reason to care whether it works.

**Method** — Outcome mapping: four parallel, color-coded causal chains (one per stakeholder) running
from immediate platform behaviors to each group's long-term outcome.

**Output** — The Outcome Framework, part of Pacta's
[TAN evaluation](https://www.linkedin.com/posts/tan-report-announcement-ugcPost-7394315754814214144-ifEZ/).

**Result** — Platform usage isn't the end goal, it's the lever: increased usage feeds
service-provider registration, which feeds funder interest and government buy-in, which sustains
the platform for the people who actually need it.
"""
    )
    st.image("https://raw.githubusercontent.com/fikalirous/portfolio/main/assets/tan/outcome-framework.png",
              caption="TAN's outcome framework across four stakeholder groups.")
