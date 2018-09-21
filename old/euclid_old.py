while True:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = 0
    q = 0
    output_1 = a     #saves a and b for the final print message
    output_2 = b
    n_1 = []

#calculates GCD
    while b != 0:
        q = a//b    #quotent
        c = a       #saves the value of a before its assignment to b
        a = b       #reassigns b to a for next iteration
        b = c%b     #remainder calculated and assigned to b for next iteration
        n_1.append(q)   #adds quotients to list
        print(c, "=", a, "(", q, ")+", b, sep='')    #a = b*(a//b)+a%b

    print("\nGCD(", output_1, ",",  output_2, ")=", a, sep='')

#calculates linear solution
    n = n_1[::-1]   #reverses list
    x=1
    y=n[1]
    for i in range(2,len(n)):
        x,y = -y, -x-n[i]*y
    print(output_1, "(", x, ")+", output_2, "(", -y, ")=", a, "\n", sep='')
