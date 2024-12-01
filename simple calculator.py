

print("******************************************************************")
print("*******************WELCOME TO SIMPLE CALCULATOR *******************")
print("******************************************************************")



num1=int(input("Enter First Number: \n" ))
num2=int(input("Enter Second Number: \n"))

num = int(input("Choose Operation: \n 1. Addition\n 2. Subtraction\n 3. Multiplication \n 4. Division \n\n"))
print("\n")
if num==1:
    add=num1+num2
    print(num1, "Addition", num2, "=", add)
elif num ==2:
    subs=num1-num2
    print(num1, "Subtracted ", num2, "=", subs)
elif num==3:
    mult=num1*num2
    print(num1, "Multiplied by", num2, "=", mult)
elif num==4:
    div=num1/num2
    print( num1, "Divided by", num2, "=", div)

