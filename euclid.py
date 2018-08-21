while True:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = 0   #see while loop
    a_1 = a #saves inputs for the final print message
    b_1 = b

    while b != 0:
        c = a   #saves the value of a before its assignment to b
        a = b
        b = c%b
        print(a,b)
    print("GCD(", a_1, ",",  b_1, ") = ", a, "\n", sep='')
