# try:
#     l=[6,7,8,9,6]
#     i=int(input("Enter the index:"))
#     print (l[i])
# except:
#     print(" Bhul Hoe gache thik kore nao...!")

# finally:
#     print("I am Always Executed..!")
# print("I am Always Executed..!")



def func1():
    try:
         l=[6,7,8,9,6]
         i=int(input("Enter the index:"))
         print (l[i])
        #  print("I am Always Executed..!")
         return 1
    except:
        print(" Bhul Hoe gache thik kore nao...!")
        # print("I am Always Executed..!")
        return 0
        

    finally:
        print("I am Always Executed..!")
 


x=func1()
print(x)
    