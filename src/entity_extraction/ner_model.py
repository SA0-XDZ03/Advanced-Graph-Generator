import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_entities(text: str):
    """
    Extracts named entities from the text using spaCy.
    """
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append({"entity": ent.text, "type": ent.label_})
    return entities
