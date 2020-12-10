import csv
import matplotlib.pyplot as plt

#----(open_csv)
def open_csv(f_path):
    result = []
    with open(f_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            result.append(row)
    return result

netflix_data = open_csv("data/netflix_titles.csv")

# define a dict based on the year values in "date_added"
dict_years = dict()
for row in netflix_data:
    if row["date_added"] != "":
        year = row["date_added"].split(", ")[1]
    if row["release_year"] != "":
        release_year = row["release_year"]
    delta = int(year) - int(release_year)
    if year not in dict_years:
        dict_years[year] = []
    dict_years[year].append(delta)

avg_dict_years = dict()
for year in dict_years:
    avg_dict_years[year] = sum(dict_years[year]) / len(dict_years[year])
    avg_dict_years[year] = round(avg_dict_years[year],2)

#I need to order the dict
netflix_years = list(avg_dict_years.items())
sorted_netflix_years = sorted(netflix_years, key=lambda tup: tup[0])

#define the data and labels to plot
data = []
labels = []
for a_tup in sorted_netflix_years:
    data.append(a_tup[1])
    labels.append(a_tup[0])

plt.plot(labels, data)
plt.title('Netflix shows release vs addition')
plt.ylabel('Average delta between the added and released year')
plt.xlabel('Years')
plt.show()
