import math
while True:
    w = int(input("\nEncrypt: 0 \nDecrypt: 1\n"))

    if w == 0:  #encrypts
        z = int(input("\nASCII string (utf-8): 0 \nInteger: 1\n"))
        if z == 0:
            user = input("Enter string: \n")
            s = user.encode('utf-8').strip()
            plaintext = int.from_bytes(s, byteorder='little')
        if z == 1:
            plaintext = int(input(("\nEnter integer: \n")))
        modulus = int(input("\nEnter a modulus: "))
        encrypt = int(input("Enter an encyption key: "))
        cyphertext = pow(plaintext, encrypt, modulus)
        print("Encrypted message:", cyphertext)

    if w==1:    #decypts
        cyphertext = int(input("Enter cyphetext: \n"))
        encrypt = int(input("Enter an encyption key: "))
        prime_1 = int(input("Enter first private key: \n"))
        prime_2 = int(input("Enter second private key: \n"))
        modulus = prime_1*prime_2

        a = encrypt     #calculates linear solution
        b = (prime_1 -1)*(prime_2 - 1)
        c = 0
        q = 0
        n_1 = []

        while b != 0:   #calculates GCD
            q = a//b    #quotent
            c = a       #saves the value of a before its assignment to b
            a = b       #reassigns b to a for next iteration
            b = c%b     #remainder calculated and assigned to b for next iteration
            n_1.append(q)   #adds quotients to list

        n = n_1[::-1]   #reverses list
        i = 2           #index
        x_1=1           #seeds
        y_1=n[1]
        x_2=0
        y_2=0

        while i < len(n):   #reverses gcd
            y = n[i]
            x_2 = (-1)*y_1
            y_2 = (x_1+y*(y_1))*(-1)
            x_1 = x_2
            y_1 = y_2
            i = i + 1

        decrypt = x_2
        k = 0
        while decrypt < 0:
            k = k + 1
            decrypt = decrypt + k*(prime_1-1)*(prime_2-1)
        print("Decryption key:", decrypt)
        plaintext = pow(cyphertext, decrypt, modulus)
        print("Plaintext:", plaintext)
        z = int(input("Convert to ASCII string: 0\n"))
        if z == 0:
            n = plaintext.bit_length()
            m = plaintext.to_bytes(n, byteorder='little')
            p = m.decode("utf-8")
            print(p)
