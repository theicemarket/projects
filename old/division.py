n = int(input("Enter polynomial degree: \n"))
root = int(input("Polynomial root: \n"))
list = []
list_1 = []
i =1

for i in range(0,n+1):
    print("Enter ", i, "th coef:", sep='')
    k = int(input())
    list.append(k)
print(list)

print("Polynomial divided by x-", root," =: ", sep='')
list.reverse()
k = list[0]

for i in range(0,n):
    list_1.append(k)
    k = root*k+list[i+1]
print(list_1)
