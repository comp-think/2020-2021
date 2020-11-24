#----(ex) Recursive function for finding the pokemon champion
def pokemon_champion(l_table):
    len_list = len(l_table)
    if len_list == 1:
        return [l_table[0]]
    elif len_list == 2:
        p_attack = l_table[0][1]
        p_defend = l_table[1][2]
        if p_attack > p_defend:
            return [l_table[0]]
        else:
            return [l_table[1]]
    else:
        mid = len_list // 2
        return pokemon_champion(pokemon_champion(l_table[:mid]) + pokemon_champion(l_table[mid:]))

pokemon_tables = [("Poliwag",10,5),("Charmander",15,2),("Abra",8,7),("Pidgey",4,5),("Goldeen",6,8),("Bulbasaur",12,10),("Charmeleon",18,8),("Psyduck",3,4)]
# ("Poliwag",10,5) vs ("Charmander",15,2)       ("Abra",8,7) vs ("Pidgey",4,5)      ("Goldeen",6,8) vs ("Bulbasaur",12,10)      ("Charmeleon",18,8) vs ("Psyduck",3,4)
# ("Poliwag",10,5)vs("Abra",8,7)      ("Bulbasaur",12,10)vs("Charmeleon",18,8)
# ("Poliwag",10,5)vs("Bulbasaur",12,10)
# ("Bulbasaur",12,10)
print(pokemon_champion(pokemon_tables))
#OUTPUT: [('Bulbasaur', 12, 10)]