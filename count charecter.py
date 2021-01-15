def number_list(l):
    even_list=[]
    odd_list=[]
    for i in l:
        if i%2==0:
           even_list.append(i)
        else:
           odd_list.append(i) 
    output=[f'even={even_list},odd={odd_list}']
    return output    
number=[1,2,44,659,5,9,56,96,56,5,56,56,5]
print(number)
print(number_list(number))             
     