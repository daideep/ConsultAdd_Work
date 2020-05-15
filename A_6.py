#TASK SIX: HIGHER ORDER FUNCTIONS, GENERATORS, LIST COMPREHENSION AND DECORATOR

#1.	Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7.
# Make sure to use only higher order function.

l = [i for i in range(1,50) if i%3 != 0 and i%7 == 0]

print(l)

#2. Write a program in Python to  multiple the element of list by itself using traditional function and pass the function
# to map to complete the operation.

num = [1,2,3,4,5]

def muliply(num):
    return num*num

final = list(map(muliply,num))

print(final)

# def mul(num):
#     new = 1
#     for i in num:
#         new = new *i
#     return new
#
# print(mul(num))

# from functools import reduce
#
# mul = reduce(lambda x,y: x*y, num)
# print(mul)


#3.Write a program to Python find out the character in a string which is uppercase using list comprehension.

str = "ConsultAdd TraininG"

# upper = []
# for c in str:
#     if c.isupper():
#         upper.append(c)
#     else:
#         pass

# print(upper)

upper = [c for c in str if c.isupper()]

print(','.join(upper))


#4. Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects.
# The dictionary should maps the students with their respective subjects. Let’s see how to do this using for loops and
# dictionary comprehension. HINT-Use Zip function also

Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']

d = {k:v for k,v in zip(Student,capital)}

print(d)


#5. 	Learn More about Yield, next and Generators




