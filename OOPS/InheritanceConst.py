#single
class A:
    def displayA(se):
        print("This is Base class...!")
    def __init__(self):
          print("I am constructor of Parent")

class B(A):
    def displayB(se):
        print ("This is Derived class...!")    #A is Parrent class of B  
    def __init__(self):
          print("I am constructor of Child")  

Obj=B()
Obj.displayA()
Obj.displayB()