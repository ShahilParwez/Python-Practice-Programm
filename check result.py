name=(input("enter your name:"))
print(f"Hello {name}")
age=int(input("Enter your age:"))
Hindi=int(input("Enter your Hindi marks:"))     
English=int(input("Enter your English marks:"))     
Maths=int(input("Enter your Maths marks:"))     
Chemistry=int(input("Enter your Chemistry marks:"))     
Physics=int(input("Enter your Physics marks:"))     
Enviroment=int(input("Enter your Enviroment marks:"))     
sum=Hindi+English+Maths+Chemistry+Physics+Enviroment
print(f"Total number is:{sum}")
per=float(sum/6)
print(f"Percentage is:{per}")
if per<=33:
    print("Fail=ja ghar kisi ko mat batana")
elif per>33 and per<45:
    print("Third division :pass ho gya kisis kam ka nhi")
elif per>45 and per<60:
    print("Second division :kosis kar or achha karne ki")
elif per>60 and per<75:
    print("First division :good mere ladke")  
elif per>75 and per<85:
    print("good first division :verry good")
elif per>85 and per<100:
    print("exellent :mera beta..")              
else:
    print("mat dikh samne.... ")    


        


