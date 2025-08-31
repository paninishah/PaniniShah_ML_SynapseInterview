from itertools import combinations

Pokedex = {
"Pikachu": ("Electric",),
"Charizard": ("Fire", "Flying"),
"Lapras": ("Water", "Ice"),
"Machamp": ("Fighting",),
"Mewtwo": ("Psychic", "Fighting"),
"Hoopa": ("Psychic", "Ghost", "Dark"),
"Lugia": ("Psychic", "Flying", "Water"),
"Squirtle": ("Water",),
"Gengar": ("Ghost", "Poison"),
"Onix": ("Rock", "Ground")
}

k = int(input("enter a number: "))

pok_names = list(Pokedex.keys())

for j in combinations (pok_names, k):
    print(j)