'''
class Ball:
    def __init__(self, colour, size):
        self.colour = colour
        self.size = size
        self._bounceCount = 0

    def bounce(self, bounce_num):
        self._bounceCount += bounce_num
        print(f"The ball has bounced {self._bounceCount} times")


soccer_ball = Ball("Black and White", "Diameter of 12 inches")
print(soccer_ball.colour)
print(soccer_ball._bounceCount)
soccer_ball.bounce(1)
soccer_ball._bounceCount = 100
soccer_ball.bounce(1)

# Basic class wiht class variable
class Person:
    name = "John"

person1 = Person()
print(person1.name)
person1.name = "Jack"
print(person1.name)



class Person:
    
    def __init__(self, name):
        self.name = name

person1 = Person("Michelle")
print(person1.name)
person2 = Person("Sahra")
print(person2.name)
names = []
people = [Person(name) for name in names]
print(people)


class Person:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}!")

person1 = Person("Steven")
person1.greet()
person1.name = "Carl"
person1.greet()

def person_do_greet(person):
    person.name = "Bill"
    person.greet()

person_do_greet(person1)


class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.subjects = []
        self.grades = []

    def display_profile(self):
        profile = f"Student Name: {self.name} {self.surname}\n\n"
        profile += "Subject\t\t\tGrade\n"
        for subject, grade in zip(self.subjects, self.grades):
            profile += f"{subject}\t\t\t{grade}\n"
        profile += f"\nAverage: {self.get_average()}\n"
        print(profile)
        

    def get_average(self):
        return sum(self.grades)/len(self.grades)


from random import randint

student1 = Student("Jack", "Black")
student2 = Student("Claire", "Steward")
student3 = Student("Peter", "Johnson")

students = [student1, student2, student3]

# # Adding subjects and grades
subjects = ("English", "Physics", "History")
for student in students:
    #student.subjects = [subject for subject in subjects]
    for value in subjects:
        print(value)
        student.subjects.append(value)

    student.grades = [randint(60,90) for _ in range(3)]

for student in students:
    student.display_profile()


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    

rectangle1 = Rectangle(5, 9)
print(f"Area of rectangle is {rectangle1.area()}")
print(f"Perimeter of rectangle is {rectangle1.perimeter()}")

rectangle2 = Rectangle(12, 15)
print(f"Area of rectangle is {rectangle2.area()}")
print(f"Perimeter of rectangle is {rectangle2.perimeter()}")

rect1_area = rectangle1.area
print(rect1_area())
rectangle1.width = 10
print(rect1_area())


new_rectangle = Rectangle 

my_rectangle = new_rectangle(5, 8)
print(my_rectangle.area())
'''

""" ==================================
local variables and class variables
"""
class MyClass:
    def __init__(self, name):
        print(f"self => >{self}<")          # the instance in memory
        """ 
        self represents a box in memory that will contain smaller boxes of
        attributes and functions (methods).
		The label on the box will be the variable name that we declare as 
        a MyClass object. We must therefor open the bigger box before we can 
        access the attributes and methods.
        """
        print(f"name => {name}")            # the input name value
        # self.name = ''
        #print(f"self.name => {self.name}")  # the instance name value
        self.name = name
        print(f"self.name => {self.name}")


    def greet_and_update(self, new_name):
        local_variable = "I'm a local variable"
        print(f"Hello, {self.name}!")       # the instance name value
        print(local_variable)
        
        # Updating the instance variable with the new_name parameter
        self.name = new_name        # John is overwritten with Alice.

# Creating an instance of MyClass
my_instance = MyClass("John")       # Passed to name class input
"""
# my_instance = "John"  
For my_instance = "John" # This will declare my_instance as a Str object since 
this is the default for the value format "John". So to overwrite the default we
need to add the replacement class name MyClass.
"""

# Calling the greet_and_update method
my_instance.greet_and_update("Alice")     #Passed to new_name class input

# Accessing the updated name
print(f"Updated name: {my_instance.name}")

'''
""" ==================================
Access Modifiers
"""
# ================ 1. Public Variable
"""
Accessible from outside the class or module.
Part of the public interface.
"""
class MyClass:
    def __init__(self):
        self.public_variable = "Accessible Everywhere"

# Creating an object of MyClass
my_object = MyClass()

# Accessing the public variable from outside the class
print(my_object.public_variable)

# ================ 2. Protected Variable
"""
No name mangling is applied.
Conventional indication that the variable is for internal use.
Still accessible from outside the class.
"""
class MyClass:
    def __init__(self):
        self._protected_variable = "Limited Access"

# Creating an object of MyClass
my_object = MyClass()

# Accessing the protected variable from outside the class
print(my_object._protected_variable)

# ================ 3. Private Variable
"""
Name mangling is applied.
Accessible with a mangled name from outside the class.
Not a strict access control mechanism, more of a convention.
"""
class MyClass:
    def __init__(self):
        self.__private_variable = "Secret"

# Accessing the private variable from outside the class
my_object = MyClass()

# print(my_object.__private_variable)             # Note this code gives error
print(my_object._MyClass__private_variable)       # Name mangling must be applied


""" ==================================
Getter Methods:

Getter methods, are used to retrieve the values of private or protected attributes.
They provide read-only access to the internal state of an object.
The naming convention for a getter method is typically get_attribute(), ie. get_value
"""
class MyClass:
    def __init__(self):
        self._value = 42

    def get_value(self):
        return self._value

# Creating an object of MyClass
my_object = MyClass()

# Using the getter method to access the value
print(my_object.get_value())  # Output: 42

"""
Setter Methods:

Setter methods, are used to modify the values of private or protected attributes.
They provide a way to control the modification of internal state and 
enforce validation rules. The naming convention for a setter method is 
typically set_attribute().
"""
class MyClass:
    def __init__(self):
        self._value = 42

    def set_value(self, new_value):
        if new_value > 0:
            self._value = new_value

# Creating an object of MyClass
my_object = MyClass()

# Using the setter method to modify the value
my_object.set_value(50)

"""
Setter & Getter combination to run.
"""
# Getter Method:
class MyClass:
    def __init__(self):
        self._value = 42

    def get_value(self):
        return self._value
    
    def set_value(self, new_value):
        if new_value > 0:
            self._value = new_value

# Creating an object of MyClass
my_object = MyClass()

# Using the getter method to access the value
print(my_object.get_value())

# Setter Method:

# Using the setter method to modify the value
my_object.set_value(50)

# Using the getter method to access the modified value
print(my_object.get_value())

'''