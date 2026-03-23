import random
import json


def build_question(question_text, correct_answer, distractors):
    """
    Build a structured MCQ question
    """

    # combine correct answer with distractors
    options = distractors + [correct_answer]

    # shuffle options
    random.shuffle(options)

    # determine correct option letter
    option_letters = ["A", "B", "C", "D"]

    option_map = {}

    correct_letter = None

    for i, option in enumerate(options):
        option_map[option_letters[i]] = option

        if option == correct_answer:
            correct_letter = option_letters[i]

    question_object = {
        "question": question_text,
        "options": option_map,
        "answer": correct_letter,
        "correct_text": correct_answer
    }

    return question_object


def build_quiz(question_data):
    """
    Build full quiz from list of question dictionaries
    """

    quiz = []

    for q in question_data:

        question_obj = build_question(
            q["question"],
            q["answer"],
            q["distractors"]
        )

        quiz.append(question_obj)

    return quiz


def save_quiz_to_json(quiz, filepath="quiz.json"):
    """
    Save quiz to JSON file
    """

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(quiz, f, indent=4)


if __name__ == "__main__":

    sample_questions = [
        {
            "question": "What is the capital of France?",
            "answer": "Paris",
            "distractors": ["London", "Berlin", "Rome"]
        },
        {
            "question": "Which process converts sunlight into chemical energy?",
            "answer": "Photosynthesis",
            "distractors": ["Respiration", "Fermentation", "Metabolism"]
        }
    ]

    quiz = build_quiz(sample_questions)

    for q in quiz:

        print("\nQuestion:", q["question"])

        for key, value in q["options"].items():
            print(f"{key}) {value}")

        print("Correct Answer:", q["answer"])

    save_quiz_to_json(quiz)
