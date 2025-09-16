import streamlit as st
from utils import read_file, save_audit
from processor import preprocess, analyze_with_ai

st.set_page_config(page_title="GenAI Legal Assistant", layout="wide")

st.title("📑 GenAI-Powered Legal Assistant for SMEs")

# Upload Section
uploaded_file = st.file_uploader("Upload a contract (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
manual_text = st.text_area("Or paste contract text here:")

if uploaded_file or manual_text.strip():
    if uploaded_file:
        save_audit("File Uploaded", {"filename": uploaded_file.name})
        with st.spinner("Reading contract..."):
            text = read_file(uploaded_file)
    else:
        text = manual_text
        save_audit("Manual Text Input", {"length": len(manual_text)})

    st.subheader("Contract Preview")
    st.text_area("Extracted Text", text[:2000] + "...", height=200)

    if st.button("Analyze Contract"):
        save_audit("Contract Analysis Started", {"source": "file" if uploaded_file else "manual"})
        
        with st.spinner("Analyzing with Gemini... (may take up to 2 minutes)"):
            summary = analyze_with_ai(text)

        st.subheader("📊 Analysis Report")
        st.write(summary)

        save_audit("Contract Analysis Completed", {"source": "file" if uploaded_file else "manual"})

         
