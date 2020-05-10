#TASK THREE: DATA STRUCTURES

#1. Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.

list = [1,2,3,4,"deep","daideep",1+2j,6-2j,20.5,34.2]
print(list)


#2. Create a list of size 5 and execute the slicing structure

l = [1,2,3,4,5]

print(l[4])
print(l[-1])


#3. Write  a program to get the sum and multiply of all the items in a given list.

list = [1,2,3,4]

sum = 0

for i in list:
    sum = sum + i
print(sum)

mul = 1

for i in list:
    mul = mul * i
    #print(mul)
print(mul)


#4.  Find the largest and smallest number from a given list.

l = [232,3443,232,45464,1,343,-3,1999]

print(max(l))
print(min(l))


# 5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

list = [1,2,3,4,5,6,7]

new = [x for x in list if x%2 != 0]
print(new)

for i in list:
    if i%2 == 0:
        list.remove(i)
print(list)

new = []

for i in list:
    if i%2 != 0:
        new.append(i)
print(new)


#6.	Create a list of first and last 5 elements where the values are square of numbers between 1 and30 (both included).

list = []

for i in range(1,31):
    list.append(i**2)

print(list[:5])
#print(list[0:-5])
print(list[-5:])


#7. Write a program to replace the last element in a list with another list.
# Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
# Expected output: [1,3,5,7,9,2,4,6,8]

data = [[1,3,5,7,9,10],[2,4,6,8]]

# print(data[0])
# print(data[1])

data[0][5:] = data[1]

print(data[0])


num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]

num1[-1:] = num2

print(num1)


#8. Create a new dictionary by concatenating the following two dictionaries:

a={1:10,2:20}
b={3:30,4:40}
# Expected Result: {1:10,2:20,3:30,4:40}

#final = a.items()
#final = a.keys()
#final = a.values()

d = {}

for x in (a,b):
    d.update(x)

print(d)


# 9. Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
# Sample data (n=5)
# Expected Output: {1:1,2:4,3:9,4:16,5:25}

n = int(input("Enter Number: "))
d = {}

for a in range(1,n+1):
    d.update({a:a*a})

print(d)


# 10. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
# which contains every number. Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# The output should be:
# [‘34’,’67’,’55’,’33’,’12’,’98’]
# (‘34’,’67’,’55’,’33’,’12’,’98’)

values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)

print('List : ',list)
print('Tuple : ',tuple)





