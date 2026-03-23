import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sentence_ranker import SentenceRanker


def train_model():

    # load dataset
    df = pd.read_csv("data/training_data.csv")

    sentences = df["sentence"].tolist()
    labels = df["label"].tolist()

    # split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        sentences,
        labels,
        test_size=0.2,
        random_state=42
    )

    # initialize ranker
    ranker = SentenceRanker()

    print("Training model...")

    ranker.train(X_train, y_train)

    print("Training complete.")

    # evaluate
    scores = ranker.predict_scores(X_test)

    predictions = [1 if s >= 0.5 else 0 for s in scores]

    print("\nModel Evaluation\n")

    print("Accuracy:", accuracy_score(y_test, predictions))
    print(classification_report(y_test, predictions))

    # save model
    ranker.save()

    print("\nModel saved to models/")


if __name__ == "__main__":
    train_model()
