x=int(input("Enter the size of the list : "))

sub=[]
record=[]

for i in range(0,x):
    sub.append(input())
    sub.append(input())
    sub.append(input())
    record.append(sub)
    sub=[]
print(record)