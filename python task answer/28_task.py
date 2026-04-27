call_counter = 0

def factorial (n):
    global call_counter
    call_counter += 1
    if n ==0 or n ==1 :
        return 1
    else:
        return n*factorial(n-1)
    
print (f" your factorial is {factorial(5)} and the number of calls is {call_counter}")