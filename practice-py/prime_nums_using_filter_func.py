def is_prime(num):
    """
    function to check if a number is prime or not
    @param num: int
    @return: Boolean
    """
    # A number is said to be prime if it is divisible by 1 and itself only
    # The divisor will definitely be less than the half of number itself

    for _ in range(2, (num//2)+1):  # whatever the number be, just taking the half of the num, +1 so that it is included
        if num % _ == 0:
            return False

    return True


if __name__ == "__main__":
    # print(is_prime(53)) # Check if number 53
    print(list(filter(is_prime, range(50, 100))))

""" Takeaways
Filter function - Returns a sequence comprising of those elements of the iterables, for which the function returns True
filter(function, iterable) 

1) The user-defined function to be used in the filter function should be mentioned without ()
2) The user-defined function to be used in pythonic filter function should be returning boolean results,
    only then it can be used in filter function 

Moto of the question in interview:
If one knows the use of filter function.
If one know how to find out if a number is Prime or not


"""