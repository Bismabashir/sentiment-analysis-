# Sentiment Spotlight

A real-time sentiment analysis web app built with Streamlit and Hugging Face Transformers. Classifies text as Positive, Neutral, or Negative using the `cardiffnlp/twitter-roberta-base-sentiment` model with chunk-based processing for long inputs.

## Demo

> Enter any text and get instant sentiment classification with confidence scores.

## Features

- Real-time sentiment classification (Positive / Neutral / Negative)
- Chunk-based processing for long text inputs
- Confidence score displayed for each prediction
- Clean and minimal Streamlit interface

## Tech Stack

- **Model** — cardiffnlp/twitter-roberta-base-sentiment (HuggingFace)
- **Framework** — Streamlit
- **Libraries** — Transformers, PyTorch
- **Language** — Python

## Installation

```bash
git clone https://github.com/Bismabashir/sentiment-analysis-.git
cd sentiment-analysis-
pip install -r requirements.txt
streamlit run app.py
```

## How It Works

1. Input text is split into 500-character chunks
2. Each chunk is analyzed by the RoBERTa model
3. Confidence scores are averaged across all chunks
4. Final sentiment and confidence score are displayed
