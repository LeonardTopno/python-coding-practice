# generator to return every 3rd element from a given list
def get_every_3rd_elem(given_list):
    
    for counter, item in enumerate(given_list): # note that counter/index starts from 0 by default

        if counter >= 2 and counter%2 == 0 : #if the counter is divisible by 2, it is even. Even numbers are every 3rd element, except for 0th-index
            yield item


# driver code
given_list = [2,4,6,8,10,12,14,16,18,20]

#printing 3rd elements from the given list

print("Original List: ", given_list)
print("The 3rd elements in the given list are: ", end = " ")
for elem in get_every_3rd_elem(given_list): # observer how generator is called here
    print(elem, end = " ")
