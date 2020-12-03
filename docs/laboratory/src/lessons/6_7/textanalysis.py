#----(tokenization and stopwords)
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "I want to tokenize and remove all the stopwords from this sentence"

# Tokenize the given sentence
word_tokens = word_tokenize(example_sent)

# Filter the stopwords
stop_words = set(stopwords.words('english'))
filtered_sentence = []
for w in word_tokens:
    if not w in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)

#----(pre)

import csv
def open_csv(f_path):
    result = []
    with open(f_path, mode='r', encoding='utf-8') as csv_file:
        ## b
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            result.append(row)
    return result

netflix_data = open_csv("data/netflix_titles.csv")

#----(tokenization and stopwords netflix titles)
def netflix_titles_tokens():
    stop_words = set(stopwords.words('english'))
    result = set()
    for show in netflix_data:
        word_tokens = word_tokenize(show["title"])
        filtered_sentence = []
        for w in word_tokens:
            if not w in stop_words:
                filtered_sentence.append(w)
        result.update(filtered_sentence)
    return result

print(netflix_titles_tokens())


#----(tokenization count)

from nltk.probability import FreqDist

def netflix_director_names():
    result = []
    for show in netflix_data:
        word_tokens = word_tokenize(show["director"])
        result += word_tokens
    return FreqDist(result)

counts = netflix_director_names()
print(counts.most_common(10))


print(FreqDist(["hi","bye","ciao","bye","hi"]))