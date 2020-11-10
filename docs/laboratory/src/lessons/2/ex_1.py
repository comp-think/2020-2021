#----(a)
def is_friend_of_harry(p_name):
    friends_list = ["Ron", "Hermione", "Hagrid", "Dumbledore"]
    if p_name in friends_list:
        return True
    else:
        return False

print(is_friend_of_harry("Hagrid"))
print(is_friend_of_harry("Voldemort"))
print(is_friend_of_harry("Bellatrix"))

#----(b)
a = is_friend_of_harry("Hagrid")
b = is_friend_of_harry("Voldemort")
c = is_friend_of_harry("Bellatrix")
if a or b or c:
    print("Harry has a friend!")
else:
    print("Harry has no friends!!")

#----(c)
def is_friend_of_harry(p_name):
    friends_list = ["Ron", "Hermione", "Hagrid", "Dumbledore"]
    p_name = p_name.lower()
    p_name = p_name.strip()
    p_name = p_name.capitalize()
    if p_name in friends_list:
        return True
    else:
        return False

#----(d)
def is_prof_friend_of_harry(p_name):
    prof_list = ["Snape", "Lupin", "Hagrid", "Dumbledore"]
    if p_name in prof_list:
        if is_friend_of_harry(p_name):
            return True
        else:
            return False
    else:
        return False

print(is_friend_of_harry("Hagrid"))
print(is_friend_of_harry("Voldemort"))
print(is_friend_of_harry("Bellatrix"))
