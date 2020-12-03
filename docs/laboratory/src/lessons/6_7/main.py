import csv
from collections import defaultdict

#----(open_csv)
def open_csv(f_path):
    result = []
    with open(f_path, mode='r') as csv_file:
        ## a
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        ## b
        #csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            result.append(row)
    return result

netflix_data = open_csv("data/netflix_titles.csv")


#----(netflix_types)
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

#----(netflix_types)
def netflix_countries():
    res_dict = dict()
    for row in netflix_data:
        for country_value in row["country"].split(", "):
            if country_value not in res_dict:
                res_dict[country_value] = []
            res_dict[country_value].append(row["show_id"])
    return res_dict

#----(print info)
italian_shows = netflix_countries()["Italy"]
for it_show_id in italian_shows:
    for show_row in netflix_data:
        if show_row["show_id"] == it_show_id:
            print(show_row["title"])
            break


show_types = netflix_types()
count_movies = 0
count_tvshows = 0
for it_show_id in italian_shows:
    if it_show_id in show_types[0]:
        count_movies += 1
    if it_show_id in show_types[1]:
        count_tvshows += 1
print(count_movies, count_tvshows)


all_countries = netflix_countries()
found = False
if "Finland" in all_countries:
    l_show_ids = all_countries["Finland"]
    for show_id in l_show_ids:
        if show_id in show_types[0]:
            found = True
print(found)