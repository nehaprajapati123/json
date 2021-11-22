# Q5.Json string ko check karo ki wo complex object contain karti hai ya nahi?

import json
# Json string ko check karo ki bo complex object contain karti hai ya nahi?

dic='{"3+j":"4-i"}'
x=json.loads(dic)
for i in x:           
    for j in i:
        if j>=chr(97) and j<=chr(122):
            pass
        elif j>=chr(65) and j<=chr(90):
            pass
        
        else:
            print(i,"json string comtain complex object")
for k in x[i]:
    for l in k:
        if l>=chr(97) and l<=chr(122):
            pass
        elif l>=chr(65) and l<=chr(90):
            pass
        
        else:
            print(x[i],"json string comtain complex object")
