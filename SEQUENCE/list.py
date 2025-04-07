# list is a non-primitive data type , its also a collection of items.

marks=[95,98,97,"maths",12, 'Java',14.78,16]
# print(marks)


maths=[96,87,97,89,76]
# print(maths[0])
# print(maths[1])
# print(maths[-1])               #reverse index will count from very last 
# print(maths[-3])
# print(maths[-4])              # error: maths index out of range..

###SLICING:
a=['a']
# print(type(a))

marks=[95,98,97,"maths",12, 'Java',14.78,16]
# print(type(marks))
l=[1,2,3,4,5,6,7]

# print(marks[1:5])             # when we want to print spacific number then {[startingindex:less than the index value]}
# print(marks[3:7])
# print(marks[3:]) 

# print(l[0:7:3])                 #(l[1stvalue index:condition:increment])
# print(l[0::2])

# print(l[-1::-1])                #reverse


# for score in marks:        # here score is the variable to varry and print the values of marks / like i in java..
#    print(score)