from transformers import pipeline

try:
    ner_pipeline = pipeline("ner", grouped_entities=True, model="dslim/bert-base-NER")
except Exception as e:
    print("⚠️ Model failed to load:", e)
    ner_pipeline = None

def preprocess(text: str) -> str:
    return " ".join(text.lower().split())

def analyze_with_ai(text: str) -> str:
    if ner_pipeline is None:
        return "Model not available. Please check installation."
    results = ner_pipeline(text)
    if not results:
        return "No named entities detected."
    return "\n".join([f"{ent['word']} → {ent['entity_group']}" for ent in results])
