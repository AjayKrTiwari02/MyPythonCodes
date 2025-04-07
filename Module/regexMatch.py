import re

a="Amit has scored 98 marks "

match=re.search("\d+",a)
# print(match)
# print(match.re)
# print(match.string)
# print(match.start())
# print(match.end())
# print(match.span())
# print(match.group())

# m=re.search("\w{2}s",a)  #Alpha numaeric 
# print(m)
# print(m.group())
# 
#[Note :Match keeps all the infomation of search]