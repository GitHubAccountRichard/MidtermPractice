#Conditionals: Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
#Modify the program to also check if the number is even or odd.

Number2 = float(input("Please enter a Number"))
if Number2 > 0:
    print("The number is positive")
elif Number2 < 0:
    print("The number is negative")
else:
    print("The number is zero")
if Number2 % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


#Print all numbers from 1 to 100 that are divisible by both 3 and 5.
#Write a program that calculates the factorial of a number using a for loop.
#Implement a guessing game where the user must guess a randomly generated number between 1 and 10.

for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)

def factorial(n):
    """
    This function returns the factorial of a number.
    :param n: the number to calculate the factorial for
    :return: result of the factorial number
    """
    result = 1
    for n in range(1, n + 1):
        result *= n
    return result
n = int(input("Please enter a number "))
print(f"the factorial of your number is {factorial(n)}")


import random
random_number = random.randint(1, 10)
Guess = input("Guess a number between 1 and 10")
if random_number == int(Guess):
    print("Your guess is correct")
else :
    print("Your guess is incorrect")


#Functions

#Implement a function sum_of_squares(n) that calculates the sum of squares of all numbers up to n.

def sum_of_squares(n):
    """
    This function returns the sum of the squares of numbers between 1 and n.
    :param n: input of the number up to which the sum of squares should be calculated
    :return: the total sum of the squares between 1 and n
    """
    sum = 0
    for i in range(0, n+1):
        sum += i ** 2
    return sum
n = int(input("Please enter a number for which you want the total sum squares "))
print(f"The totla sum squares for {n} is {sum_of_squares(n)}")


#1Write a function that takes a string and returns True if it is a palindrome.
#2Given a string, count the number of vowels in it.
#3Extract all the email addresses from a given text file.

#1

def palindrome(string):
    """
    This function checks if the input string is a palindrome
    :param n: input string to check if it is a palindrome
    :return: True or False depending on if the input string is a palindrome
    """
    lower_string = string.lower()
    if lower_string == lower_string[::-1]:
        return True
    else:
        return False
print(palindrome("Maam"))


#2

def vowels(string):
    return sum(string.lower().count(v) for v in "aeiou")

print(vowels("Maam"))

#3

emails = open("emails.txt", "r")
print(emails.read())
emails.close()


fp = open("text.txt", "r") # "r" stands for reading the file
print(fp.read()) # read() method gets the entire file content
fp.close() # this is good practice

# same thing using the context manager
# this is more pythonic
with open("text.txt", "r") as f:
    print(f.read())
#no need to close

# read the file line by line
print("now we print it line by line ")
with open("text.txt", "r") as f:
    for line in f: # f is iterable and we get each individual line
        print(line, end="")




