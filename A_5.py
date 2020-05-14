l = [1, 2, 3, 3, 4, 5, 2, 1]

new = []

for i in l:
    if i not in new:
        new.append(i)
    else:
        break

print(new)


#ValueError: invalid literal for int() with base 10: 'ds'

try:
    x = int(input("Enter Number : "))
    y = int(input("Enter Number : "))
except:
    print("Enter Interger Value")
else:
    print("Sum :", x + y)
finally:
    print("End of Current Code")

print('--------------------')

a = 2
b = 4
print(a+b)


#TASK FIVE: FILE HANDLING AND EXCEPTION HANDLING

#1.Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError

try:
    x = "hello"
    if len(x) = 5:
except SyntaxError:
    print("Invalid Syntax , : is require")
finally:
    print(x)


# 2. Write a program in Python to allow user to open a file by using argv module.
# If the entered name is incorrect throw an exception and ask them to enter the name again.
# Make sure to use read only mode.

import sys
file_name = sys.argv[0]
text = []

try:
    f = open(file_name, 'r')
    text = f.readlines()
    f.close()
except IOError:
    print('cannot open', file_name)

if text:
    print(text[15])


# 3. Write a program to handle an error if the user entered the number more than four digits it should return
# “Please length is too short/long !!! Please provide only four digits”

while True:
    try:
        n = int(input("Enter Value : "))
        if n > 9999:
            print("Please length is too long !!! Please provide only four digits")
        else:
            print(n)
            break
    except:
        print("Please Enter Interger Value")


        
#4. Create a login page backend to ask user to enter the UserEmail and password.
# Make sure to ask Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.

count=0

while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')

    if password=='1010' and username=='daideep':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1

        
        
#6. Read any file using Python File handling concept and return only the even length string from the doc.txt file.

f = open("doc.txt","w")

f.write("Hello I am a file.\nWhere you need to return the data string \nWhich is of even length \n"
        "Make sure you return the content in \nThe same link as it is present")

f.close()

file = open("doc.txt","r")

str = file.read()
#print(list)

for i in str.split():
    if len(i) % 2 == 0:
        print(i)

file.close()






