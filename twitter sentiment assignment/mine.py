import sys
import json


sentiment_scores = open("sentiment_scores")
twitter_data = open("twitter_data")

# Storing sentiment scores
scores = {}

for line in sentiment_scores:
    term, score = line.split("\t")
    scores[term] = int(score)

# Parsing tweets
