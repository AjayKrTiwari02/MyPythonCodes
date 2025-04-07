class Student:
    __name="Ronaldo"   #its by default class level act as private ...
    name="Messi"
   


obj=Student
# print(obj.__name)    # Can't be used directly out side the class...  
print(obj.name)

