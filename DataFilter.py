import json
import pandas as pd
import matplotlib.pyplot as plt
import re

tweets_data_path = './test-out.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

art_data = []
movies_data = []
travel_data = []
a, m, t = 0, 0, 0
for item in tweets_data:
    if word_in_text('travel', item['text']) == True and  t < 15000:
        travel_data.append(item)
        t += 1
    elif word_in_text('movies', item['text']) == True and m < 15000:
        movies_data.append(item)
        m += 1
    elif word_in_text('art', item['text']) == True and a < 15000:
        art_data.append(item)
        a += 1
    if a >= 15000 and m >= 15000 and t >= 15000:
        break
new_data = art_data + movies_data + travel_data

with open('data.txt', 'w') as f:
    json.dump(new_data, f)