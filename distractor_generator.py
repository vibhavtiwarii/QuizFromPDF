import random
from nltk.corpus import wordnet
import spacy

nlp = spacy.load("en_core_web_sm")


def get_wordnet_distractors(answer):
    """
    Generate distractors using WordNet
    """

    distractors = set()

    synsets = wordnet.synsets(answer)

    for syn in synsets:

        # hypernyms → more general terms
        for hyper in syn.hypernyms():

            for lemma in hyper.lemmas():
                word = lemma.name().replace("_", " ")

                if word.lower() != answer.lower():
                    distractors.add(word)

        # hyponyms → related specific terms
        for hypo in syn.hyponyms():

            for lemma in hypo.lemmas():
                word = lemma.name().replace("_", " ")

                if word.lower() != answer.lower():
                    distractors.add(word)

    return list(distractors)


def get_spacy_similar_words(answer, candidates):
    """
    Rank candidate distractors using semantic similarity
    """

    answer_doc = nlp(answer)

    scored = []

    for c in candidates:

        try:
            similarity = answer_doc.similarity(nlp(c))
            scored.append((c, similarity))
        except:
            continue

    scored.sort(key=lambda x: x[1], reverse=True)

    return [w[0] for w in scored]


def generate_distractors(answer, num_distractors=3):
    """
    Main distractor generation function
    """

    candidates = get_wordnet_distractors(answer)

    if not candidates:
        return []

    ranked = get_spacy_similar_words(answer, candidates)

    distractors = []

    for word in ranked:

        if word.lower() != answer.lower():
            distractors.append(word)

        if len(distractors) == num_distractors:
            break

    return distractors


if __name__ == "__main__":

    answer = "Paris"

    distractors = generate_distractors(answer)

    print("Answer:", answer)
    print("Distractors:", distractors)
