mix = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code below:
def find_type(input_list):
    for element in input_list:
        print(type(element))

find_type(mix)