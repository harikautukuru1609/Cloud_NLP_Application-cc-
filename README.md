# Cloud-Based Natural Language Processing Application

## 📌 Project Overview

The **Cloud-Based Natural Language Processing (NLP) Application** is a web-based application developed using **Python, Flask, and NLTK**. It analyzes user-provided text and identifies its sentiment as **Positive, Negative, or Neutral**.

The application provides a simple web interface where users can enter text and receive an NLP-based sentiment analysis result.

## 🎯 Objectives

* To develop a simple cloud-based NLP application.
* To analyze the sentiment of text entered by the user.
* To classify text into Positive, Negative, or Neutral sentiment.
* To provide an easy-to-use web interface.
* To understand the practical implementation of Natural Language Processing.

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **NLTK**
* **VADER Sentiment Analyzer**
* **HTML**
* **CSS**
* **Git & GitHub**

## 📂 Project Structure

```text
Cloud_NLP_Application/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── .gitignore
│
└── README.md
```

## ⚙️ Features

* Simple and user-friendly interface
* Text input for sentiment analysis
* Positive sentiment detection
* Negative sentiment detection
* Neutral sentiment detection
* Displays sentiment scores
* Flask-based web application

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/harikautukuru1609/Cloud-NLP-Application.git
```

### 2. Open the Project

```bash
cd Cloud-NLP-Application
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\activate
```

### 5. Install Required Libraries

```bash
pip install flask nltk
```

### 6. Run the Application

```bash
python app.py
```

### 7. Open in Browser

Open:

```text
http://127.0.0.1:5000
```

## 🧪 Example

### Input

```text
I really enjoyed this project. It is amazing!
```

### Output

```text
Sentiment: Positive
```

Another example:

```text
I don't like this application. It is very bad.
```

Output:

```text
Sentiment: Negative
```

## 🧠 How It Works

The application follows these steps:

```text
User enters text
       ↓
Flask receives the text
       ↓
NLTK VADER analyzes the text
       ↓
Sentiment score is calculated
       ↓
Text is classified
       ↓
Positive / Negative / Neutral
       ↓
Result displayed on webpage
```

## 📊 Sentiment Analysis

The VADER sentiment analyzer generates:

* **Positive Score**
* **Negative Score**
* **Neutral Score**
* **Compound Score**

The compound score is used to determine the overall sentiment.

## 🔮 Future Enhancements

* Add text summarization.
* Add emotion detection.
* Add multiple language support.
* Add speech-to-text functionality.
* Deploy the application on a cloud platform.
* Add user authentication.
* Store analysis history in a database.
* Add graphical sentiment visualization.

## 👩‍💻 Author

**Utukuru Harika**

B.Tech – Artificial Intelligence and Data Science

Prathyusha Engineering College

### Skills

* Python
* Java
* MySQL
* Machine Learning
* Web Development
* Data Science

## 📜 License

This project is created for educational and academic purposes.
