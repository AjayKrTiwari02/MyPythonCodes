import re
a="charlie chaplin  coa  chaaaaaaa   and Baaaaa Baaaaaa black sheep"
b="niit123@gmail.com"
c="Hello"
d="xyz,yz,xyyyz,xyzz,xyyz,xxzzy,zyyyyz,xxyyyzz"

# match=re.search(r"\.",b)   #(regularparameter,string):(starting index,ending endex)
# print(match)

# match=re.search(r"[@]",b)   #(regularparameter,string):(starting index,ending endex)
# print(match)

# match=re.findall(r"[l]",c)   #prints number of charecters in diff. []:ex['l','l']
# print(match)

# match=re.search(r"^He",c)      #none / index span 
# print(match)

# match=re.search(r"com$",b)       
# print(match)

# match=re.findall(r"c.a",a)     # serching with the starting & ending charecter 
# print(match)

# match=re.findall(r"cha|Ba",a)      #cha or ba
# match=re.search(r"cha|Ba",a)       # first index value ...
# print(match)

# match=re.findall(r"a?a",a)        # any number of (with respect to index 0,1)
# print(match)

# match=re.findall(r"a*a",a)
# print(match)

# match=re.findall(r"xy+z",d)      # in order of xy with any .....
# print(match)


# match=re.findall(r"y{2,4}",d)   #number of repeatation between 2 to 4
# print(match)

# match=re.findall(r"(x|y)yz",d)   #starting value x or y and ending with yz
# print(match)
