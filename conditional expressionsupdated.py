# Python Basic Programs by Bhushan Fulari

# 1. Check whether year is leap or not
print("\tTo check whether year is leap or not")
year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year\n")
else:
    print("It is not a leap year\n")

# 2. Check the student is pass or fail
print("\tCheck the student is pass or fail")
marks = int(input("Enter the obtained marks: "))
if marks >= 35:
    print("Pass\n")
else:
    print("Fail\n")

# 3. Check the person is eligible for vote or not
print("\tCheck the person is eligible for vote or not")
age = int(input("Enter the age: "))
if age >= 18:
    print("Applicable for vote\n")
else:
    print("Not applicable for vote\n")

# 4. Check the temperature
print("\tCheck the temperature")
temp = int(input("Enter your current temperature: "))
if temp >= 25:
    print("Hot\n")
else:
    print("Cold\n")

# 5. Check the number is even or odd
print("\tCheck the number is even or odd")
num = int(input("Enter the number: "))
if num % 2 == 0:
    print("The number is even\n")
else:
    print("The number is odd\n")

# ✅ 6. Simple Calculator
print("\tSimple Calculator")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print(f"Result: {n1 + n2}\n")
elif op == "-":
    print(f"Result: {n1 - n2}\n")
elif op == "*":
    print(f"Result: {n1 * n2}\n")
elif op == "/":
    if n2 == 0:
        print("Cannot divide by zero\n")
    else:
        print(f"Result: {n1 / n2}\n")
else:
    print("Invalid operator\n")
