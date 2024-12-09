from src.nlp_pipeline import process_text

def test_nlp_pipeline():
    text = "Dave is an American entrepreneur. He met Louis in UK."
    result = process_text(text)
    assert len(result["entities"]) > 0
    assert len(result["relationships"]) > 0
