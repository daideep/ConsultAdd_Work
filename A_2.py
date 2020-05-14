#OPERATORS AND DECISION MAKING STATEMENT

# 1. Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “c” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.

n = int(input('Enter Value :' ))

if n%3 == 0 and n%5 ==0:
    print('Consultadd Python Training')
elif n%3 == 0:
    print('Consultadd')
elif n%5 == 0:
    print('c')

# 2. 	Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If USer Enter 4 - Multiplication
# If User Enter 5 - Average
# Ask user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
# Ask user to enter two more numbers as first and second2 for calculating the average as soon as user choose an option 5.
# At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
# NOTE: At a time user can perform one action at a time.

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Average")

choice = int(input("Enter choice(1/2/3/4/5): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
   print(num1,"+",num2,"=", num1 + num2)
elif choice == 2:
   print(num1,"-",num2,"=", num1 - num2)
elif choice == 3:
   print(num1,"*",num2,"=", num1 * num2)
elif choice == 4:
   print(num1,"/",num2,"=", num1 / num2)
elif choice == 5:
    print("Avg. of", num1, "and", num2, ":", (num1+num2)/2)
else:
   print("Negative")


#3. Write a program in Python to implement the given flowchart:

a =10
b =20
c =30

avg = (a+b+c)/3
print('avg is', avg)

if avg > a and avg > b and avg>c:
    print("Avg is higher than a,b,c")
elif avg > a and avg > b:
    print("Avg is higher than a,b")
elif avg > a and avg > c:
    print("Avg is higher than a,c")
elif avg > b and avg > c:
    print("Avg is higher than b,c")
elif avg > a:
    print("Avg is just higher than a")
elif avg > b:
    print("Avg is just higher than b")
elif avg > c:
    print("Avg is just higher than c")

# 4. 	Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”

n = int(input('Enter Number : '))

while n < 0:
    break
print("Its over")

while n > 0:
    continue
print("Good Going")


#5. Write a program in Python which will find all such numbers which are divisible  by 7 but are not a multiple of 5, between 2000 and 3200.

for i in range(2000,3201):
    if i % 7 == 0 and i % 5 == 0:
        print(i)


#6. What is the output of the following code examples?

x=123

for i in x:
    print(i)

# Ans : TypeError: 'int' object is not iterable

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("error")

#   Ans = 0
#         1
#         2

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Ans : 0
#       1
#       2
#       3
#       4

# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
# Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement

for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')

# 8.  Write a program that accepts a string as an input from user and calculate the number of digits and letters.
#      Expected output: consul12
#      Letters 6
#      Digits 2

s = input("Input a string :")
d=l=0
for i in s:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
    else:
        pass

print("Letters", l)
print("Digits", d)


# 9. Read the two parts of the question below:
# - Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever.
# - Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing. The program stops if the user guesses the correct number or answers “no”. ( The program continues as long as a user has not answered “no” and has not guessed the correct number)

number = input("Guess the lucky number :")
while number != 5:
    print("That is not the lucky number")
    number = input("Guess the lucky number :")
    if number == 5:
        print('Lucky Number')

number = -1
again = "yes"
while number != 5 and again != "no":
    number = input("Guess the lucky number: ")
    if number != 5:
        print("That is not the lucky number")
        again = input("Would you like to guess again? ")


#10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as

counter = 1
while counter <= 5:
    number = input("Guess the " + str(counter) + ". number ")
    if number != 5:
        print("Try again.")
    else:
        print("Good guess!")
    counter = counter + 1
else:
    print("Game over")

