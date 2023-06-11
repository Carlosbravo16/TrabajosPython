num=[1,2,3,4]
print(num)
print(num[2])
print([-1])
num[1]=9
print(num)
for p in num :
    print(p)
    for i, e in enumerate(num):
        print(i,e)
dato=["jazz", "salsa", "rock"]
for l1, l2 in zip(num, dato):
    print(l1,l2)
    print(len(dato))
