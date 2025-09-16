import streamlit as st
from processor import preprocess, analyze_with_ai

st.set_page_config(page_title="Legal Text Analyzer", layout="wide")
st.title("Legal Text Analysis Tool (Local with Transformers)")

st.markdown("""
This tool analyzes legal text locally using Hugging Face Transformers.  
- **Preprocessing**: Lowercase and clean text.  
- **Entity Recognition**: Detect names, organizations, dates, etc.
""")

input_text = st.text_area("Enter or paste legal text here:", height=200)

if st.button("Analyze"):
    if not input_text.strip():
        st.warning("Please enter some text before analyzing.")
    else:
        # Preprocessing
        cleaned_text = preprocess(input_text)
        st.subheader("Preprocessed Text")
        st.write(cleaned_text)

        # Entity Recognition
        entities = analyze_with_ai(input_text)
        st.subheader("Detected Entities")
        st.write(entities)
