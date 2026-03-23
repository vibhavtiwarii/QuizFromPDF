import re
import nltk

# make sure punkt tokenizer exists
nltk.download("punkt", quiet=True)


def clean_text(text: str) -> str:
    """
    Clean general text noise from PDF output
    """

    # remove references like [1], [2]
    text = re.sub(r"\[[0-9]+\]", "", text)

    # remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def sentence_tokenize(text: str):
    """
    Split text into sentences using NLTK
    """

    sentences = nltk.sent_tokenize(text)

    return sentences


def filter_sentences(sentences):
    """
    Remove sentences that are not useful for question generation
    """

    filtered = []

    for s in sentences:

        s = s.strip()

        # remove very short sentences
        if len(s) < 25:
            continue

        # remove sentences with too many numbers
        if sum(c.isdigit() for c in s) > 5:
            continue

        filtered.append(s)

    return filtered


def preprocess_text(text: str):
    """
    Full preprocessing pipeline
    """

    text = clean_text(text)

    sentences = sentence_tokenize(text)

    sentences = filter_sentences(sentences)

    return sentences


if __name__ == "__main__":

    sample_text = """
    Photosynthesis is the process by which plants convert sunlight into chemical energy.
    Chlorophyll absorbs light energy from the sun.
    Plants grow in many environments.
    """

    sentences = preprocess_text(sample_text)

    print("\nProcessed Sentences:\n")

    for s in sentences:
        print("-", s)
