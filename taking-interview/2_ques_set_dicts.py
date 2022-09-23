"""
Topic: Intersection of two dictionaries
"""

dict_1 = {"first_name": "Leo", "last_name": "Topno", "college" : "IIT Guwahati", "Degree": "B.Tech"}
dict_2 = {"first_name": "John", "last_name" : "Paul", "designation":"Group Manager", "location": "Chennai"}

# intersection = ["first_name", "last_name"]

# solution aproach: 1
intersection_1 = []
for key in dict_1.keys():                  #dict_1 -> dict_1.keys()
    if key in dict_2.keys():
        intersection_1.append(key)

print(intersection_1)


# solution appraoch:2 -> using dict.keys(), same as sol_1
intersection_2 = []
for key in dict_1:
    if key in dict_2:
        intersection_2.append(key)

print(intersection_2)


# solution approach: 3 -> using list_comprehension] in sol_2
intersection_3 = [key for key in dict_1 if key in dict_2]
print(intersection_3)


# ============= Something Extra: How to access 
print(dict_1.items())
print(dict_1.keys())
print((dict_1.values()))