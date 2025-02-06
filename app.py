import streamlit as st
from transformers import pipeline
import textwrap

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment",
    tokenizer="cardiffnlp/twitter-roberta-base-sentiment"
)

label_mapping = {
    "LABEL_0": "Negative",
    "LABEL_1": "Neutral",
    "LABEL_2": "Positive"
}

emoji_mapping = {
    "Negative": "😟",
    "Neutral": "😐",
    "Positive": "😀"
}

# Function to split text into chunks and analyze sentiment
def analyze_text_in_chunks(text, chunk_size=500):
    chunks = textwrap.wrap(text, width=chunk_size)
    sentiments = []
    confidence_scores = {"Positive": [], "Neutral": [], "Negative": []}

    for chunk in chunks:
        result = sentiment_pipeline(chunk)
        sentiment_label = label_mapping.get(result[0]['label'], result[0]['label'])
        sentiment_score = result[0]['score']
        sentiments.append(sentiment_label)
        confidence_scores[sentiment_label].append(sentiment_score)

    final_sentiment = max(set(sentiments), key=sentiments.count)
    avg_confidence = (
        sum(confidence_scores[final_sentiment]) / len(confidence_scores[final_sentiment])
    )

    return final_sentiment, avg_confidence

st.markdown("<h1 style='text-align:center; color:black;'>Sentiment Spotlight</h1>", unsafe_allow_html=True)

input_text = st.text_area("Enter some text to analyze its sentiment:", "")

if st.button('Submit'):
    if input_text.strip():
        # Analyze sentiment in chunks
        final_sentiment, avg_confidence = analyze_text_in_chunks(input_text)
        
        label_color = "red" if final_sentiment == "Negative" else "green" if final_sentiment == "Positive" else "orange"

        st.markdown("""
            <style>
                .sentiment-box {
                    font-size: 24px;
                    font-weight: bold;
                    padding: 10px;
                    text-align: center;
                    display: inline-block;
                    width: 300px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                }
            </style>
        """, unsafe_allow_html=True)

        # Display sentiment result
        st.markdown(f"""
        <div class='sentiment-box' style='color: black;'>
            Sentiment: <span style='color:{label_color};'>{final_sentiment}</span> {emoji_mapping[final_sentiment]}
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
        <div style='margin: 10px 0; font-size:18px; font-weight: bold;'>
            Confidence: <span style='font-weight: bold;'>({avg_confidence:.2%})</span>
        </div>
        """, unsafe_allow_html=True)
        st.progress(avg_confidence)

    else:
        st.error("Please enter some text to analyze.")

