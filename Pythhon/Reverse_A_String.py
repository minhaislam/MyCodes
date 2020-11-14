a = 'hello'
#print(a[::-1])


i = len(a)


def ReverseString(i,a):
    strs = ''
    while i>0 :
        strs +=a[i-1]
        i-=1
    print(strs) 

ReverseString(i,a)

#Another way

def RcursiveString(i,a):
    if i==0:
        return a
    else:
        return RcursiveString(i-1,a[1:])+a[0]


print(RcursiveString(i,a)) 