Numbers = [23,11,56,78,90,83,87,1,2]

for index in range(0, len(Numbers)):
    if Numbers[index] <= 2:
        if Numbers[index] == 2:
            print(f'{Numbers[index]} is Prime')
        else:
            print(f'{Numbers[index]} is NotPrime')
    else:        
        for i in range(2,Numbers[index]):       
            if Numbers[index] % i == 0 :
                print(f'{Numbers[index]} is Not Prime')
                break
            elif (i*i) > Numbers[index] :
                print(f'{Numbers[index]} isPrime')
                break
