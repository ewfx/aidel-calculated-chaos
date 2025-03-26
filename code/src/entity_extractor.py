from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

model_name = "xlm-roberta-large-finetuned-conll03-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

def extract_entities(transaction: str):
    """
    Extract entities from the transaction text.
    This is a placeholder function. Replace with actual entity extraction logic.
    """
    entities = ner_pipeline(transaction)
    filtered_entities = [e for e in entities if e['entity_group'] in ["PER", "ORG"]]
    for entity in filtered_entities:
      print(f"Entity: {entity['word']}, Type: {entity['entity_group']}, Score: {entity['score']:.2f}")
    print(filtered_entities)
    return filtered_entities