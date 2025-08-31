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

best_team = None
max_types = 0

for j in combinations (pok_names, k):
    team_types = set()
    for i in j:
        pok_types = Pokedex[i]
        team_types.update(pok_types)
    print(f"Team: {j}, Types: {team_types}, Count: {len(team_types)}")
    if len(team_types) > max_types:
        best_team = j
        max_types = len(team_types)

print(f"Best Team: {best_team}, with {max_types} team types")