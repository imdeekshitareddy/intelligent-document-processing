from utils.pdf_reader import extract_text_from_pdf
from model.entity_extractor import extract_entities

text = extract_text_from_pdf("sample_pdfs/test.pdf")

entities = extract_entities(text)

print(entities)