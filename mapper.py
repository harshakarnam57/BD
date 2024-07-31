!/usr/bin/env python3
import sys
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
for line in sys.stdin:
    columns = line.strip().split(',')
    if len(columns) >= 8:
        movie_title = columns[0]
        review_content = columns[7]
        # Perform sentiment analysis on the review content
        sentiment = sia.polarity_scores(review_content)
        # Emit the movie title and sentiment score as key-value pair
        print(f'{movie_title},{sentiment["compound"]}')