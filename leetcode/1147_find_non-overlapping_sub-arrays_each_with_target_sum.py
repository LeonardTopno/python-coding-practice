# HashMap and
def find_min_sum_of_len_of_2_sub_arr_with_target_sum(arr, target):
    min_sum_of_len = 999999  # to store the sum of length of sub-arrays
    best = [999999]*len(arr)  # best is a list
    prefix = 0
    latest = {0: -1}

    for index, elem in enumerate(arr):
        prefix += elem
        if (prefix - target) in latest:
            ii = latest[prefix-target]  # Took Value of a key from the dict latest

            if ii >= 0:  # If the value(this value is actually length) is greater than 0
                min_sum_of_len = min(min_sum_of_len, index-ii + best[ii])

            best[index] = index - ii

        if index:   # checking if index is non-zero (everything except the first elem index)
            best[index] = min(best[index-1], best[index])
            latest[prefix] = index


    return min_sum_of_len if min_sum_of_len < 999999 else -1  # Leo : Note how if-else has been used in return


if __name__ == "__main__":
    arr = [5, 2, 6, 3, 2, 5]
    target = 5
    print(find_min_sum_of_len_of_2_sub_arr_with_target_sum(arr, target))


"""
https://www.tutorialspoint.com/program-to-find-two-non-overlapping-sub-arrays-each-with-target-sum-using-python
"""
