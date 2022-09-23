# 2 : List Comprehension

even_num_list = [x for x in range(101) if not x % 2]
print(even_num_list)

odd_num_list = [x for x in range(101) if x % 2]
print(odd_num_list)

prime_num = [x for x in range(2, 101) if n not in [n for i in range(2, n) if n%2]]
print(prime_num)

# 1 : Swap 2 numbers a,b = b, a
a, b = 4, 5
print(a, b)
a, b = b, a  # swapping two numbers a,b
print(a, b)


