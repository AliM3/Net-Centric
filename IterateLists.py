# Ways to traverse a list
# Reset i for every list test here
list = [1, 2, 3, 4, 5]

# Liat comprehension
[print(i) for i in list]

# Loop with range()
length = len(list)
for i in range(length):
	print(list[i])
	
# For loop only
for i in list:
	print(i)
	
# While loop
length2 = len(list)
i = 0
while i < length:
	print(list[i])
	i += 1
	
# Enumerate
for i, val in enumerate(list):
	print(i, ",", val)
