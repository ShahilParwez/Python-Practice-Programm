def coun_prime(num):
    primes=[2]
    x=3
    if num<2:
        return 0
    while x<=num:
        for y in primes:
            if x%y==0:
                break 
            else:
             primes.append(x)
             x+=2
    print(primes)
    return len(primes)
print(coun_prime(10))                   