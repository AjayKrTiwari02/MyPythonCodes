# An Object variable should not always be directly asscible.
# the method can ensure the correct values are set. if an incorrect value is set, the method can return an error.
#GETTER SETTER METHOD:

class Student:
    def __init__(self) :      #when self is defined its instaciated [becomes object level] & can be used outside the class
        self.__name=""        # Private variable cant be used directly.....//blanck value..
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name

obj=Student()

obj.setname("Testing")
# n=obj.getname()
# print(n)
# or
print(obj.getname())

