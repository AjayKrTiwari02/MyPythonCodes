#The stack is a linear data structure.
#Stores items in last-in/First-out (LIFO) or First-in/last-out(FILO) manner.
#Push=>Inserting an Elements
#pop=>Deletion An Element(Last Element)
#peek=>Display the last Element.
#Display=>Display List
l=[]
while True:
    c=int(input('''
        1 Push Elements
        2 Pop Elements
        3 Peek Elements
        4 Display Stack
        5 Exit
   ''' ))
    if c==1:
        n=input("Enter The Value");
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty list")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("Last Stack Value",l[-1])
    elif c==4:
        print("Displaying Stack:",l)

    elif c==5:
        break;            
    else:
        print("Invalid Input")