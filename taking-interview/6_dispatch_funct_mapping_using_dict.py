"""
using dictionary as lookup table for function dispatch

"""


def perform_addition(a, b):
    return a+b


def perform_subtraction(a, b):
    return a-b


def perform_multiplication(a,b):
    return a*b


def perform_division(a, b):
    return a/b


func_choice_dict = {                        # Point to note: func names are without()
    "+": perform_addition,                  # This is possible when all the functions take same number of
    "-": perform_subtraction,                   # arguments (here 2) or 0 arguments
    "x": perform_multiplication,
    "/": perform_division,
}


if __name__ == "__main__":
    while True:
        action = (input("Enter the mathematical operation to perform (+,-,x,/):"))
        if action in func_choice_dict:
            num1 = float(input("Enter the first number:"))
            num2 = float(input("Enter the second number:"))
            result = func_choice_dict[action](num1, num2)
            print(result)
        else:
            print("Invalid Operation")


# -------Leo's Note --------
"""
1. Dispatch or Function Mapping using a Dictionary
is a programming technique that allows you to associate functions with specific keys in a dictionary.
2. When we map a user-defined function to the key of a dictionary, we do not use ()
3. One thing to note is: All the user-defined function should not take any arguments or all should take same
    number of arguments 
4. Benefit: Instead of using long if-else chains or nested switch statements to chose which 
    functions to choose to execute based on some condition, we can use a dictionary as a lookup 
    table for function dispatch. This allows for a cleaner code.
    
"""