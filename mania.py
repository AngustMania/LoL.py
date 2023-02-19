class Person:
  height = 15
  age = 666
  name = "Loshara"
  is_loh = True
  
  def __init__(self, surname):
    self.surname = surname
    print(self.name)
  
me = Person("loshara")
you = Person("Lol")

print(me.surname)
print(you.surname)