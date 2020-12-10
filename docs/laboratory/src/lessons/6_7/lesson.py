import csv

#----(open_csv)
def open_csv(f_path):
    result = []
    with open(f_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            result.append(row)
    return result

netflix_data = open_csv("data/netflix_titles.csv")
#print(netflix_data[2])


def netflix_types():
    l_movies = []
    l_tvshow = []
    for row in netflix_data:
        if row["type"] == "Movie":
            l_movies.append(row["show_id"])
        else:
            if row["type"] == "TV Show":
                l_tvshow.append(row["show_id"])
    return (l_movies,l_tvshow)

neflix_types_tuple =  netflix_types()

#----(netflix_types)
def netflix_countries():
    res_dict = dict()
    for row in netflix_data:
        for country_value in row["country"].split(", "):
            if country_value not in res_dict:
                res_dict[country_value] = []
            res_dict[country_value].append(row["show_id"])
    return res_dict



italian_shows = netflix_countries()["Italy"]

for it_show_id in italian_shows:
    for show_row in netflix_data:
        if show_row["show_id"] == it_show_id:
            #print(show_row["title"])
            break

show_types = netflix_types()
count_movies = 0
count_tvshows = 0
for it_show_id in italian_shows:
    if it_show_id in show_types[0]:
        count_movies += 1
    if it_show_id in show_types[1]:
        count_tvshows += 1

all_countries = netflix_countries()
found = False
if "Finland" in all_countries:
    l_show_ids = all_countries["Finland"]
    for show_id in l_show_ids:
        if show_id in show_types[0]:
            found = True
print(found)



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



from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def netflix_titles_tokens():
    stop_words = set(stopwords.words('english'))
    result = set()

    for show in netflix_data:
        word_tokens = word_tokenize(show["title"])
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
        result.update(filtered_sentence)
    return result

from nltk.probability import FreqDist

def netflix_director_names():
    result = []
    for show in netflix_data:
        word_tokens = word_tokenize(show["director"])
        # 

        result += word_tokens
    return FreqDist(result)

counts = netflix_director_names()

print(counts.most_common(10))