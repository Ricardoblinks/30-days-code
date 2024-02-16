from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Perform sentiment analysis
    sentiment = blob.sentiment
    
    # Interpret sentiment polarity
    if sentiment.polarity > 0:
        return "Positive"
    elif sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Example usage
text = "I don't like this product! It's not amazing."
sentiment = analyze_sentiment(text)
print("Sentiment Analysis Result:", sentiment)
