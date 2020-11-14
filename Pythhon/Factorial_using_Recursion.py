fact = int(input())

def factorial(fact):
    if fact == 1:
        return fact
    elif fact <=0:
        return 'NA'
    else:
        return fact*factorial(fact-1)

print(factorial(fact))