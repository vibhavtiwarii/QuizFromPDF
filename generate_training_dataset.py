import os
import re
import pandas as pd
import nltk
import spacy
from pdf_parser import extract_text_from_pdf
from preprocess import preprocess_text

nltk.download("punkt")

nlp = spacy.load("en_core_web_sm")


DATA_SOURCE_FOLDER = "data/source_texts"
OUTPUT_FILE = "data/training_data.csv"


def label_sentence(sentence):
    """
    Label sentences based on linguistic signals.
    1 = factual/definition (good for questions)
    0 = narrative/general
    """

    doc = nlp(sentence)

    sentence_lower = sentence.lower()

    # Definition patterns
    definition_patterns = [
        "is the process",
        "is defined as",
        "refers to",
        "is known as",
        "is called",
        "is a type of",
        "is an example of"
    ]

    for pattern in definition_patterns:
        if pattern in sentence_lower:
            return 1

    # Sentences with named entities (facts)
    if len(doc.ents) > 0:
        return 1

    # Sentences containing numbers (dates, measurements)
    if re.search(r"\d", sentence):
        return 1

    # Scientific noun-heavy sentences
    noun_count = sum(1 for token in doc if token.pos_ == "NOUN")
    if noun_count >= 3:
        return 1

    # Otherwise treat as non-question sentence
    return 0


def collect_sentences():
    """
    Collect sentences from text or pdf files
    """

    sentences = []

    for file in os.listdir(DATA_SOURCE_FOLDER):

        path = os.path.join(DATA_SOURCE_FOLDER, file)

        if file.endswith(".pdf"):

            text = extract_text_from_pdf(path)
            sents = preprocess_text(text)

        elif file.endswith(".txt"):

            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            sents = preprocess_text(text)

        else:
            continue

        sentences.extend(sents)

    return sentences


def generate_dataset():

    sentences = collect_sentences()

    print("Total sentences collected:", len(sentences))

    data = []

    for s in sentences:

        label = label_sentence(s)

        data.append({
            "sentence": s,
            "label": label
        })

    df = pd.DataFrame(data)

    # Ensure both classes exist
    counts = df["label"].value_counts()

    if len(counts) < 2:
        raise ValueError(
            "Dataset contains only one class. Add more varied text sources."
        )

    print("\nLabel distribution:")
    print(counts)

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nDataset saved to", OUTPUT_FILE)


if __name__ == "__main__":
    generate_dataset()
