# class is a blueprint for creating objects
# object is an instance of a class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person = Person("John", 20)
person.say_hello()

# __init__ is a special method that is called when an object is created
# self is a reference to the current object
# name and age are the arguments that are passed to the __init__ method

# attributes are the variables that are associated with the class

# methods are the functions that are associated with the class

# class keyword is used to define a class
# class name should be in PascalCase



### getattr() => used to get the value of an attribute of an object

 # -> syntax: getattr(object, attribute_name, default_value)
 # -> default_value is optional
 # -> if the attribute is not found, it will return the default value
 # -> if the default value is not provided, it will raise an AttributeError

print(getattr(person, "name")) # John
print(getattr(person, "age")) # 20
print(getattr(person, "gender", "unknown")) # unknown

# getattr(person, "skills") # AttributeError: 'Person' object has no attribute 'skills'

### setattr() => used to set the value of an attribute of an object