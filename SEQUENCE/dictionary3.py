#dict function used to create dictionary[key=value]

# c=dict(name='python',fees=8000,duration="2 month")
# print(c)
# print(type(c))

d={'name:':'python',"fees:":8000,'duration:':"2 monts"}
# d.update({"fees:":10000})
# print(d)

# d.clear()
# print(d)

# d['desc']="This is Python Learning"
# print(d)
                                     # if the key is present in the dictionary then it get Updated,
                                     #Or if the key is not present in then its get created. 
d['duration:']="1month"
print(d)