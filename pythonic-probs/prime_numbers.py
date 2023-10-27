# Python program to print PRIME Numbers between a given interval

start = 2
end = 10

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                # print(f"{num} is not prime")
                break
        else:
            print(f"{num} is prime")
    else:
        print(f"{num} is not prime")



print("--------------------------------------------------")
# Program to check if a number is prime or not
# Input from the user
# num = int(input("Enter a number: "))

for num in range(start, end+1):
    # If number is greater than 1
    if num > 1:
        # Check if factor exist
        for i in range(2, (num//2)+1):     #//2 + 1
            if (num % i) == 0:
                # print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")

    # Else if the input number is less than or equal to 1
    else:
        print(num, "is not a prime number")


"""
def is_prime(numb: int):
    if numb > 1:
        for i in range(2, numb//2+1):
            if numb % i == 0:
                print({i})
                break
            else:
                print(f"{numb} is prime")
                return True
    return False


print(is_prime(9))



#lambda numb: False for i in range(2, numb//2+1) if numb % i == 0 else True

print(list(filter(is_prime, range(2, 10))))
"""