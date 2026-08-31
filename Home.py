import streamlit as st

st.set_page_config(
    page_title="Gokulnath G L — Interactive Portfolio",
    page_icon="🌾",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp { max-width: 2000px; margin: 0 auto; }
    h1, h2, h3 { font-family: Georgia, 'Iowan Old Style', serif; }
    .hero { font-size: 1.1rem; line-height: 1.65; max-width: 100ch; color: #333; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Gokulnath G L")
st.subheader("Data Science for Social Good")

st.markdown(
    """
    <div class="hero">
    I’m a Social Data Science student at University College Dublin with experience in data analytics, research, and social development.
    I’ve worked on projects across disability rights, public health, gender, renewable energy,
    and rural development, focusing on turning data into clear insights for better policy and community outcomes.
    Now based in Ireland, I’m interested in research roles within think tanks and organisations working on social policy, ESG, and data
    governance. I aim to build practical, evidence-based solutions that support inclusive and ethical decision-making.
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.subheader("Works")

cards = [
    ("⚖️ Policy & Rights", "Disability rights, CSR, and AI-adoption research", "pages/2_Policy_Rights.py"),
    ("🔬 Research", "human values & internet engagement, AI-regulation text analysis, and a live agent-based compliance simulator.", "pages/5_Research.py"),
    ("🏥 Public Health", "District-level TB surveillance, with the live public dashboard embedded.", "pages/3_Public_Health.py"),
    ("🤝 Gender & Grassroots", "Mapping women- and trans-led organizations across Indian states.", "pages/4_Gender_Grassroots.py"),
    ("🌦️ Climate & Agriculture", "Automated weather stations, LoRaWAN micro-climate networks, and a live turbulence-intensity model you can explore month by month.", "pages/1_Climate_Agriculture.py"),
    ("📊 Personal Projects", "Self-directed projects that I have worked on", "pages/6_Personal_Projects.py"),
]
cols = st.columns(2)
for i, (title, desc, page) in enumerate(cards):
    with cols[i % 2]:
        with st.container(border=True):
            st.markdown(f"#### {title}")
            st.caption(desc)
            st.page_link(page, label="Open")

st.write("")
st.divider()

col1, col2, col3, col4 = st.columns(4)
with col1:
    with open("assets/Gokul_UCD_CV.pdf", "rb") as f:
        st.download_button("📄 CV", f, file_name="Gokul_UCD_CV.pdf", mime="application/pdf")
with col2:
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/gokulnath-g-l-13071a178/")
with col3:
    st.link_button("💻 GitHub", "https://github.com/fikalirous")
with col4:
    st.link_button("🌐 Static site", "https://fikalirous.github.io/portfolio/")

st.caption("work00gokul@gmail.com")
