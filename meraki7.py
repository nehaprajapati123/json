# Text.txt:-  
#  Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29
# Output:-

# Json_file.json:-


# {
#     “Name”: “Abhishek”,
#     “Designation”: “CEO of      navgurukul”,
#     “Gender”:”male”,
#     “Age”: “29”
#     }

dic={
    "Name":"Abhishek",
    "Designation": "CEO of Navgurukul",
    "genter":"male",
    "age": "29"
}
import json
x=json.dumps(dic)
print(x)

import json
for i in dic:
    y=open("files.txt","a")
    json.dump(i,y)
    json.dump(dic[i],y,)
y.close()

