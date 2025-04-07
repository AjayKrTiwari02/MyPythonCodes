# copy file:-

from shutil import copyfile
# copyfile("C:\\FileHandling\\XYZ1.txt", "C:\\FileHandling\\DELL.txt")

# or


# sFile = input("Enter the Name of Source File: ")
# tFile = input("Enter the Name of Target File: ")

# fileHandle = open(sFile, "r")
# texts = fileHandle.readlines()     #rb-> read mode ,wb-> write mode
# fileHandle.close()                  #r-> normal text file read                         

# fileHandle = open(tFile, "w")     #w-> normal text file write
# for s in texts:
#     fileHandle.write(s)
# fileHandle.close()

# print("\nFile Copied Successfully!")