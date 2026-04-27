
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def calculate(action, a, b):
    return action(a, b)

print (calculate(addition, 10, 5))
print (calculate(subtraction, 10, 5))