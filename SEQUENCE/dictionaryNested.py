#Nested dictionary means puting a dictionary inside another dictionary.
#this is a collection of a dictionaries in to single dictionary.

cousre={
    "php":{'duration':"2months","Fees":"3000"},
    'Python':{'duration':"3months","Fees":"5000"},
    'java':{'duration':"4months","Fees":"6000"},
    'C++':{'duration':"1months","Fees":"4500"}
}
# print(cousre)
# print(cousre['php'])
# print(cousre['php']['Fees'])  #Fetching Data using key values 

# for k,v in cousre.items():
    #  print(k)
    #  print(k,v)
    #  print(k,v["duration"],v["Fees"])

##Update
# cousre['java']["Fees"]=20000
# for k,v in cousre.items():
#   print(k,v["duration"],v["Fees"])

# del cousre['java']
# for k,v in cousre.items():
#   print(k,v["duration"],v["Fees"])


