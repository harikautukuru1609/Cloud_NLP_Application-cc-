from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download VADER data
nltk.download("vader_lexicon")

# Create Flask application
app = Flask(__name__)

# Create sentiment analyzer
sia = SentimentIntensityAnalyzer()


@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = ""
    score = ""
    text = ""

    if request.method == "POST":
        text = request.form["text"]

        result = sia.polarity_scores(text)
        compound = result["compound"]

        if compound >= 0.05:
            sentiment = "Positive 😊"
        elif compound <= -0.05:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

        score = compound

    return render_template(
        "index.html",
        sentiment=sentiment,
        score=score,
        text=text
    )


# Run the application on port 5001
if __name__ == "__main__":
    app.run(debug=True, port=5001)