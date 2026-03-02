from utils.pdf_reader import extract_text_from_pdf

text = extract_text_from_pdf("sample_pdfs/test.pdf")

print(text)