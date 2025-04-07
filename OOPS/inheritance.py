#single
class A:
    def displayA(se):
        print("This is Base class...!")

class B(A):
    def displayB(se):
        print ("This is Derived class...!")    #A is Parrent class of B    

Obj=B()
Obj.displayA()
Obj.displayB()