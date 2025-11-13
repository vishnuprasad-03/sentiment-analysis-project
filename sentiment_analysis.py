from textblob import TextBlob

# Sample sentences to analyze
sentences = [
    "I love coding and learning new things!",
    "This weather is terrible today.",
    "I feel okay, not too bad, not too good."
]

print("Sentiment Analysis Results:\n")
for text in sentences:
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # -1 = negative, +1 = positive
    if sentiment > 0:
        mood = "Positive 😊"
    elif sentiment < 0:
        mood = "Negative 😞"
    else:
        mood = "Neutral 😐"
    print(f"Text: {text}")
    print(f"Sentiment Score: {sentiment:.2f} → {mood}\n")
