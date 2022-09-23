# put debug points
# 1. stepover : steps to the next step (not necessarily next line) in the program
# 2. stepinto: opens up function calls that lie outside of the code that we have written
# 3. stepinto my code: does not open up function calls that lie outside of the code that we have written
# stepover and step into my code will have the same effect, but with a minor difference
import random

def generateRandom(upper):
    """
    :param upper: >= 0
    :return: int
    """

    r = random.randint(1, upper)
    return r


def main():
    run = True
    num1 = generateRandom(10)
    num2 = generateRandom(10)
    result = num1 * num2

    while run:
        ans = input("What is " + str(num1) + " x " + str(num2) + "? ")

        if ans.isdigit():
            if int(ans) == result:
                print("Correct!")
                run = False
            else:
                print("Incorrect! Try again.")
        else:
            print("Answer must be positive number, try again.")


# global vars
times = 10

for x in range(times):
    main()




