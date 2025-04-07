class Caculator:
      a,b=0,0
      def __init__(s):
            print("-:This is Calculator:-\n")
            s.a=float(input("Enter the 1st value: "))
            s.b=float(input("Enter the 2nd value:"))
      def sum(s):
            s.c=s.a+s.b
            return s.c
      def multy(s):
            s.c=s.a*s.b
            return s.c
      def sub(s):
            s.c=s.a-s.b
            return s.c
      def div(s):
            s.c=s.a/s.b
            return s.c

c=Caculator()    
while(True):
      inp=int(input("""
            - Enter 1 for sum.
            - Enter 2 for multiplication.
            - Enter 3 for Subtraction.
            - Enter 4 for division.
            - Enter 0 for exit.
            """))
      if(inp==1):
            print('The output is :',c.sum())
            # break
      elif(inp==2):
            print('The output is :',c.multy())
            # break
      elif(inp==3):
            print('The output is :',c.sub())
            # break
      elif(inp==4):
            print('The output is :',c.div())
            # break
      elif(inp==0):
            print("Thank You ...")
            break
      else:
            print("Wrong Input ...")