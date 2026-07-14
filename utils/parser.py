import io
import re


def extract_text(uploaded_file) -> str:
    """Extract plain text from a PDF or DOCX uploaded via Streamlit."""
    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):
        return _extract_pdf(uploaded_file)
    elif filename.endswith(".docx"):
        return _extract_docx(uploaded_file)
    else:
        return ""


import logging

logger = logging.getLogger(__name__)

def _extract_pdf(uploaded_file) -> str:
    try:
        import fitz  # PyMuPDF
        data = uploaded_file.read()
        doc  = fitz.open(stream=data, filetype="pdf")
        text = "\n".join(page.get_text() for page in doc)
        return _clean(text)
    except Exception as e:
        logger.warning("PDF extraction failed", exc_info=e)
        return ""


def _extract_docx(uploaded_file) -> str:
    try:
        from docx import Document
        doc  = Document(io.BytesIO(uploaded_file.read()))
        text = "\n".join(p.text for p in doc.paragraphs)
        return _clean(text)
    except Exception as e:
        logger.warning("DOCX extraction failed", exc_info=e)
        return ""


def _clean(text: str) -> str:
    """Remove excessive whitespace while keeping structure."""
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()
