String = str(input("Enter A string: "))

Occurance = {}
for s in String:
    if s in Occurance:
        Occurance[s] += 1
    else:
        Occurance[s] = 1

for key,value in Occurance.items():
    if(value>1):
        print(f'Reoccuring Character {key} occured {value} times')

print(max(Occurance,key=Occurance.get))