# Writing & Reading JSON File:
# we have to use file handling read & write operations...

import json

# file=open("sample2.json","r")   # The mods are read:"r",write:"w"
# x=file.read()                   # We have to convertstring to python object
# data=json.loads(x)              # JSON==Python conversion
# print(data)
# print(type(data))
# for a in data:                  #To fetch the keys of a JASON dictionary
#     print(a) 
#     print(data[a]) 



# file=open("sampleX5.json","w")
# x=file.write('''{"1":"Sumit",
#                  "2":"Raju",
#                  "3":"Farhan",
#                  "4":"Rancho",
#                  "5":"Virus"
#                  "6":"mm" }''') 
# print("File Conversion to JSON Successfull")

file=open("sampleNew20.json","w")
x=file.write("""{"URL":"www.training.com",
      "name":"AptechLearning",
      "fees":"12000"}""")
print("File Conversion to JSON Successfull")








    # 1 for a in ldata:
    # print(a["people"]) 

    # y=[{"cname":"Python","Fees":"12000","Duration":"2Months"}]
    # x=file.write(str(y)) 