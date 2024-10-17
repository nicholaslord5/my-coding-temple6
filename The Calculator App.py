# 1. The Calculator App
# Objective: The aim of this assignment is to build a basic calculator 
# that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

# Task 3: Ensure your code can handle division by zero and other potential errors. 
# So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

### Greeting ###
print("Ahoy! Here be ye olde trusty calculator!")

### Arithmetic functions ###
def add (x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    try: ###
        return x / y
    except ZeroDivisionError: 
        return "Division by zero is not allowed."

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    ### take input from the user ###
    choice = input("Enter choice(1/2/3/4): ")

    ### check if choice is one of the four options ##
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number from the options.") #### if input letters or other symbols
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        ### check for another calculation ###
        #### break the while loop if answer is no ###
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation != "yes":
          print("Fair winds, me harty!")
          break
    else:
        print("Invalid Input. Please select an option from the list.") ### input error msg ###
