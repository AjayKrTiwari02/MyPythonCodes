class DemoClass:                               #camal case
    a=10
    def sumvalue(self):                        #argument object inside the class important(this)
        print(20+30)
        self.c=self.a*self.a
        print(self.c)
        
    def nameprint(se):  
        print("Object oriented programing")

    def __init__(sl):                      # init keyword is used to define constructor
        print("Welcome to PYTHON OOPS Concept")

    
dmo=DemoClass()                             # variable(object) =Class name                             #out side of the class
print(dmo.a)
dmo.sumvalue();
dmo.nameprint();

print("2nd object... ")
dmo2=DemoClass() 
print(dmo2.a)
dmo2.sumvalue();
dmo2.nameprint();
