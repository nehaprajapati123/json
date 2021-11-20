# Q5.Json string ko check karo ki wo complex object contain karti hai ya nahi?
dic='{"nam@e:"neh1a,"khf:"jhyf","ghf":"juyf"}'
for i in dic:
    for j in i:
        if j<="a" and j>="z":
            pass
        else:
            print(j,"complex is contain")
    for k in dic[i]:
        if k<="a" and k>="z":
            pass
        else:
            print(k,"complex is contain")

