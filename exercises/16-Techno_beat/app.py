def lyrics_generator(beat_list):
    beat = []
    count = 0
    for i in beat_list:
        if i == 0:
            beat.append("Boom")
        elif i == 1:
            beat.append("Drop the base")
            count += 1
            if count == 3:
                beat.append("!!!Break the base!!!")
                count = 0
    return beat


# Your code go above, nothing to change after this line:
print(lyrics_generator([0, 0, 1, 1, 0, 0, 0]))
print(lyrics_generator([0, 0, 1, 1, 1, 0, 0, 0]))
print(lyrics_generator([0, 0, 0]))
print(lyrics_generator([1, 0, 1]))
print(lyrics_generator([1, 1, 1]))
