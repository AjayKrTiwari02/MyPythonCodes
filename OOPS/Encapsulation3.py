class Student:
    __name="Sachin"
    def __init__(self):
        print(self.__name)
        self.__displayinfo()
    def __displayinfo(self):
        print("Welcome to NIIT")

obj=Student()


# obj.__displayinfo() # We have to call it in constructor....
