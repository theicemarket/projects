while True:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = 0
    d = 0
    q = 0
    output_1 = a     #saves a and b for the final print message
    output_2 = b
    n_1 = []

#calculates GCD
    while b != 0:
        q = a//b    #quotent
        c = a       #saves the value of a before its assignment to b
        d = b       #saves value of b before its assignment to c%b
        a = b       #reassigns b to a for next iteration
        b = c%b     #remainder calculated and assigned to b for next iteration
        n_1.append(q)   #adds quotients to list
        print(c, "=", d, "(", q, ")+", b, sep='')    #a = b*(a//b)+a%b

    print("\nGCD(", output_1, ",",  output_2, ")=", a, sep='')

#calculates linear solution
    n = n_1[::-1]   #reverses list
    i = 2
    x_1=1
    y_1=n[1]
    x_2=0
    y_2=0
    print(n)
    while i < len(n):
        y = n[i]
        x_2 = (-1)*y_1
        y_2 = (x_1+y*(y_1))*(-1)
        x_1 = x_2
        y_1 = y_2
        i = i + 1
    print(output_1, "(", x_2, ")+", output_2, "(", -y_2, ")=", a, "\n", sep='')
