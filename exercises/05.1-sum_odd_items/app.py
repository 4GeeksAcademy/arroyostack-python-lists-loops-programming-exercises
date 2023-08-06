arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sum_oods(number_sequence):
    total = 0

    for number in number_sequence:
        if number % 2 != 0:
            total += number
            
    return total



print(sum_oods(arr))


