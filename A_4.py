#TASK FOUR: FUNCTIONS

# 1. Write a program to reverse a string.
# Sample data: “1234abcd”
# Expected Output: “dcba4321”

str = "1234abcd"
print(str[::-1])

def reverse(str):

    new_str = ''
    index = len(str)
    while index > 0:
        new_str += str[index-1]
        index -= 1
    print(new_str)

reverse("1234abcd")


#2. Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
# Expected Output:
# No. of Upper case characters : 2
# No. of Lower case Characters : 10

def check(str):

    upper = 0
    lower = 0

    for c in str:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1

    print("No. of Upper Case : ", upper)
    print("No. of Lower Case : ", lower)

check("Daideep Patel")


#3. Create a function that takes a list and returns a new list with unique elements of the first list.

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5]))


# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence
# after sorting them alphabetically.

l = [1,2,4,3,10,3,12,5]
l.sort()
print(l)

value = input("Enter comma-seperate values :")

items=[n for n in value.split('-')]
print(items)

items.sort()

print('-'.join(items))

# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Sample input:
# Hello world
# Practice makes perfect

# Expected Output:
# HELLO WORLD
# PRACTICE MAKES PERFECT

lines = []

while True:
    l = input("Enter value")
    if l:
        lines.append(l.upper())
    else:
        break

for l in lines:
    print(l)


#6. Define a function that can receive two integral numbers in string form and compute their sum and print it in console.

str = input("Enter Two Integer Number :")
sum = 0

for c in str:
    sum = sum + int(c)

print(sum)


#7. Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.

s1 = input("Enetr Value")
s2 = input("Enter Value")

def max_str(s1,s2):

    if len(s1) > len(s2):
        print("Max. string :", s1)
    elif len(s1) < len(s2):
        print("Max. string :", s2)
    elif len(s1) == len(s2):
        print(s1)
        print(s2)

max_str(s1,s2)


#8. Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.

def square():

    l = []

    for x in range(1,21):
        l.append(x**2)

    print(tuple(l))

square()


# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers
# between 0 and limit with a label to identify the even and odd numbers. Example: If the limit is 3 , it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

def shownumbers(limit):

    for i in range(0,limit+1):

        if i % 2 == 0:
            print(i,": even")
        else:
            print(i,": odd")

shownumbers(3)


#10. Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)

Number = list(range(1,21))
print(Number)

f = list(filter(lambda i:i%2==0, Number))

print(f)


#11. Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda x: x%2 == 0, [1,2,3,4,5,6,7,8,9,10]))

print(even)

square = list(map(lambda x: x**2, even))

print(square)


#12. Write a function to compute 5/0 and use try/except to catch the exceptions

def divison(x):

    try:
        div = x/0
        print(div)
    except:
        print("Can't diivde by 0")

divison(5)


#13.Flatten the list [[1,2,3],[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
#Goal : Turn [1,2,3,4,5,6,7] to 1234567

from functools import reduce

result = reduce(lambda x,y: x+y, [[1,2,3],[4,5],[6,7,8]])

print(result)

final = reduce(lambda x,y: x+y , result)

print(final)


#14. What is the output of the following codes:

def foo():
    try:
        return 1
        #print(1)
    finally:
        return 2
        #print(2)

print(foo())

# output : 2

def a():
    try:
        f(x,4)
        #print(1)
    finally:
        print('after f')
    print('after f?')
a()

#output : NameError: name 'x' is not defined





