theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
wiki_woko_generator = list(map(lambda n: "wiki" if n == 1 else "woko" ,theBools))

print(wiki_woko_generator)