#Esay questions
#Question1
num = int(input("Enter a number: "))

if num > 0:
    print("num is positive")
elif num == 0:
    print("num is zero")
else:
    print("num is negative")
num = int(input("Enter a number: "))
#Question2
if num % 2 == 0:
    print("num is even")
else:
    print("num is odd")
num = int(input("Enter a number: "))
#Question3
if num >= 18:
    print("eligible to vote")
else:
    print("not eligible")
#Question4
def number(a, b):
    if a > b:
        print("a is greater")
    else:
        print("b is greater")

number(10, 20)
#Question5
num = int(input("Enter a number: "))

if num >= 40:
    print("pass")
else:
    print("fail")
#Question6
num = int(input("Enter a number: "))

if num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
elif num == 7:
    print("Sunday")
else:
    print("Invalid input! Enter a number between 1 and 7.")

#Question7
def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return
        else:
            print("Invalid operator! Please use +, -, *, or /.")
            return
        
        print(f"Result: {result}")
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")

calculator()

#Question8
num = int(input("Enter a number: "))

if num == 1:
    print("January")
elif num == 2:
    print("February")
elif num == 3:
    print("March")
elif num == 4:
    print("April")
elif num == 5:
    print("May")
elif num == 6:
    print("June")
elif num == 7:
    print("July")
elif num == 8:
    print("August")
elif num == 9:
    print("September")
elif num == 10:
    print("October")
elif num == 11:
    print("November")
elif num == 12:
    print("December")
else:
    print("Invalid input! Enter a number between 1 and 12.")
# Medium Questions

#  Question-1
def greatestNumber(num1, num2, num3):
    if num1>num2:
        if num1>num3:
            return num1
        return num3
    elif num2>num3:
        return num2
    return num3
print(greatestNumber(10,20,30))
#  Question-2
def leapYear(year):
    if (year % 400 == 0 and year % 100 != 0 ) or ( year % 4 == 0 ):
            return "Leap Year"
    else:
        return "Not A Leap Year"
print(leapYear(2024))
