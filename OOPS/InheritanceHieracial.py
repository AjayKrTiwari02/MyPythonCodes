
class Mobile:
    def calling(self):
        print("Mobile gives the facilities of Calling.. ")
    def message(self):
        print("Mobile gives the facilities of Messagging..")    

class Samsung(Mobile):
     def __init__(s ):
         print("Samsung galaxy S20 \nFeel the New Glaxy ")

class Nokia(Mobile):
     def __init__(n ):
         print("Nokia-1110 \nConnecting People")
print("-----------------NokiaStore---------------------")
nok=Nokia()
nok.calling();
nok.message();

print("-----------------SamsungStore-------------------")
sam=Samsung()
sam.calling();
sam.message();