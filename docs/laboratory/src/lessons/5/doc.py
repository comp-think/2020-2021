#----Example: recursive function for calculating n! (factorial)
def factorial_recursive(n):
    #Base case
    if n == 1:
        return 1
    #Recursive case: n * (n-1)!
    else:
        return n * factorial_recursive(n-1)
print(factorial_recursive(5))
#OUTPUT: 120

#----(ex) Recursive function for building sentences
def build_sentence(l_words, dict_sentence = dict()):
    len_list = len(l_words)
    if len_list == 1:
        word_parts = l_words[0].split(":")
        if word_parts[0] not in dict_sentence:
            dict_sentence[word_parts[0]] = ""
        dict_sentence[word_parts[0]] += word_parts[1] + " "
    else:
        mid = len_list // 2
        build_sentence(l_words[:mid])
        build_sentence(l_words[mid:])
        return dict_sentence

l_words = ["it:ciao", "en:help", "en:me", "it:sono", "en:I", "en:am", "it:Silvio", "en:in", "en:trouble"]
#print(build_sentence(l_words))
#OUTPUT: {'it': 'ciao sono Silvio ', 'en': 'help me am I in trouble '}
