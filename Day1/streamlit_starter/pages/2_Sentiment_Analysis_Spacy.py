import streamlit as st
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Load the spaCy model and add the TextBlob sentiment analysis pipeline
nlp = spacy.load("en_core_web_sm")
spacy_text_blob = SpacyTextBlob()
nlp.add_pipe(spacy_text_blob)

# Title and instructions for the app
st.title("Sentiment Analysis App")
st.write("Enter some text, and the app will analyze whether the sentiment is Positive, Negative, or Neutral.")

# Text input from the user
user_input = st.text_area("Enter your text here:")

# Analyze sentiment if user input is provided
if user_input:
    # Process the text through spaCy NLP pipeline
    doc = nlp(user_input)
    
    # Get the sentiment polarity
    sentiment_polarity = doc._.blob.polarity
    
    # Determine the sentiment (positive, negative, or neutral)
    if sentiment_polarity > 0:
        sentiment_label = "Positive"
    elif sentiment_polarity < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    # Display the sentiment and the polarity score
    st.write(f"**Sentiment**: {sentiment_label}")
    st.write(f"**Polarity Score**: {sentiment_polarity}")
