import random
Cnumber=random.randrange(1,10)
userInput=int(input("Enter your Number:--"))
if userInput>Cnumber:
    print("computer Number",Cnumber)
    print("your guess number is too high")
elif Cnumber>userInput:   
        print("computer Number",Cnumber)
        print("your guess number is too low")
else:
        print("computer Number",Cnumber)
        print("your guess number is too equal")