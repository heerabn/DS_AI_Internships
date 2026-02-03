num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
sum=num1+num2
print("the sum is:",sum)
choice= input("Enter operation ( -, *, /): ")
if choice == '-':
    print("Result:", num1 - num2)
elif choice == '*':
    print("Result:", num1 * num2)
elif choice == '/':
    print("Result:", num1 / num2)
else:
    print("Invalid operation")

#concatination example
name=input("Enter your name:")
print("welcome you",name)
age=int(input("Enter your age:"))
print("your age is:",age)



