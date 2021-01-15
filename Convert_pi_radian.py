import math
number=float(input("Enter your Value (degree) : "))
print("\nIf you want to convert (degree) type : d ")
print("If you want to convert (radian) type : r ")
asked=str(input("Enter :- "))
if asked =='d':
    deg=number/180
    print(f"{number} in Pi : {deg} π")
elif asked =='r':
    rad=number*3.17/180
    print(f"{number} in Radian : {rad} radian")
else:
    print("Input is invalid ")        