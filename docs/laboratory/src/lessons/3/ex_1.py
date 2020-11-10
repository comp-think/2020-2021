l_schedule = ["Introduction to Computational Thinking","Algorithms","Computability","Programming Languages","Laboratory","Organising information: ordered structures","Laboratory","Brute-force algorithms","Organising information: unordered structures","Laboratory","Recursion","Laboratory","Divide and conquer algorithms","Dynamic programming algorithms","Laboratory","Organising information: trees","Laboratory","Backtracking algorithms","Laboratory","Organising information: graphs","Laboratory","Project: specification","Greedy algorithms"]

#----(a)
def lab_lessons(a_list):
    count = 0
    for title in a_list:
        if title == "Laboratory":
            count += 1
    return count

#----(b)
def all_before_lab(a_list):
    result = []

    i = 0
    title = a_list[i]
    while title != "Laboratory":
        result.append(title)
        i += 1
        title = a_list[i]

    return result

#----(c)
def all_before_lab_n(a_list,n):
    result = []

    i = 0
    count_lab = 0
    while count_lab < n:
        title = a_list[i]
        result.append(title)
        if title == "Laboratory":
            count_lab += 1
        i += 1

    return result

#----(d)
l_schedule_extended = [
("14/10/20",2,"Introduction to Computational Thinking"),
("16/10/20",2,"Algorithms"),
("19/10/20",2,"Computability"),
("21/10/20",2,"Programming Languages"),
("23/10/20",2,"Laboratory"),
("26/10/20",2,"Organising information: ordered structures"),
("28/10/20",2,"Laboratory"),
("30/10/20",2,"Brute-force algorithms"),
("09/11/20",2,"Organising information: unordered structures"),
("11/11/20",2,"Laboratory"),
("13/11/20",2,"Recursion"),
("16/11/20",2,"Laboratory"),
("20/11/20",2,"Divide and conquer algorithms"),
("23/11/20",2,"Dynamic programming algorithms"),
("25/11/20",2,"Laboratory"),
("27/11/20",2,"Organising information: trees"),
("30/11/20",2,"Laboratory"),
("02/12/20",2,"Backtracking algorithms"),
("04/12/20",2,"Laboratory"),
("09/12/20",2,"Organising information: graphs"),
("11/12/20",2,"Laboratory"),
("14/12/20",2,"Project: specification"),
("16/12/20",2,"Greedy algorithms")
]

def max_lessons_hours(a_list, max_hours):
    result = []
    tot_hours = 0
    i = 0
    while tot_hours < max_hours:
        title = a_list[i][2]
        result.append(title)
        tot_hours += a_list[i][1]
        i += 1

    return result
