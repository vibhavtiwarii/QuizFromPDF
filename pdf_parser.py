import pdfplumber
import re


def clean_text(text: str) -> str:
    """
    Clean common PDF formatting issues
    """

    if not text:
        return ""

    # remove hyphenated line breaks (e.g., "ener-\ngy")
    text = re.sub(r'-\n', '', text)

    # replace line breaks with spaces
    text = re.sub(r'\n+', ' ', text)

    # normalize whitespace
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF file.
    Returns a single cleaned string.
    """

    all_text = []

    with pdfplumber.open(pdf_path) as pdf:

        for page_number, page in enumerate(pdf.pages):

            try:
                page_text = page.extract_text()

                if page_text:
                    cleaned = clean_text(page_text)
                    all_text.append(cleaned)

            except Exception as e:
                print(f"Warning: failed to read page {page_number}: {e}")

    return " ".join(all_text)


if __name__ == "__main__":

    # change this to your test pdf
    pdf_file = "sample.pdf"

    text = extract_text_from_pdf(pdf_file)

    print("\nPreview of extracted text:\n")
    print(text[:1000])
