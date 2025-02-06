# **Sentiment Spotlight**

This project uses **Streamlit** and **Hugging Face's Transformers** to perform sentiment analysis on user-provided text. The sentiment analysis is powered by the `cardiffnlp/twitter-roberta-base-sentiment` model, which classifies the text into three sentiment categories: **Negative**, **Neutral**, and **Positive**. The app processes text in chunks to handle long input and returns the overall sentiment with a confidence score.

## **Features**

- **Sentiment Analysis**: Classifies text into **Negative**, **Neutral**, or **Positive** categories.
- **Text Chunking**: Long texts are split into smaller chunks for efficient processing.
- **Emoji Representation**: Displays emojis for each sentiment category.
- **Confidence Score**: Shows the confidence level for the detected sentiment.
- **Streamlit Interface**: Simple and user-friendly web interface for easy interaction.

## **Installation**

To run this project locally, follow these steps:

### **Prerequisites**

Ensure that you have the following installed on your machine:

- Python 3.9 or above
- pip (Python package installer)

### 1.Install the required dependencies:
pip install -r requirements.txt

### 2. If you don't have a requirements.txt, you can manually install the necessary libraries using:
pip install streamlit transformers

## Usage:
#### After installing the required libraries, you can run the Streamlit app using:
- streamlit run app.py
- Replace app.py with the name of your Python file if it's different.
- The app will open in your default web browser. Enter some text in the input box and click Submit to see the sentiment analysis result.

## Functionality
- Input Text: You can input any text in the text area.
- Sentiment Analysis: The system will analyze the sentiment of the text and display the result as Positive, Neutral, or Negative, along with an emoji that represents the sentiment.
- Confidence Score: Shows the confidence of the model's prediction in percentage format.
- Text Chunking: If the text is too long, it will be split into chunks and analyzed piece by piece to ensure efficient processing.

## Code Explanation
- Sentiment Pipeline: The Hugging Face cardiffnlp/twitter-roberta-base-sentiment model is used for sentiment classification.
- Chunking: The input text is split into smaller chunks of 500 characters to manage large inputs efficiently.
- Emoji Mapping: Sentiment categories are mapped to their corresponding emojis (😟, 😐, 😀) for better visualization.
- Confidence Scores: The confidence for each sentiment is averaged across the chunks of text.

## Example
Here’s an example of how the app works:

Input Text: "I love this new movie! It's amazing and exciting."
Result: Sentiment: Positive 😀
Confidence: 97.3%




