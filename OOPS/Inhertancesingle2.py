#single
class A:
    def displayA(se,a,b):
        se.c=a+b
        print("Base class output:",se.c)
       
class B(A):
    def displayB(se,d,e):
        se.f=d*e
        print("Answer :"+str(se.f))
        print ("This is Derived class...!")    #A is Parrent class of B    

Obj=B()
Obj.displayA(35,15)
Obj.displayB(10,12.2)