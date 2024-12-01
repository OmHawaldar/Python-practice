# NUMBER GUESSING GAME
print("******************************************************************")
print("******************* WELCOME TO NUMBER GUESSING GAME *******************")
print("******************************************************************")
num1=random.randrange(1,100)
while True:
    gn=int(input("Guess the Number: \n"))
    if gn>num1:
        print("Try again, guessed number is larger ")
    elif gn<num1:
        print("Try again, guessed number is smaller ")
    if gn==num1:
        print(" You Won! Your Guess is",gn, "\n Number to be Guessed is",num1)
        break
