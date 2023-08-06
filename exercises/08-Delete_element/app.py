people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    filtered_people = []
    
    for name in people:
        if name == person_name: pass 
        else: filtered_people.append(name)
    
    return filtered_people
            

    
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))