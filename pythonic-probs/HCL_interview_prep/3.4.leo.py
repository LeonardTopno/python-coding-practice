
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
