def get_largest_range(array):
    hasht = {x:0 for x in array}  # Dict comprehension
    fin_left_val = fin_right_val = 0

    print(hasht)

    for number in array:
        if hasht[number] == 0:  # Checking/ensuring we have not visited it earlier
            print(hasht)
            left_val = number - 1
            right_val = number + 1

        while left_val in hasht:
            hasht[left_val] = 1  # Marking it visited
            left_val -= 1

        left_val += 1

        while right_val in hasht:
            right_val += 1
            hasht[right_val] = 1

        right_val -= 1

        if (fin_right_val - fin_left_val) >= (right_val - left_val):
            fin_right_val = right_val
            fin_left_val = left_val

    return [fin_left_val, fin_right_val]


if __name__ == "__main__":
    arr = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    print("Leo")
    print(get_largest_range(arr))
