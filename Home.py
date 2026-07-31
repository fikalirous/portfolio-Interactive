import streamlit as st

st.set_page_config(
    page_title="Gokulnath G L — Interactive Portfolio",
    page_icon="🌾",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp { max-width: 1100px; margin: 0 auto; }
    h1, h2, h3 { font-family: Georgia, 'Iowan Old Style', serif; }
    .hero { font-size: 1.1rem; line-height: 1.65; max-width: 70ch; color: #333; }
    .card {
        border: 1px solid #D8DED4; border-radius: 8px; padding: 1.1rem 1.3rem;
        background: #F8F9F6; height: 100%;
    }
    .card h4 { margin-top: 0; }
    .card p { color: #5B655D; font-size: 0.92rem; margin-bottom: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Gokulnath G L")
st.caption("Data for international development — interactive edition")

st.markdown(
    """
    <div class="hero">
    I’m a Social Data Science student at UCD with experience in data analytics, research, and social development.
    I’ve worked on projects across disability rights, public health, gender, renewable energy,
    and rural development, focusing on turning data into clear insights for better policy and community outcomes\.
    Now based in Ireland, I’m interested in research roles within think tanks and organisations working on social policy, ESG, and data
    governance. I aim to build practical, evidence-based solutions that support inclusive and ethical decision-making.
    <br><br>
    This is the interactive companion to my <a href="https://fikalirous.github.io/portfolio/" target="_blank">
    main portfolio site</a> — the same case studies, but with live charts you can filter, and a couple of
    simulations you can actually run yourself.
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.subheader("Where the work sits")

cols = st.columns(2)
cards = [
    ("🌦️ Climate & Agriculture", "Automated weather stations, LoRaWAN micro-climate networks, and a live turbulence-intensity model you can explore month by month.", "Climate_Agriculture"),
    ("⚖️ Policy & Rights", "Disability rights, CSR, and AI-adoption research — filter the charts yourself.", "Policy_Rights"),
    ("🏥 Public Health", "District-level TB surveillance, with the live public dashboard embedded.", "Public_Health"),
    ("🤝 Gender & Grassroots", "Mapping women- and trans-led organizations across Indian states.", "Gender_Grassroots"),
]
for i, (title, desc, page) in enumerate(cards):
    with cols[i % 2]:
        st.markdown(f'<div class="card"><h4>{title}</h4><p>{desc}</p></div>', unsafe_allow_html=True)
        st.write("")

st.markdown(
    '<div class="card"><h4>🔬 Research</h4><p>MSc coursework at UCD — human values &amp; internet engagement, '
    'a 33-country AI-regulation text analysis, and a live agent-based compliance simulator you can run with your own parameters.</p></div>',
    unsafe_allow_html=True,
)

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
