celsius_temps = [0, 10, 20, 30, 37, 100]

converted_fahrenheit = list(map(lambda x: (x * 9/5) + 32, celsius_temps))

print (converted_fahrenheit)