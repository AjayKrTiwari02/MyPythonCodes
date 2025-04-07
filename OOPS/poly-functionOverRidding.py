class Aptech:
    def displayinfo(self):
        print("Welcome to Python World")
    def display(self):
        print(10+20)
class School(Aptech):
    def displayinfo(self):
        #  super().displayinfo()  # to call the function of parent which has same name as function of sub class
         print("Welcome to School")

sc=School()
sc.displayinfo()
sc.display()