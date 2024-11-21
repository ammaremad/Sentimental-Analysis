# Sentiment Analysis Using BERT

## Overview
This project implements a sentiment analysis model using a pre-trained BERT (Bidirectional Encoder Representations from Transformers) model to classify sentiments from a dataset of tweets. The primary goal is to analyze the sentiments expressed in social media texts and provide insights into public opinion.

## Project Structure
- **Data Cleaning**: The dataset is preprocessed to remove unnecessary columns, clean text data, and prepare it for analysis.
- **Exploratory Data Analysis (EDA)**: Visualization techniques are employed to understand the sentiment distribution and identify distinctive words associated with each sentiment category.
- **Model Implementation**: A pre-trained BERT model is utilized for sentiment classification, achieving high accuracy.
- **Model Evaluation**: The model's performance is evaluated using metrics such as accuracy, precision, recall, and F1-score.

## Dataset
The dataset used in this project is a collection of 1.6 million tweets, which includes the following columns:
- **Target**: Sentiment label (0 for negative, 1 for positive)
- **Id**: Unique identifier for each tweet
- **Date**: Timestamp of the tweet
- **Flag**: Unused column
- **User**: User who posted the tweet
- **Text**: The content of the tweet

### Data Cleaning Steps
1. **Remove Unnecessary Columns**: The `Id` and `User` columns are dropped as they do not contribute to sentiment analysis.
2. **Text Cleaning**: Links, numbers, and stopwords are removed from the text data to enhance the quality of the input for the model.
3. **Label Encoding**: The sentiment labels are encoded for model training.

### Visualization
- **Sentiment Distribution**: A pie chart and bar plot are created to visualize the distribution of sentiments in the dataset.
- **Word Clouds**: Distinctive words for positive and negative sentiments are visualized using word clouds.

## Model Implementation
The project utilizes the Hugging Face Transformers library to load a pre-trained BERT model for sentiment analysis. The model is tested with example texts and achieves an impressive accuracy of 100% on the test data.

### Model Evaluation
The model's performance is evaluated using:
- **Accuracy**: The proportion of correctly predicted sentiments.
- **Classification Report**: Detailed metrics including precision, recall, and F1-score.
- **Confusion Matrix**: A visual representation of the model's predictions compared to the actual labels.

## Deployment
The trained model and tokenizer are saved for future use, allowing for easy deployment in applications requiring sentiment analysis.

## Getting Started
To run this project locally, follow these steps:
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd sentiment-analysis-bert
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook or Python script to execute the analysis.

## Conclusion
This project demonstrates the effectiveness of using a pre-trained BERT model for sentiment analysis on social media data. The insights gained from the analysis can be valuable for understanding public sentiment and trends.

Feel free to reach out for any questions or collaborations!
