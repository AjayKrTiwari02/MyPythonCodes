#Overloading Function :
class Area:
    def find_area(self,x=None,y=None):

        if(x!=None and y!=None):
            print(x*y)
        elif(x!=None):
            print(x*x)
        elif(y!=None):
            print(y*y)
        else:
            print("Nothing")
ar=Area()
ar.find_area()
ar.find_area(10)
ar.find_area(None,20)
ar.find_area(10,20)
ar.find_area(" Hellow ",3)
ar.find_area(5," ## ")
# ar.find_area(" Hellow ") ##error

    