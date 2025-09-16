import json
import os
from datetime import datetime
from PyPDF2 import PdfReader
import docx

AUDIT_FILE = "audit_trail.json"

def read_file(file):
    """Read PDF, DOCX, or TXT file and return extracted text."""
    if file.type == "application/pdf":
        pdf = PdfReader(file)
        text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        text = " ".join([p.text for p in doc.paragraphs])
    else:
        text = file.read().decode("utf-8")
    return text

def save_audit(user_action, metadata=None):
    """Save user actions to audit trail JSON file."""
    entry = {
        "timestamp": str(datetime.now()),
        "action": user_action,
        "metadata": metadata or {}
    }
    if not os.path.exists(AUDIT_FILE):
        with open(AUDIT_FILE, "w") as f:
            json.dump([], f)

    with open(AUDIT_FILE, "r+") as f:
        data = json.load(f)
        data.append(entry)
        f.seek(0)
        json.dump(data, f, indent=2)
