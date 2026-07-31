# Gokulnath G L — Interactive Portfolio

The interactive companion to my [static portfolio site](https://fikalirous.github.io/portfolio/), built with [Streamlit](https://streamlit.io). Same case studies, but with live charts you can filter and a couple of simulations you can run yourself.

Live app: **TBD (pending Streamlit Community Cloud deploy)**

## Highlights

- **Climate & Agriculture** — pick a month and watch a real turbulence-intensity model re-fit itself to that month's wind data.
- **Policy & Rights** — filterable charts for UDID, CCPD, the Gates Foundation grants database, AI adoption research, and UDISE+ enrollment.
- **Public Health** — the live public TB survey dashboard, embedded.
- **Research** — a live agent-based simulator: drag the penalty/documentation-burden/strictness sliders and watch GPAI-provider compliance behavior recompute in real time, plus an interactive 33-country AI-regulation comparison tool.

## Structure

```
Home.py                        Landing page
pages/
  1_Climate_Agriculture.py
  2_Policy_Rights.py
  3_Public_Health.py
  4_Gender_Grassroots.py
  5_Research.py
  6_About.py
utils/theme.py                 Shared color palette + Plotly styling
data/                          Pre-aggregated CSVs (no raw/personal data — see note below)
assets/                        CV PDF
```

## Local development

```
pip install -r requirements.txt
streamlit run Home.py
```

## A note on the data

Every file in `data/` is either already-aggregate (counts, summary statistics, published survey
figures) or was aggregated specifically for this app. No row-level personal data, survey
microdata, or proprietary datasets are included — see the [static site's contribution
guide](https://github.com/fikalirous/portfolio#adding-a-new-project) for the same privacy
checklist this app follows.

## Deployment

Deployed on [Streamlit Community Cloud](https://streamlit.io/cloud), pointed at `Home.py` on
`main`. Community Cloud auto-redeploys on every push — no separate deploy step needed.
