class Animal:
 def animal(self):
    print("This is Class for animal")
class Mammals(Animal):
  def mammals(se):
    print("Mammals are the part of Animal Kingdom")  
class Herbivores:
  def herb(self):
    print("The Animal Which depends on green food or herbs are part of this Family") 

class CoW(Mammals,Herbivores):
  def __init__(se):
     print('The Cow is a Herbivore Mammal')
class Horse(Mammals,Herbivores):
  def __init__(se):
     print('The Horse is a Herbivore Mammal')
     
print("------------------CoW------------------")
cw=CoW()
cw.animal();
cw.mammals();
cw.herb();
print("-----------------Horse-------------------")
h=Horse()
h.animal();
h.mammals();
h.herb();
