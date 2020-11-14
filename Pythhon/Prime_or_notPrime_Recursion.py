def prime(value,i = 2):
    if value<= 2:
        return 'Prime' if (value == 2) else 'Not prime'
    elif value % i == 0:
        return 'NotPrime'
    elif i*i > value:
        return 'Prime'
    
    return prime(value, i+1)
        


value = int(input())

print(prime(value,2))