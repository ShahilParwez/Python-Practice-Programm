name=input("Enter your name")
temp=" "
i=0
while i<len(name):
    if name[i] not in temp:
        temp+=name[i]
        i+=1
        print(f"{name[i]}:{name.count(name[i])}")
       
