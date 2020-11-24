#----(ex) Recursive function for handling a set of pokemon cards
evolution_map = {
    "Poliwag": "Poliwhirl",
    "Bulbasaur": "Ivysaur",
    "Charmander": "Charmeleon",
    "Pidgey": "Pidgeotto",
    "Psyduck": "Golduck",
    "Abra": "Kadabra"
}

cards_set = set()
def pokemon_cards(l_pokemons):
    len_list = len(l_pokemons)
    if len_list == 1:
        pokemon_name = l_pokemons[0]
        if pokemon_name not in cards_set:
            cards_set.add(pokemon_name)
        else:
            cards_set.remove(pokemon_name)
            level2_pokemon = evolution_map[pokemon_name]
            cards_set.add(level2_pokemon)
    else:
        mid = len_list // 2
        pokemon_cards(l_pokemons[:mid])
        pokemon_cards(l_pokemons[mid:])
        return list(cards_set)

l_cards = ["Poliwag", "Pidgey", "Abra", "Pidgey", "Charmander", "Bulbasaur", "Charmander", "Psyduck", "Poliwag","Goldeen"]
print(pokemon_cards(l_cards))
#OUTPUT: {'Poliwhirl', 'Charmeleon', 'Bulbasaur', 'Psyduck', 'Pidgeotto', 'Goldeen', 'Abra'}