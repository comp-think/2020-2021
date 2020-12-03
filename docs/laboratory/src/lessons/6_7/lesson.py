import csv

#----(open_csv)
def open_csv(f_path):
    result = []
    with open(f_path, mode='r', encoding='utf-8') as csv_file:
        ## b
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            result.append(row)
    return result

netflix_data = open_csv("data/netflix_titles.csv")


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
print(netflix_data[0])


