"""URL-synced section switcher — a drop-in replacement for st.tabs() that supports
deep links (e.g. ?section=AI+Adoption) and opens on the right section by default,
which plain st.tabs() cannot do (it has no `index`/default-tab parameter and never
reflects the current tab in the URL)."""

import streamlit as st


def section_selector(sections, param="section", key_prefix="nav"):
    current = st.query_params.get(param, sections[0])
    if current not in sections:
        current = sections[0]
    idx = sections.index(current)

    choice = st.radio(
        "Section", sections, index=idx, horizontal=True,
        label_visibility="collapsed", key=f"{key_prefix}_{param}",
    )

    if st.query_params.get(param) != choice:
        st.query_params[param] = choice

    return choice
