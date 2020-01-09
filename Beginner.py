print("Hello, World!");

#Variables and Literals
x = 15
print("x = ", x)
x = "Words"
print('x = ', x)
#Both types of quotes work?

#This creates a double newlne. Print itself makes one
print("\n")


#Operators
a = 10
b = 7

#Add and Subtract
print('a + b = ', a + b)
print('a - b = ', a - b)

#Multiply and Divide
print('a * b = ', a * b)
print('a / b = ', a / b)

#Floor Division
print('a // b = ', a // b)

#Remainder
print('a % b = ', a % b)

#Exponent
print('a ** b = ', a ** b)

#Shortcuts
x = 9
x += 6  #x += 6 -> x = x + 6
print(x)
#x is 15 here now because of previous line
x /= 3  #x /= 3 -> x = x / 3
print(x)
# -= , *= , //= , **= work too

#Input from User
#Use the input() function
inputString = input('Enter a sentence: ')
print('The inputted string is: ', inputString)

#Line Comment
"""Multiline
    Comment"""
'''Another
    Multiline
    Comment'''
