Celsius_values = [-2,34,56,-10]



def fahrenheit_values(x):
    conversion = (x - 32) / 1.8

    return "{:.1f}".format(conversion)
# the magic go here:

   
result = list(map(fahrenheit_values, Celsius_values))
print(result)
