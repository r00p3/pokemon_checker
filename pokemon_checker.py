
with open('drawn_pokemon.txt', 'r') as f:
    pokemon_list = f.read().splitlines()
    pokemon_list = [pokemon.lower() for  pokemon in pokemon_list]

failed = True

while failed:
    chosen_pokemon = input("Enter Pokemon to check: ")
    while chosen_pokemon in pokemon_list:
        print(f"You've already drawn this Pokemon. You drew it on day {pokemon_list.index(chosen_pokemon)+1}")
        chosen_pokemon = input("Enter Pokemon to check: ")

    print(f"The Pokemon to draw for day {len(pokemon_list)+1} is {chosen_pokemon}.")
    confirm = input("Is this correct? Add to fhateile? (Y/N): ").lower()
    if confirm == "Y".lower():
        with open('drawn_pokemon.txt', 'a') as file:
            file.writelines(chosen_pokemon.title() + "\n")
        failed = False
    else: 
        failed = True
        print()
        print("##################################" + '\n')
