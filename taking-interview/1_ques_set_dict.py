"""
Q: You have two lists.
Can you build a dictionary from these two sequences, where  elements of list1 is to be used as keys
"""

fields = ["first_name", "last_name", "designation"]
values = ["Leo", "Topno", "Software Engineer"]

my_dict = dict(zip(fields,values))

print(my_dict)

# 2. ================================================================
""" 
Q: Can you update (add a key-value pair) to this dictionary.
"""

field = ["designation"]
value = ["Technical Architect"]

# my_dict.update({"designation" : "SF"})

my_dict.update(zip(field, value))

print(my_dict)

# 3. ================================================================
"""

Q: Can you add a field "location" to the dictionary and assign the value to "Bengaluru"

my_dict.update() is used to update an the value of already existing key.
also alo to add a new key-value pair to the dictionary if not the key does not already exist.


"""

my_dict.update({"location":"Bengaluru"})

print(my_dict)

my_dict["location"] = "Chennai"

print(my_dict)


my_list = [[10,20,30],[40,50,60],[70,80,90]]
