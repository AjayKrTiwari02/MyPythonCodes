class DemoClass:                             #camal case
    a=10
    def sumvalue(self ,i):                   #argument object inside the class important(this)
        self.c=self.a*i
        print(self.c)

    def arguement(s,a,b):
        print(a+b)    


    def __init__(sl ,c,d):                   # Parameterized Constructer
        print("The Multiplication is:")
        sl.e=12
        print(c*d+sl.e)        #e is local variable need reference
                                # c,d local pram. dont need reference


print("------1st object--------")   
dmo=DemoClass(5,6)
dmo.sumvalue(22); 
dmo.arguement(10,15);



print("-----2nd object---------")                        # variable(object) =Class name 
dmo2=DemoClass(10,2)
dmo2.sumvalue(12);
dmo2.arguement(130,15);