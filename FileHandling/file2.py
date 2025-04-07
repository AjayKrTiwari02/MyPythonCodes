# append mode
file1 = open("c:\\FileHandling\\Abc.txt", "a")  #append mode 

# writing newline character
file1.write("\n")
file1.write("Today\t")

# without newline character
file1.write("Tomorrow")
print("File Written Successfully..")
file1.close()



             

