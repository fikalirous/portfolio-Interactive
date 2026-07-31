import streamlit as st

st.set_page_config(page_title="About", page_icon="👋", layout="wide")
st.title("👋 About")

st.markdown(
    """
## Profile

Passionate data professional with experience applying data-driven approaches in the social
development sector across India. With a background in engineering and hands-on expertise in
research, data management, and visualization, I've worked on projects spanning disability rights,
gender equity, public health, renewable energy, and rural development.

## Experience

**Data Analyst, Pacta** — Sep 2024 to Jul 2025
Quantitative research in disability, law, and CSR domains using web scraping, data cleaning, EDA,
and NLP.

**Data Specialist, Gram Vikas** — Dec 2020 to Jan 2024
Developed automated reporting systems, dashboards, and survey frameworks for water conservation
initiatives. Led installation of automated weather stations across 7 blocks in 6 districts of
Odisha.

**Rural Development Fellow, SBI Youth For India** — Oct 2019 to Oct 2020
Led weather station installation and monitoring in Odisha, engaging 600+ farmers.

### Consulting & short-term engagements

- **Data Consultant, South Asia Women's Fund India** (Oct–Dec 2024)
- **Data Consultant, National Institute for Research in Tuberculosis** (May–Jul 2024)
- **Data Consultant, Mindsprint** (Feb–May 2024)

## Education

- **MSc Social Data Science**, University College Dublin — 2026 (in progress)
- **Certificate of Higher Education, Data Analysis**, Scaler Academy — 2023
- **BE, Electrical and Electronics Engineering**, Amrita University — 2018

## Skills

**Data & Analysis:** Python (data extraction & APIs, web scraping, EDA, NLP, geospatial analysis),
R, SQL, survey design, dashboard development, impact assessment

**Tools:** Tableau, Looker Studio, Metabase, Streamlit, Google Apps Script, Google Workspace,
Microsoft Office

**Project Management:** Monitoring & evaluation, stakeholder coordination, training & capacity
building, report writing
"""
)

with open("assets/Gokul_UCD_CV.pdf", "rb") as f:
    st.download_button("📄 Download CV", f, file_name="Gokul_UCD_CV.pdf", mime="application/pdf")

st.link_button("LinkedIn", "https://www.linkedin.com/in/gokulnath-g-l-13071a178/")
