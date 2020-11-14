number = int(input())


flag = 0


for num in range(2,number//2):
    if(number % num == 0):
       flag = 1

if flag == 1:
    print('not Prime')
else:
    print('Prime')