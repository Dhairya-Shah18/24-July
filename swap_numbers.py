#Program to Swap Two Number Without using a Third Variable

num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))

print("First Number:",num1)
print("Second Number:",num2)


num1=num1+num2
num2=num1-num2
num1=num1-num2

print("Ater Swaping")
print("First Number:",num1)
print("Second Number:",num2)