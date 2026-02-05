# Inheritance

class Animal:
  def __init__(self, name):
    self.name = name

  def sound(self):
    return f"{self.name} makes a sound"
  
class Dog(Animal):
  bark = "Woof Woof Woof!" # class attribute
  #overriding sound method with super()
  # comment out below sound method code and see the result
  def sound(self):
    base = super().sound()
    return f'{base}, then {self.name} bark {self.bark}' 
jack = Dog('Jack')
print(jack.name)
print(jack.sound())
print(jack.bark)

animal = Animal('Animal')
# print(animal.bark) # Attribute error because back belongs to Dog class