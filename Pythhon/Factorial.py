fact = int(input())
c=1
if fact>=1:
    for i in range(1,fact+1):
        c = c*i
else:
    print(1)

print(c)