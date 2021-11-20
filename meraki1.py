# Q.1 Json data ko python object main convert karne ka program likho?.


import json
x='{"neha":"neha"}'
y=json.loads(x)
print(y)
print(type(y))
print(type(x))