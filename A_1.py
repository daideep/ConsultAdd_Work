TASK ONE: NUMBERS AND VARIABLES

1.Create three variables in a single line and assign different values to them and make sure their data types are invited different. 
Like one is int, another one is float and last one is string.

  a,b,c = 1,2.5,"daideepb

  print(a)
  print(b)
  print(c)

2. Create a variable of value type complex and swap it with another variable whose value is an integer.

  x = 2 + 5j 
  y = 10

  x,y = y,x

  print(x)
  print(y) 

3. Swap two numbers using third variable as result name and do the same task without using any third variable.

  a = 1
  b = 2

  result = a
    a = b
    b = result

   print(a)
   print(b)

  a,b = b,a

  print(a)
  print(b)


4. Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.

  x = eval(raw_input('Enter Value (python 2.x)' : ))

  print(x)

  y = eval(input('Enter Value (python 3.x)' : ))  
 
  print(y)


5. Write a program to complete the task given below: Ask user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
   Use z for adding 30 into it and print the final result by using variable result.

   x = int(input('Enter Numbers in between 1-10' : ))
   y = int(input('Enter Numbers in between 1-10' : ))

   z = x + y

   print(z)   

   final = z + 30

   print(final)


6. Write a program to check the data type of the entered values. HINT: Printed output should say -  The input value data type is : int/float/string/etc

 result = input("Enter Value : " )
  
 print("The Input Value Data Type is " , type(result))


7. Create Variable using CamelCase, LadderCase and UPPERCASE. (Refer:   https://capitalizemytitle.com/camel-case/)

   CamelCase = "FedEx"
   UPPERCASE = "FEDEX"


8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value. 
If Yes then Why?

    Yes - its overright

     a = 'two'
     a = 2
     print(a)
