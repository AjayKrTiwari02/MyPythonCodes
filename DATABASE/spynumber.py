
# SPY NUMBER :
# Example 1: 1421
# Sum of digits ==> 1+4+2+1 = 8
# Product of digits ==> 1*4*2*1 = 8

num=int(input("Enter your number "))
sum=0
product=1
num1 = num
 
while(num>0):
    d=num%10
    sum=sum+d
    product=product*d
    num=num//10
 
if(sum==product):
    print(" is a Spy number!")
else:
    print(" is not a Spy number!")