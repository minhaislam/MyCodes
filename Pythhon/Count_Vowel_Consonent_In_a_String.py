a = 'Hellol'
vowel = ['a','e','i','o','u','A','E','I','O','U']
vl = 0
cn = 0
c = 0
for i in a:
    for v in vowel:
        if(v == i):
            vl +=1
            
print(f'Number of Vowels {vl}')
print(f'Number of Consonents {len(a)-vl}')

