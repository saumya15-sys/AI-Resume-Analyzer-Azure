import streamlit as st

from utils.document_parser import extract_resume_text
from utils.resume_analyzer import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer"
)

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume Uploaded Successfully")

    if st.button("Analyze Resume"):

        with st.spinner("Extracting Text..."):

            resume_text = extract_resume_text(
                "temp_resume.pdf"
            )

        with st.spinner("Analyzing Resume..."):

            analysis = analyze_resume(
                resume_text
            )

        st.subheader("AI Analysis")

        st.markdown(analysis)