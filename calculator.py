num1 = int(input("Enter the first number : "))
opreation = input("Enter the opreation : ")
num2 = int(input("Enter the second number : "))

if opreation=="plus":
    print(num1+num2)
elif opreation=="minus":
    print(num1-num2)
elif opreation=="divide":
    print(num2/num1)
elif opreation=="multiply":
    print(num1*num2)
else:
    print("You have entered wrong spelling")
input()
