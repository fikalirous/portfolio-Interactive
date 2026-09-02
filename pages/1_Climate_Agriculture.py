import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

from utils.theme import MOSS, BRASS, MUTED, style_fig

st.set_page_config(page_title="Climate & Agriculture", page_icon="🌦️", layout="wide")
st.title("🌦️ Climate & Agriculture")


st.divider()

# ---------------------------------------------------------------------------
st.header("Weather data extraction & turbulence-intensity analysis ")
st.markdown(
    """
**turbulence intensity** — how much wind speed fluctuates around its mean — at Indian wind farm sites, since turbulence directly
affects turbine loading and IEC site suitability classification.

Built a Python pipeline to analyse turbulence intensity across multiple wind turbines based on the Meteoblue weather data, helping improve understanding of wind
conditions for generation forecasting. Processed turbine wind-speed data at 15-minute intervals and modelled turbulence intensity for each
turbine and month. The analysis provided a full-year view of turbulence patterns across wind farm sites. 
`TI = α·v^β + c` fit per month via nonlinear least squares. 
"""
)

st.markdown("#### 🔧 Try it yourself — turbulence model, 2023")
st.caption(
    "Pick a month to see the real 15-minute wind-speed readings from this turbine, the fitted "
    "turbulence model, and how well it actually explains the data that month."
)


@st.cache_data
def load_turbulence():
    return pd.read_csv("data/turbulence_bhr001_2023.csv")


df = load_turbulence()
months_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
available_months = [m for m in months_order if m in df["month"].unique()]

month = st.select_slider("Month", options=available_months, value="Nov")

sub = df[df["month"] == month]
mean_speed = sub["wind_speed"].values
ti = sub["turbulence_intensity"].values


def turbulence_model(v, alpha, beta, c):
    return alpha * v ** beta + c


bounds = ([0, -np.inf, 0.01], [0.3, 0, 0.2])
try:
    params, _ = curve_fit(turbulence_model, mean_speed, ti, bounds=bounds, method="dogbox", maxfev=5000)
    pred = turbulence_model(mean_speed, *params)
    r2 = r2_score(ti, pred)
    fit_ok = True
except Exception:
    fit_ok = False
    r2 = 0.0

col1, col2 = st.columns([2, 1])

with col1:
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=mean_speed, y=ti, mode="markers", name="15-min observations",
        marker=dict(color=BRASS, size=5, opacity=0.35),
    ))
    if fit_ok:
        xs = np.linspace(mean_speed.min(), mean_speed.max(), 200)
        fig.add_trace(go.Scatter(
            x=xs, y=turbulence_model(xs, *params), mode="lines",
            name=f"Fitted model (R²={r2:.2f})", line=dict(color=MOSS, width=3),
        ))
    fig.update_xaxes(title="Mean wind speed (m/s)")
    fig.update_yaxes(title="Turbulence intensity", range=[0, 1.5])
    style_fig(fig, title=f"Turbine BHR-001 — {month} 2023", height=420)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.metric("Model R²", f"{r2:.2f}" if fit_ok else "fit failed")
    st.metric("Readings this month", f"{len(sub):,}")
    if fit_ok and r2 < 0.15:
        st.warning("Weak fit this month — the simple power-law model doesn't hold up well here.")
    elif fit_ok:
        st.success("The model explains a real share of this month's variance.")

st.caption(
    "**Result** — The expected physical relationship holds — turbulence intensity drops as wind "
    "speed rises — but try scrubbing through the months: the model's R² swings from ~0.39 in "
    "January to a complete fit failure in December. A single fixed turbulence model isn't safe to "
    "apply year-round at this site."
)
