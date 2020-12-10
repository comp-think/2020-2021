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


dict_years = dict()
for row in netflix_data:
    if row["date_added"] != "":
        year = row["date_added"].split(", ")[1]
        if year not in dict_years:
            dict_years[year] = 0
        dict_years[year] += 1

#I need to order the dict
netflix_years = list(dict_years.items())
sorted_netflix_years = sorted(netflix_years, key=lambda tup: tup[0])


data = []
labels = []
for a_tup in sorted_netflix_years:
    data.append(a_tup[1])
    labels.append(a_tup[0])

# x-Axis ticks and label
plt.xticks(range(len(data)), labels)
plt.xlabel('Years')

# y-Axis label
plt.ylabel('Number of Shows')

# chart title
plt.title('Netflix shows per year')

# plt a bar
plt.bar(range(len(data)), data)
plt.show()