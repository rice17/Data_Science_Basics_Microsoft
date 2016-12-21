import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    lines(sent_file)
    lines(tweet_file)

scores = {}

def make_dict(sentiment):
    for line in sentiment:
        term, score = line.split("\t")
        scores[term] = int(score)

tweets = []

def get_tweets(twitter_file):
    data = twitter_file.read()
    json_data = json.loads(data)
    for line in json_data:
        for x in line:
            tweets.append(x['text'])

def calculate_scores(tweets):
    total = 0
    positive = 0
    negative = 0    
    for text in tweets:
        text = text.lower()
        weed = ".,!?\"\'()/"
        for each in weed:
            text.replace(each, "")
        words = text.split(' ')
        scores_subtotal = 0
        for each_word in words:
            if scores.has_key(each_word):
                scores_subtotal += scores[each_word]
        if scores_subtotal > 0:
            positive += 1
        elif scores_subtotal < 0:
            negative += 1
        total += 1
        print scores_subtotal
    
    print "Positive responses %.2f"%(float(positive*100)/total) + "%"
    print "Negative responses %.2f"%(float(negative*100)/total) + "%"
    

if __name__ == '__main__':
    main()
    sentiment_scores = open(sys.argv[1])
    make_dict(sentiment_scores)
    tweets_file = open(sys.argv[2])
    get_tweets(tweets_file)
    print len(tweets)
    calculate_scores(tweets)
