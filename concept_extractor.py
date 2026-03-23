import spacy

# load English NLP model
nlp = spacy.load("en_core_web_sm")


def extract_concepts(sentence: str):
    """
    Extract important concepts from a sentence using:
    - Named entities
    - Noun phrases
    """

    doc = nlp(sentence)

    concepts = set()

    # Named Entities (persons, places, organizations, etc.)
    for ent in doc.ents:
        concepts.add(ent.text.strip())

    # Noun phrases (important objects or terms)
    for chunk in doc.noun_chunks:
        concepts.add(chunk.text.strip())

    return list(concepts)


def extract_concepts_from_sentences(sentences):
    """
    Extract concepts from a list of sentences
    """

    results = []

    for sentence in sentences:
        concepts = extract_concepts(sentence)

        results.append({
            "sentence": sentence,
            "concepts": concepts
        })

    return results


if __name__ == "__main__":

    sentences = [
        "Photosynthesis converts sunlight into chemical energy.",
        "The capital of France is Paris.",
        "Albert Einstein developed the theory of relativity."
    ]

    results = extract_concepts_from_sentences(sentences)

    for r in results:
        print("\nSentence:", r["sentence"])
        print("Concepts:", r["concepts"])
