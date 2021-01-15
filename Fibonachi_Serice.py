terms=int(input("How many terms you want to ? :"))
n1,n2=0,1
count=0
if terms <=0:
    print("Please Provide a Positive Integer ")
elif terms == 1:
    print("Fibonachi sequence upto ",terms, ":")
    print(n1)
else:
    print("Fibonachi sequence : ")
    while count < terms:
        print(n1)
        nth=n1 + n2 

        n1= n2 
        n2 = nth
        count +=1       