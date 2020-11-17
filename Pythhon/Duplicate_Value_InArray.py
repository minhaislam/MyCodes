
Values = [23,34,56,78,90,45,75,23,75]


DuplicateList = []
NonDuplicateList =[]
for v in Values:
    if v not in NonDuplicateList:
        NonDuplicateList.append(v)
    else:
        DuplicateList.append(v)

print(DuplicateList)


    