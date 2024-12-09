def extract_relationships(text: str, entities: list):
    """
    Extracts simple relationships based on predefined patterns.
    """
    relationships = []
    # Example: Extract 'met with', 'works at', etc.
    if "met" in text:
        relationships.append({"subject": entities[0], "object": entities[1], "relation": "met with"})
    if "works at" in text:
        relationships.append({"subject": entities[0], "object": entities[1], "relation": "works at"})
    return relationships
