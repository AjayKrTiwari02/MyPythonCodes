try:
    num=int(input("Enter an index value:"))

    a=[4,5,6,8,9,10]
    print(a[num])

except ValueError as e1:
    print("Number entered is not an integer..")
    # print(e1)
except IndexError as e:
    print("value at index not found.")
    # print(e)