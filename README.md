# Intelligent Document Processing System 📄🤖

## Overview

This project is an **AI-powered Intelligent Document Processing system** that automatically extracts important information from PDF documents using Natural Language Processing (NLP).

The system allows users to upload a document and automatically identifies:

* 👤 Names
* 📅 Dates
* 💰 Money Amounts
* 🏢 Organizations

The extracted information is displayed in a structured format.

---

## Features 🚀

* Upload PDF documents
* Automatic text extraction
* Named Entity Recognition (NLP)
* Structured JSON output
* Simple web interface
* Fast and lightweight system

---

## Project Structure 📁

```
intelligent-document-processing/
│
├── app.py                # Main Flask application
├── requirements.txt      # Required libraries
├── README.md             # Project documentation
│
├── model/                # NLP processing modules
│
├── utils/                # Helper functions (PDF extraction)
│
├── templates/            # HTML frontend
│
├── static/               # CSS / Images
│
└── sample_pdfs/          # Sample test documents
```

---

## How It Works ⚙️

1. User uploads a PDF document
2. The system extracts text from the PDF
3. NLP model analyzes the text
4. Important entities are extracted
5. Results are displayed on the webpage

### System Flow

```
PDF Upload
   ↓
Text Extraction
   ↓
NLP Processing
   ↓
Entity Extraction
   ↓
Results Display
```

---

## Technologies Used 🧠

* Python
* Flask
* Natural Language Processing (NLP)
* spaCy
* PDF Processing Libraries

---

## Installation 🔧

Clone the repository:

```
git clone https://github.com/imdeekshita/intelligent-document-processing.git
```

Go to project directory:

```
cd intelligent-document-processing
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python app.py
```

Open browser:

```
http://localhost:5000
```

---

## Example Input 📥

Sample Contract Text:

```
This agreement is made on 12 January 2025 between ABC Pvt Ltd and John Smith.
The total payment amount is $5000.
```

---

## Example Output 📤

```
Names:
ABC Pvt Ltd
John Smith

Dates:
12 January 2025

Amounts:
$5000
```

---

## Future Improvements ⭐

* OCR for scanned PDFs
* Deep Learning NER models
* Docker deployment
* Better UI
* Support for multiple document formats

---

## Author 👩‍💻

**B.Tech Computer Science Student**

Machine Learning Project

---
