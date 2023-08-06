my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

#Your code go from here:
def maxInteger(int_list):
    current_number = 0
    for i in int_list:
        if i > current_number:
            current_number = i
        else: pass
    
    return current_number


print(maxInteger(my_list))

# Alternative Solution
# def maxInteger(int_list):
    #     return max(int_list)

