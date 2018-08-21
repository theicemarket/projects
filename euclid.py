while True:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = 0
    a_1 = a
    b_1 = b

    while b != 0:
        c = a
        a = b
        b = c%b
        print(a,b)
    print("GCD(", a_1, ",",  b_1, ") = ", a, "\n", sep='')
