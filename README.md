# 📚 PDF Quiz Generator

An AI-powered application that automatically generates multiple-choice quizzes from PDF documents using NLP, machine learning, and large language models.

---

## 🚀 Overview

This project allows users to upload a PDF file and instantly generate a quiz based on its content. It combines traditional NLP techniques, a trained machine learning model, and LLM-based question generation to create meaningful and context-aware multiple-choice questions.

---

## 🧠 Features

* 📄 Upload any PDF document
* 🧹 Automatic text extraction and preprocessing
* 🧠 Sentence importance ranking using a trained ML model
* ❓ AI-generated multiple-choice questions (MCQs)
* 🎯 Automatic quiz generation with multiple questions
* 📝 Interactive quiz interface using Streamlit
* 📊 Score calculation based on user responses

---

## 🏗️ Architecture

The system follows a pipeline-based architecture:

1. **PDF Parsing**

   * Extracts raw text from uploaded PDF files

2. **Text Preprocessing**

   * Cleans text and splits into meaningful sentences
   * Filters out noisy or irrelevant sentences

3. **Sentence Ranking (ML Model)**

   * Uses TF-IDF + Logistic Regression
   * Identifies important sentences suitable for question generation

4. **Question Generation (LLM)**

   * Uses Groq API (LLaMA model)
   * Converts sentences into MCQs with 4 options

5. **Quiz Interface**

   * Displays questions using Streamlit
   * Collects answers and calculates score

---

## 🛠️ Tech Stack

* **Frontend & App Framework:** Streamlit
* **NLP:** spaCy, NLTK, WordNet
* **Machine Learning:** scikit-learn (TF-IDF + Logistic Regression)
* **LLM Integration:** Groq API (LLaMA 3)
* **PDF Processing:** pdfplumber
* **Data Handling:** pandas

---

## 📂 Project Structure

```
.
├── app.py                     # Streamlit application
├── pdf_parser.py              # Extract text from PDFs
├── preprocess.py              # Text cleaning and sentence filtering
├── sentence_ranker.py         # ML model for ranking sentences
├── train_model.py             # Model training script
├── question_generator.py      # LLM-based MCQ generation
├── distractor_generator.py    # WordNet + spaCy distractors
├── concept_extractor.py       # Extract key concepts
├── quiz_builder.py            # Build structured quiz
├── generate_training_dataset.py # Dataset creation
├── data/
│   ├── source_texts/          # Input data for training
│   └── training_data.csv      # Generated dataset
├── models/
│   ├── sentence_model.pkl
│   └── vectorizer.pkl
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone <your-repo-link>
cd pdf-quiz-generator
```

### 2. Create environment (recommended)

```
conda create -n quizgen python=3.10
conda activate quizgen
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Download NLP models

```
python -m spacy download en_core_web_sm
```

---

## 🔑 Environment Setup

Create a `.env` file and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

---

## 🧪 Training the Model

Before running the app, train the sentence ranking model:

```
python train_model.py
```

This will:

* Train the classifier
* Save model files in the `models/` directory

---

## ▶️ Running the App

```
streamlit run app.py
```

Then:

1. Upload a PDF
2. Click **Generate Quiz**
3. Answer questions
4. View your score

---

## 📊 Example Workflow

1. Upload a PDF (e.g., science notes)
2. System extracts and preprocesses text
3. Important sentences are selected
4. AI generates MCQs
5. User attempts quiz and gets score

---

## 🧠 Key Concepts Used

* TF-IDF Vectorization
* Logistic Regression Classification
* Named Entity Recognition (NER)
* Semantic similarity (spaCy)
* WordNet-based distractor generation
* Prompt engineering for LLMs

---

## ⚠️ Limitations

* MCQ quality depends on input text quality
* LLM-generated questions may vary in accuracy
* Requires trained model before use
* Processing large PDFs may take time

---

## 🔮 Future Improvements

* Better distractor generation using LLMs
* Improved UI/UX beyond Streamlit
* Support for more file formats
* Real-time quiz analytics
* Deployment as a web application

---

## 👨‍💻 Author

Built as an AI/NLP project to explore automated question generation from unstructured documents.

---

## ⭐ Acknowledgements

* spaCy
* NLTK
* scikit-learn
* Groq API
* Streamlit
