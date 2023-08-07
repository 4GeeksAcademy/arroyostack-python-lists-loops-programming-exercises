from collections import Counter


par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
def count_character_frequency(phrase):
    for i in phrase.lower():
        if i == " ": pass
        elif i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

count_character_frequency(par)

print(counts)

# Alternative solution

# frequency_dictionary = Counter(par.lower())

# print(frequency_dictionary)


