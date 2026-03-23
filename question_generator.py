import os
from groq import Groq
from dotenv import load_dotenv

# load API key from .env
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_mcq(sentence):
    """
    Generate a multiple choice question from a sentence
    """

    prompt = f"""
You are an expert teacher.

Generate a high-quality multiple choice question based on the sentence below.

Sentence:
{sentence}

Rules:
- The question must test understanding of the key concept.
- Provide exactly 4 options.
- Only one option must be correct.
- Distractors must be plausible but incorrect.
- Avoid repeating the sentence exactly.

Return the result in the following format:

Question: <question>

A) <option>
B) <option>
C) <option>
D) <option>

Answer: <correct letter>
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return response.choices[0].message.content


def generate_mcqs(sentences, num_questions=5):
    """
    Generate MCQs from top ranked sentences
    """

    questions = []

    for sentence in sentences[:num_questions]:

        mcq = generate_mcq(sentence)

        questions.append(mcq)

    return questions


if __name__ == "__main__":

    test_sentences = [
        "Photosynthesis converts sunlight into chemical energy.",
        "The capital of France is Paris.",
        "Water freezes at zero degrees Celsius."
    ]

    mcqs = generate_mcqs(test_sentences)

    for q in mcqs:
        print("\n------------------------\n")
        print(q)
