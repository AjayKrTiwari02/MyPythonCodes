#Multilevel
class GrandFather:
    def display1(se):
        print("The Grand Father is Called ")
 
class Father(GrandFather):
    def __init__(sl ):
        print ("The Father is Called ")        

class Childe(Father):
    def display2(S):
        print ("In the School Function Of Their child ") 
    # def __init__(sl ):
    #     print('Child init')
   
Obj=Childe()
Obj.display1()
Obj.display2()