sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))    
sub3 = int(input("Enter marks for subject 3: "))

total = sub1 + sub2 + sub3
average = total / 3

print (average)

if average >= 90:
    print("Grade: A")

elif average >= 80:
    print("Grade: B")

elif average >= 70:
    print("Grade: C")

elif average >= 35:
    print("Grade: D")

elif average < 35:
    print("you are fail")
