from src.utils.text_cleaner import clean_text
from src.entity_extraction.ner_model import extract_entities
from src.entity_extraction.relation_extraction import extract_relationships

def process_text(text: str):
    """
    Full pipeline: Cleans text, extracts entities, and identifies relationships.
    """
    cleaned_text = clean_text(text)
    entities = extract_entities(cleaned_text)
    relationships = extract_relationships(cleaned_text, entities)
    return {"entities": entities, "relationships": relationships}
