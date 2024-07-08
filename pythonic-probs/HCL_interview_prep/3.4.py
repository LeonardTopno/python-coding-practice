# Given byte string
given_string = "b'7Aebc\n"  # seems to be byte sting id there was a ' at the end but it does not have

# Extract the string between b' and \n

# Convert byte string to regular string (assuming the frequently used UTF-8 encoding)
#regular_string = given_string.decode('utf-8')

#print(f"regular_string = {regular_string}")

string = "b'7Aebc\n"

# Find the index of `b'` and `\n`
start_index = string.index("b'") + 2
end_index = string.index("\n")

print(f"start_index {start_index}")
print(f"end_index {end_index}")


# Extract the substring between `b'` and `\n`
extracted_string = string[start_index:end_index]

# Print the extracted string
print(extracted_string)
