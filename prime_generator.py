file = open("prime_list.txt","w")
m = int(input("Enter a range: "))
for b in range(2, m):
    p = 0
    for i in range(2, b):
        if b%i == 0:
            p = 1
            break
    if p == 0:
        print(b)
        file.write(str(b) + "\n")
