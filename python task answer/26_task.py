import random as r

answer = r.randint(1, 100)

while True:
    guss = int(input("Guess a number between 1 and 100: "))
    if guss == answer:
        print(f"Congratulations! You guessed the correct number: {answer}")
        break
    else:
        print("Wrong guess. Try again!")
    
    try_again = input("Do you want to try again? (yes/no): ")
    if try_again != "yes":
        print(f"The correct number was: {answer}, thank you for playing!")
        break
    else :
        print("Let's try again!")