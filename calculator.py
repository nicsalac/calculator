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



