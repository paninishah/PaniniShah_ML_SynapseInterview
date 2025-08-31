runes = input("enter runes: ").upper()

runes_needed = ['L', 'U', 'M', 'O', 'S']

# empty dictionary
my_runes = {} 

for i, rune in enumerate(runes):
    my_runes[rune] = my_runes.get(rune, 0) + 1

    if (my_runes.get('L', 0)>= 1 and
        my_runes.get('U', 0)>= 1 and
        my_runes.get('M', 0)>= 1 and 
        my_runes.get('O', 0)>= 1 and
        my_runes.get('S', 0)>= 1):
        print(f"formed at step {i+1}")
        