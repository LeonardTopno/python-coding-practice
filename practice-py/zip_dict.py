dict_1 = {"first_name": "Leonard",
          "last_name": "Topno",
          "job_title": "Technical Manager"}
dict_2 = {
    "first_name": "Abhilasha",
    "last_name": "Horo",
    "job_title": "Educator",
    "salary": "Rs. 25000"
}

# Traversing dictionaries in parallel
print(tuple(zip(dict_1.items(), dict_2.items())))

# Leo's note: zip() does not generate tuple but a zip-object, which can then be converted to tuple or list

for (k1, v1), (k2, v2) in zip(dict_1.items(), dict_2.items()):
    print(k1, "-->", v1)
    print(k2, "-->", v2)

print(dict_1.items())
print(dict_1.keys)  # Leo: Observe that it returns a List
print(dict_1.get("first_name"))
print(dict_1["salary"])



