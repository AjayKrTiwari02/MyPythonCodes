class Person:
    def __init__(self, name:str):
        # Constructor with only name
        self.name = name
        self.age = 20
        
    def __init__(self, name:str, age:int):
        # Constructor with name and age. Overwrites above implementation.
        self.name = name
        self.age = age
        
    def __str__(self):
        # Returns a string representation of the object.
        return "Person(Name: {}, Age: {})".format(self.name, self.age)
    
if __name__ == '__main__':
    obj1 = Person("Alice",40)
    print(obj1)
    # Throws error
    obj2 = Person("Alice")

    #Note:[ Python does not support constructor overloading. If you try to overload the constructor,
    #  the last implementation will be executed each time. Any previous implementation will
    #  be over-written by the latest one. Example Consider the following example. In class Person
    #  two __init__() functions are provided. However, the implementation of the first __init__()
    #  function is over-written by the later implementation.]

