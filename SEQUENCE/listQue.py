#The queue is Linear data structure.
#Stores items in first in First Out(FIFO) manner.
#Exit from front.(ticket Line)
#Enqueue:Adds an items to the Queue.
#Dequeue:Removes an item from the queue.
#Front:Get the front items from queue.
#Rear:Get the last item from queue.
y=[]
while True:
    c=int(input('''
        1 Push Elements
        2 Pop Fist Elements
        3 Front Elements
        4 Last Elements
        5 Display Queue.
        6 Exit
   ''' ))
    if c==1:
        n=input("Enter The Value :");
        y.append(n)
        print(y)
    elif c==2:
        if len(y)==0:
            print("Empty Queue")
        else:
            del y[0]
            print(y)
    elif c==3:
        if len(y)==0:
            print("Empty Queue")
        else:
            print("First Queue Value :",y[0])
    elif c==4:
        if len(y)==0:
            print("Empty Queue")
        else:
            print("last Queue Value :",y[-1])
    elif c==5:
        print("Display Queue :",y)      

    elif c==6:
        print('Thankyou')
        break; 
    else:
        print("Invalid Option")