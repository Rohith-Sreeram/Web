import nltk
import spacy
import google.generativeai as genai

# Download NLTK punkt (first run only)
nltk.download("punkt")
nlp = spacy.load("en_core_web_sm")

# 🔑 Configure Gemini (replace with your API key from Google AI Studio)
genai.configure(api_key="YOUR_GEMINI_API_KEY")

def preprocess(text):
    """Split contract into sentences using spaCy."""
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    return sentences

def analyze_with_ai(text):
    """Send contract to Gemini model for analysis."""
    prompt = f"""
    You are a legal assistant for Indian SMEs. Analyze this contract:

    1. Risk Scoring (1-10)  
    2. Clause-by-clause explanation in plain business language  
    3. Identify unfavorable terms  
    4. Suggest alternative clauses (SME-friendly)  
    5. Compliance check with Indian laws  
    6. Generate summary report  

    Contract text:
    {text}
    """

    model = genai.GenerativeModel("gemini-1.5-flash")  # use "gemini-1.5-pro" for deeper analysis
    response = model.generate_content(prompt)

    return response.text
