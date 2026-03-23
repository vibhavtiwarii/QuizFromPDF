import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


class SentenceRanker:

    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=5000
        )
        self.model = LogisticRegression()

    def train(self, sentences, labels):
        """
        Train the importance classifier
        """

        X = self.vectorizer.fit_transform(sentences)

        self.model.fit(X, labels)

    def predict_scores(self, sentences):
        """
        Return importance scores for sentences
        """

        X = self.vectorizer.transform(sentences)

        scores = self.model.predict_proba(X)[:, 1]

        return scores

    def rank_sentences(self, sentences, top_k=10):
        """
        Return the most important sentences
        """

        scores = self.predict_scores(sentences)

        ranked = list(zip(sentences, scores))

        ranked.sort(key=lambda x: x[1], reverse=True)

        return ranked[:top_k]

    def save(self, model_path="models/sentence_model.pkl",
             vectorizer_path="models/vectorizer.pkl"):

        with open(model_path, "wb") as f:
            pickle.dump(self.model, f)

        with open(vectorizer_path, "wb") as f:
            pickle.dump(self.vectorizer, f)

    def load(self, model_path="models/sentence_model.pkl",
             vectorizer_path="models/vectorizer.pkl"):

        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

        with open(vectorizer_path, "rb") as f:
            self.vectorizer = pickle.load(f)


if __name__ == "__main__":

    sentences = [
        "Photosynthesis converts sunlight into chemical energy.",
        "Plants grow in many environments.",
        "The capital of France is Paris.",
        "Water freezes at zero degrees Celsius."
    ]

    labels = [
        1,  # important
        0,  # not important
        1,
        1
    ]

    ranker = SentenceRanker()

    ranker.train(sentences, labels)

    ranked = ranker.rank_sentences(sentences)

    print("\nTop ranked sentences:\n")

    for sentence, score in ranked:
        print(f"{score:.3f} → {sentence}")
