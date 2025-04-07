f=open('C:\\FileHandling\\XYZ1.txt','w')        # file is opened 
f.write("hello  , my name is spidy")     # will write this file .

# tasks=['gym ','chapter3 ','water plants ','dogs walk']
# f.writelines(tasks)                      #will write all strings in the file.

# tasks=['My  ','Name  ','Is ','Groot']
# f.writelines(tasks) 
print("File Write Sucssesful..!")
f.close()   



#A File pointer tells the current position in the file where reading or writing will take place
#it's like a bookmark.it's left at the spot we left & the continuation is done further from there.