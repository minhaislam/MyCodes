lsts = [45,67,23,54,69,76]
j = max(lsts)
k= lsts[0]

for i in range(len(lsts)):
    if lsts[i]<j and lsts[i]>k:
        k=lsts[i]
print(k)