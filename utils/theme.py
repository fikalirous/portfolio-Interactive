"""Shared color palette and Plotly styling helpers, matching the static Quarto site's theme."""

MOSS = "#3F6353"
MOSS_DARK = "#2C4A3D"
BRASS = "#A9762F"
INK = "#1C2420"
MUTED = "#5B655D"
PAPER = "#F4F5F1"
RULE = "#D8DED4"
SAGE = "#7A9A87"

CATEGORICAL = [MOSS, BRASS, SAGE, "#8A5A44", "#5B7A99", "#B08968"]

REGION_COLORS = {
    "Africa": "#B0413E",
    "Americas": MOSS,
    "Asia-Pacific": BRASS,
    "Europe": "#5B7A99",
    "Europe/Asia": "#8FB8D9",
    "Middle East": "#7A5C99",
    "Global": MUTED,
}


def style_fig(fig, title=None, height=None):
    """Apply consistent typography and layout to a Plotly figure."""
    fig.update_layout(
        font=dict(family="Segoe UI, -apple-system, sans-serif", color=INK, size=13),
        title=dict(text=title, font=dict(size=16, family="Georgia, serif")) if title else None,
        plot_bgcolor="white",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=50 if title else 20, b=10),
        height=height,
        legend=dict(bgcolor="rgba(0,0,0,0)"),
    )
    fig.update_xaxes(gridcolor=RULE, zerolinecolor=RULE)
    fig.update_yaxes(gridcolor=RULE, zerolinecolor=RULE)
    return fig
