import streamlit as st

from pdf_parser import extract_text_from_pdf
from preprocess import preprocess_text
from sentence_ranker import SentenceRanker
from question_generator import generate_mcq
from quiz_builder import build_quiz


st.title("📚 PDF Quiz Generator")

st.write("Upload a PDF and generate multiple choice questions.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])


def generate_quiz_from_pdf(pdf_path):

    # extract text
    text = extract_text_from_pdf(pdf_path)

    # preprocess
    sentences = preprocess_text(text)

    # load sentence ranking model
    ranker = SentenceRanker()
    ranker.load()

    # select important sentences
    ranked = ranker.rank_sentences(sentences, top_k=5)

    important_sentences = [s for s, score in ranked]

    questions = []

    for sentence in important_sentences:

        mcq_text = generate_mcq(sentence)

        questions.append(mcq_text)

    return questions


if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    if st.button("Generate Quiz"):

        with st.spinner("Generating questions..."):

            quiz_questions = generate_quiz_from_pdf("temp.pdf")

        st.session_state.quiz = quiz_questions
        st.session_state.answers = {}


if "quiz" in st.session_state:

    st.header("Quiz")

    for i, q in enumerate(st.session_state.quiz):

        st.markdown(f"**Question {i+1}**")

        st.text(q)

        answer = st.radio(
            f"Select answer for Q{i+1}",
            ["A", "B", "C", "D"],
            key=f"q{i}"
        )

        st.session_state.answers[i] = answer


    if st.button("Submit Quiz"):

        score = 0

        for i, q in enumerate(st.session_state.quiz):

            # extract correct answer from generated text
            if "Answer:" in q:
                correct = q.split("Answer:")[-1].strip()

                if st.session_state.answers[i] == correct:
                    score += 1

        st.success(f"Your score: {score} / {len(st.session_state.quiz)}")
