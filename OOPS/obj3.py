##obj3.py
class Cube:                      
    
    def area(self ,le,br):                   #argument object inside the class important(this)
        self.ar=le*br
        print("The area of the cube :"+str(self.ar))

    def volume(s,l,b,h):
        s.volume=l*b*h
        print("The volume is :"+str(s.volume))    


    def __init__(sl ):                   # Parameterized Constructer
        print("Calculate Cube Details")
       


    
C=Cube()                            # variable(object) =Class name 
print("1st Cube :")
C.area(5,6)
C.volume(5,6,8)                     

C1=Cube()
print("2nd Cube :")
C1.area(11,12)
C1.volume(11,12,8) 

C2=Cube()
print("3rd Cube :")
C2.area(2,3)
C2.volume(2,3,5) 