#TASK SEVEN: CLASSES AND OBJECTS

#1.Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.

# import math
# c=50
# h=30
# value = []
#
# items = [x for x in input("Enter Value :").split(",")]
# #print(items)
#
# for d in items:
#     value.append(str((int(round(math.sqrt(2*c*float(d)/h))))))
#
# #print(value)
# print(','.join(value))

# Ds = []
# result =[]
# Dv=input("enter the value of D\n")
# Ds=Dv.split(",")
# Ds = [int(i) for i in Ds]
# i=0
# l = len(Ds)
# while(i<l):
#     Q = round(math.sqrt((2*C*Ds[i])/H))
#     result.append(Q)
#     i+=1
# print("output=",result)


#2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length * self.length

o1 = Square(5)

print(o1.area())


# 3.Create a class to find the three elements that sum to zero from a set of n real numbers.
# # Input array: [-25,-10,-7,-3,2,4,8,10]
# # Output: [[-10,2,8],[-7,-3,10]]





#4. What is the output of the following code? Explain your answer as well.

class Test:
    def __init__(self):
        self.x = 0

class Derived_Test(Test):
    def __init__(self):
        Test.__init__(self)
        self.y = 1

def main():

    b = Derived_Test()
    print(b.x, b.y)

main()

# Output:
# 0 1
# Reason: when main() function is called, object b of Derived_Test class is created which also inherits the properties of Test class.


class A:
    def __init__(self, x= 1):
        self.x = x

class der(A):
    def __init__(self,y = 2):
        super().__init__()
        self.y = y

def main():
    obj = der()
    print(obj.x, obj.y)

main()

# Output:
# 1 2
# Reason: when main() function is called, object "obj" of der class is created which also inherits the properties of A class.


class A:
    def __init__(self, x):
        self.x = x

    def count(self, x):
        self.x = self.x + 1

class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y

    def count(self):
        self.y += 1

def main():
    obj = B()
    obj.count()

    print(obj.x, obj.y)

main()

# Output:
# 3 1
# Reason: when main() function is called, object "obj" of B class is created which also inherits the properties of A class.
# and excute count() before print statement so value of y is increment by 1 (self.y += 1)


class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)

    def multiply(self, i):
        self.i = 4 * i


class B(A):
    def __init__(self):
        super().__init__()

    def multiply(self, i):
        self.i = 2 * i

obj = B()

#Output : 30
# object "obj" of B class is created autometically by calling constructer which also inherits the properties of A class.
# and by calling multiply() of B class get result (self.i = 2 * i) where i = 15 define in class A.


# 5.Create a Time class and initialize it with hours and minutes.
# Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Make a method displayTime which should print the time.
# Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.

class Time():

	def __init__(self, hours, mins):
		self.hours = hours
		self.mins = mins

	def addTime(t1, t2):
		t3 = Time(0,0)
		if t1.mins+t2.mins > 60:
			t3.hours = (t1.mins+t2.mins)/60
		t3.hours = t3.hours+t1.hours+t2.hours
		t3.mins = (t1.mins+t2.mins)-(((t1.mins+t2.mins)/60)*60)
		return t3

	def displayTime(self):
		print("Time is",self.hours,"hours and",self.mins,"minutes.")

	def displayMinute(self):
		print((self.hours*60)+self.mins)

a = Time(2,50)
b = Time(1,20)

c = Time.addTime(a,b)
c.displayTime()
c.displayMinute()


# 6. Write a Person class with an instance variable, , and a constructor that takes an integer, , as a parameter.
# The constructor must assign  to  after confirming the argument passed as  is not negative; if a negative argument is passed as ,
# the constructor should set  to  and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:
# yearPasses() should increase the  instance variable by .amIOld() should perform the following conditional actions:
# If , print You are young..
# If  and , print You are a teenager..
# Otherwise, print You are old..

class Person:

    def __init__(self,age):
        self.age = age

    def yearPasses(self):
        self.age += 1

    def amIOld(self):
        if self.age <= 0:
            self.age = 0
            print('Age is not valid, setting age to 0.')
        elif self.age < 13:
            print('You are young.')
        elif (13 <=self.age < 18):
            print('You are a teenager.')
        else:
            print('You are old.')

age = int(input("Enter Value :"))

a = Person(age)
a.amIOld()