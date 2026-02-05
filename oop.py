# Inheritance

class Animal:
  def __init__(self, name):
    self.name = name

  def sound(self):
    return f"{self.name} makes a sound"
  
class Dog(Animal):
  bark = "Woof Woof Woof!" # class attribute

jack = Dog('Jack')
print(jack.name)
print(jack.sound())
print(jack.bark)

animal = Animal('Animal')
# print(animal.bark) # Attribute error because back belongs to Dog class