# DATA STRUCTURES

# 1. Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.

list = [1,2,3,4,"deep","daideep",1+2j,6-2j,20.5,34.2]
print(list)

# 2. Create a list of size 5 and execute the slicing structure

l = [1,2,3,4,5]

print(l[4])
print(l[-1])

print(l[2])
print(l[0])
print(l[-2])


# 3. Create a list of given structure and run

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

print(x[5])

# Access list [1, 2, 3, 4]
print(x[5][0:5])

# Access list [600,  700]
print(x[6:8])

# Access list [100, 300, 500, 600, 800]
print(x[0::2])

# Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
print(x[::-1])

# Access list [10]
print(x[5][5][0])

# Access list [ ]
print([])


# 4. Create a list of thousand number using range and xrange and see the difference between each other.

for i in range(1,11):
    print(i)

# for i in xrange(1,11):
#     print(i)

# 5. How Tuple is beneficial as compare to the list?

# Iteration in tuple is faster than lists since tuples are immutable.
# Tuples are generally used for different Python Data Types; whereas, lists are used for similar data types.


# 6. Write a program in Python to iterate through the list of numbers in the range of 1,100
# and print the number which is divisible by 3 and a multiple of 2.

for i in range(1,101):
    if i%3==0 and i%2==0:
        print(i)


# 7. Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with their index.

word = "daideep"

# vowel = ""
#
# for i in word:
#     if i in 'aeiou':
#         vowel = vowel + i
#
# print(vowel[::-1])

index=[]
letters=[]

for ind,letter in enumerate(word):
    if letter in "aeiouAEIOU":
        index.append(ind)
        letters.append(letter)

print(index)
print(letters)


#8.Write a program in Python to iterate through the string “hello my name is abcde” and print the string which has even length of word.

s = "hello my name is abcde"
str = ""

for word in s.split():
    if len(word)%2 == 0:
        str = str + " " + word

print(str)


#9. Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.

x=[1,2,3,4,5,6,7,8,9,-1]

sum = 8
count = 0

for i in range(0, len(x)):
    for j in range(i + 1, len(x)):
        if x[i] + x[j] == sum:
            print("Pair is :", x[i],",",x[j])
            count += 1

print(count)


# 10. Write a program in Python to complete the following task:
# Create two different list as in even_list and odd_list
# Ask user to enter the number in the range of 1,50 and make sure if the entered number is even append it to the even_list and if the entered number is odd append it to the odd list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list.

a=[]
n=int(input("Enter number of elements:"))

for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)

even_list = []
odd_list = []

even = 0
odd = 0

for n in a:
    if n % 2 == 0 and even <= 5:
        even_list.append(n)
        even += 1
    elif n % 2 != 0 and odd <= 5:
        odd_list.append(n)
        odd += 1
    else:
        pass

print("Even_List :", even_list)
print(even)
print("Odd_List :", odd_list)


#11.Write a program to find out the occurrence of a specific word from an alphanumeric statement. Example: 12abcbacbaba344ab
#Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic

str = "consult5202add"

new = {}

for i in str:
    if i.isalpha():
        if i in new:
            new[i] = new[i] + 1
        else:
            new[i] = 1

print(new)

# 12. Generate and print another tuple whose values are even numbers in the given
# tuple (1,2,3,4,5,6,7,8,9,10).

t = (1,2,3,4,5,6,7,8,9,10)
l = []

for i in range(0,len(t)):
    if t[i] % 2 == 0:
        l.append(t[i])

print(tuple(l))