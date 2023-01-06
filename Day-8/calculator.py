from art import logo

# Define operations 
# define 4 functions
# ask user for the input num1 
# ask for operations 
# ask for num2 
# print the answer 
# whether they would like to continue or a fresh start?
# Enhancements 
    # Check if response is invlid - DONE
    # Add more functions like - squareroot, power etc

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2        

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

print(logo)

def calculator():
    num1 = float(input("What's the first number?: "))
    should_countiue = True
    while should_countiue: 
        for symbols in operations:
            print(symbols)
        invalid_symbol = True
        while invalid_symbol: 
            op_symbol = input("Pick an operation: ")
            if op_symbol in list(operations.keys()):
                invalid_symbol = False
            else: 
                print("Invalid symbol, try again")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[op_symbol]
        answer = round(calculation_function(num1=num1, num2=num2), 2)
        print(f"{num1} {op_symbol} {num2} = {answer}")

        response = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'q' to quit : ").lower()
        if response == 'y':
            num1 = answer
        elif response == 'n':
            calculator()
        elif response == 'q':
            should_countiue = False

calculator()

 
