#Car Rental System:
#   Display Available cars
#   Request a Car for Rent (1000 Rs->1qty)
#   Exit

class CarShop:

    def __init__(s,stock):
        s.stock=stock
    def displayCar(s):
        print("Total Cars :-",s.stock)
    def rentForCars(s,q):
        if q<=0:
            print("Enter the Positive value  or Greater  than Zero")
        elif q>s.stock:
            print("Enter the value less than stock")
        else:
            s.stock=s.stock-q
            print("Total Prices :",q*1000)
            print("Total Cars : ",s.stock)

while True:
    ob=CarShop(120)
    uc=int(input(
        '''
        1. Display Stock
        2. Rent a Car
        3. Exit

        Enter Your Choice:-
                '''
     ) )
    
    if uc==1:
        ob.displayCar()

    elif uc==2:
        n=int(input("Enter the Number of cars:--"))
        ob.rentForCars(n)
    elif uc==3:
        break
    else:
        print("Invalid Choice.....!")


    

