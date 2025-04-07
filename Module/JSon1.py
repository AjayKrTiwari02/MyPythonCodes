#Converting JSON to Python Object:
# If you have a JSON string,you can parse it by using the json.load()method.

import json

#Some json

# x='{"cname":"Python","Fees":"12000","Duration":"2Months"}'
x='[{"cname":"Python","Fees":"12000","Duration":"2Months"}]' #Dictionary inside a list 
# print(type(x))

## parse x:

y=json.loads(x)
print(type(y))
print(y)

#The result will be Python dictionary..

# for a in y:
#     print(y[a])
