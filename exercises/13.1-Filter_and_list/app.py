
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def filtered_word(prefix):
    return True if prefix.startswith("R") else False

resulting_names = list(filter(filtered_word, all_names))

print(resulting_names)




