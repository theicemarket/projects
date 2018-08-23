while True:
    b = int(input("Enter a number: "))
    p = 0
    for i in range(2, b):
        if b%i != 0:
            print(b, "!|", i)
        else:
            p = 1
            print(b, "x|", i)
            break
    if p == 1:
        print(b, "\nis composite")
    else:
        print(b, "\nis prime")
