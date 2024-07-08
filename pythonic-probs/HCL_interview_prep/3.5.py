"""
list1 = [1,2,3]
list2 = [4,5,""]
Form the dictionasry using list1 and list2 and validate key 3 has empty value
"""



# Given lists
list1 = [1, 2, 3]
list2 = [4, 5, ""]

# Form the dictionary using zip()
my_dict = dict(zip(list1, list2))


# alidate if key 3 has an empty value
# ------- Method 1:  
key_to_check = 3
if key_to_check in my_dict and my_dict[key_to_check] == "":
    print(f"Key {key_to_check} has an empty value.")
else:
    print(f"Key {key_to_check} either does not exist or does not have an empty value.")

# Print the resulting dictionary
print("Resulting dictionary:", my_dict)



# ------Method 2 using my_dict.get(key_to_check, None)

key_to_check = 3
value = my_dict.get(key_to_check, None)

if value == "":
    print(f"Key {key_to_check} has an empty value.")
elif value is None:
    print(f"Key {key_to_check} does not exist in the dictionary.")
else:
    print(f"Key {key_to_check} exists but does not have an empty value: {value}")

