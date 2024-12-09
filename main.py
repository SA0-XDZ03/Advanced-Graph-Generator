from src.nlp_pipeline import process_text

if __name__ == "__main__":
    sample_text = "Dave is an American entrepreneur. He met Louis in UK. Both worked in GreenWell Foundation."
    result = process_text(sample_text)
    print("Extracted Entities:", result["entities"])
    print("Extracted Relationships:", result["relationships"])
