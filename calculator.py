# This function adds two numbers
def add(number_one, number_two):
    return number_one + number_two

# This function subtracts two numbers
def subtract(number_one, number_two):
    return number_one - number_two

# This function multiplies two numbers
def multiply(number_one, number_two):
    return number_one * number_two

# This function divides two numbers
def divide(number_one, number_two):
    return number_one / number_two

while True:
    # take the input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    if choice == '1' :
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2' :
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3' :
        print(num1, "*", num2, "=", multiply(num1, num2))
    
    elif choice == '4' :
        print(num1, "/", num2, "=", divide(num1, num2))

    # check if user wants another calculation
    # break thw while loop if answer is no
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no" :
        break
else:
    print("Invalid Input")

