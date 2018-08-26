import random
import math

#calculates gcd + linear coefficents
def gcd(a,b):
    a_list =[]
    b_list =[]
    remainder_list = []
    quotent_list = []
    while b!=0:
        a_list.append(a)
        b_list.append(b)
        c = b
        b = a%b
        remainder_list.append(b)
        q = a//c
        quotent_list.append(q)
        a = c
    return(a_list, b_list, quotent_list, remainder_list,c)    #gcd = c= gcd(a,b)[4]

#finds x,y s.t. ax+by=gcd(a,b)
def linear_solution(a,b,c):
    coef_lists = gcd(a,b)
    for i in coef_lists[:-1]:   #removes int c from list
        i.reverse()

    #seeds
    x_1=1
    y_1=coef_lists[2][1] # = gcd(a,b)[4] = actual gcd(a,b)

    #recursion on a-by = r
    #into c*x-d*y = gcd(a,b) where d = r
    #using quotent list calculted from gcd function
    for i in range(2, len(coef_lists[2])):
        y = coef_lists[2][i]
        x_2 = -y_1
        y_2 = -x_1-y*y_1
        x_1 = x_2
        y_1 = y_2
    #solution is (x,y) = (x_1, -y_1)

    if c == 1:
        #forces x_1 to be a positive solution to a(x_1)+(b)(y*)=gcd(a,b)
        k = 0
        while x_1 < 0:
            k = k + 1
            x_1 = x_1 + k*b
    return(x_1,-y_1)

def prime_gen():
    x = 10**140
    y = 10**200
    i = 0
    pseu_primes = []
    while i != 2:
        a = random.randint(x,y)
        b = 1361
        if pow(b,a-1,a) == 1:
            pseu_primes.append(a)
            i = i+1
    return(pseu_primes)

#keygen
def keygen():
    z = int(input("Generate all keys: 0\nFind decryption key and modulus given (e,p,q): 1\n"))

    if z == 0:
        while z == 0:
            print("Generaring pseudoprimes, please wait: ")
            pseu_primes = prime_gen()
            prime_1 = pseu_primes[0]
            prime_2 = pseu_primes[1]
            print("Prime 1:", prime_1, "\n\nPrime 2:", prime_2)
            z = int(input("If values are prime, return 1. \nOtherwise return 0.\n "))+1

        encrypt = 65537
        if gcd(encrypt, (prime_1 -1)*(prime_2 - 1))[4] != 1:    #checks that gcd(e,totient(modulus)) = 1
            print("WHAT??")

        decrypt = linear_solution(encrypt,(prime_1 -1)*(prime_2 - 1), 1)[0]
        print("\nEncryption key: ", encrypt)
        print("\nDecryption key: ", decrypt, "\n")
        print("Modulus: ", prime_1*prime_2, "\n")

    if z == 1:
        encrypt = int(input("\nEnter an encyption key: "))
        prime_1 = int(input("\nEnter first private key: \n"))
        prime_2 = int(input("\nEnter second private key: \n"))
        decrypt = linear_solution(encrypt,(prime_1 -1)*(prime_2 - 1), 1)[0]

#encryption
def encryption():
    z = int(input("\nASCII string (utf-8): 0 \nInteger: 1\n"))

    if z == 0:
        user = input("\nEnter string: \n")
        s = user.encode('utf-8').strip()
        plaintext = int.from_bytes(s, byteorder='little')

    if z == 1:
        plaintext = int(input(("\nEnter integer: \n")))

    modulus = int(input("\nEnter a modulus: "))
    encrypt = int(input("\nEnter an encyption key: "))
    cyphertext = pow(plaintext, encrypt, modulus)
    print("\nEncrypted message:", cyphertext)

#decryption
def decryption():
    cyphertext = int(input("\nEnter cyphetext: \n"))
    modulus = int(input("Enter modulus: \n"))
    decrypt = int(input("Enter decryption key\n"))

    #plaintext = cypertext ^ (dycryption key) mod modulus
    plaintext = pow(cyphertext, decrypt, modulus)
    print("Plaintext:", plaintext)

    #converts integer plaintext to ASCII string using UTF-8
    z = int(input("\nConvert to ASCII string: 0\n"))
    if z == 0:
        n = plaintext.bit_length()
        m = plaintext.to_bytes(n, byteorder='little')
        p = m.decode("utf-8")
        print(p)

#main select
def main():
    print("\n//RSA encryption, decryption, and keygen//")
    w = int(input("Encrypt: 0 \nDecrypt: 1\nKeygen:  2\n\n"))
    if w == 0:  #encrypts
        encryption()
    if w == 1:
        decryption()
    if w == 2:
        keygen()

while True:
    main()
