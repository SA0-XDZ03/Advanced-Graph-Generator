import re

def clean_text(text: str) -> str:
    """
    Cleans input text by removing special characters, extra spaces, and making it lowercase.
    """
    text = text.strip().lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text)  # Remove multiple spaces
    return text
