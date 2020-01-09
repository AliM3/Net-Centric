# 1. Write a program that prints ‘Hello World’ to the screen.
print("Hello, World!")

# 2. Write a program that asks the user for their name and greets them with their name.
name = input("What is your name?\n")
print("Hello", name)

# 3. Modify the previous program such that only the users Alice and Bob are greeted with their names.
specialUser = input("Who are you?\n")
if specialUser == 'Alice' or specialUser == 'Bob':
    print('Hey', specialUser)
else:
    print('Begone', specialUser, '!')

# 4. Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
n = input("Give me a number: ")
i = 1
sum = 0
for i in range(0, int(n) + 1):
    sum = sum + i
print(sum)

# 5. Modify the previous program such that only multiples of three or five are considered in the sum,
# e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
n = input("Give me a number: ")
i = 0
sum = 0
while i <= n:
    if i % 3 == 0 or i % 5 == 0 :
        sum += i
    i += 1
print(sum)

# 6. Write a program that asks the user for a number n and gives them the possibility to choose between computing the
# sum and computing the product of 1,…,n.
n = input("Give me a number\n")
compute = input("Do you want the product or sum of 1 to your number?\n")
i = 1
product = 1
sum = 0
if compute == "product":
    while i <= int(n):
        product = i * product
        i += 1
    print("The product is ", product)
elif compute == "sum":
    for i in range(0, int(n) + 1):
        sum = sum + i
    print("The sum is ", sum)
else:
    print("Invalid Input")

# 7. Write function that reverses a list, preferably in place.
def reverseList(list):
    list.reverse()
    return list

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list)
print(reverseList(list))

# 8. Write a function that tests whether a string is a palindrome
def isPalindrome(str):
    revStr = str[::-1]
    if str == revStr:
        return print("It is a palindrome")
    return print("It is not a palindrome")


testStr = "stats"
isPalindrome(testStr)
