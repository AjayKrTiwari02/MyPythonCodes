#SpecialSqueces:
import re

a="harry potter"
b="harry potter@12345"
# match=re.search(r'\Ahar',a)          #Matches if the String  begins with given characters
# match=re.search(r'\Apot',a) 
# print(match)

# match=re.search(r'r\b',a)          #Matches if the word begins or end with the given character \b(string),(string)\b
# print(match)

# match=re.search(r'\bha',a) 
# print(match)                    #\B it opposite of the \b i.e the string should not start or end with the given regex..

# match=re.search(r'ha\B',a)   
# print(match)

# match=re.search(r'r\B',a)   
# print(match)

# match=re.findall(r'\d',b) 
# print(match)

# match=re.findall(r'\D',b) 
# print(match)

# match=re.findall(r'\s',b) 
# print(match)

# match=re.findall(r'\S',b) 
# print(match)

# match=re.findall(r'\w',b) 
# print(match)

# match=re.findall(r'\W',b) 
# print(match)
# match=re.search(r'5\Z',b) 
# print(match)  
           # Matches if the string ends with the given regex..