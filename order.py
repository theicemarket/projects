import math

#returns smallest d s.t. number^d congruent to 1 mod modulus.
def get_order(number,modulus):  #order of a number mod modulus
        i = 1
        while pow(number, i, modulus) != 1:
            i = i + 1
        return(i)

def get_primitives(modulus):        #finds primitive roots given a modulus
        for i in range(1,modulus):
                if get_order(i,modulus) == modulus -1:
                    print(i)

def powers_upto_modulus(number,modulus):      #calculates the various powers of number mod modulus
        for i in range(1,modulus):
            print(number, "^", i, " = ", pow(number, i, modulus), " (mod ", modulus, ")", sep="")

def numbers_with_order(order, modulus):         #generates numbers with a given order mod modulus
        for i in range(1,modulus+1):
            if pow(i, order, modulus) == 1 and get_order(i,modulus) == order:
                print(i, "^", order, " = ", 1, " (mod ", modulus, ")", sep="")

def solutions(k, modulus):        #finds solutions to x^k congruent to 1 mod modulus
        for i in range(1,modulus+1):
            if pow(i, k, modulus) == 1:
                print(i, "^", k, " = ", 1, " (mod ", modulus, ")", sep="")

def prime_gen(user_range):
    prime_list = []
    for b in range(2, user_range):
        p = 0
        for i in range(2, b):
            if b%i == 0:
                p = 1
                break
        if p == 0:
            prime_list.append(b)
    print(prime_list)

def find_order(k,p): #finds numbers with order k mod p
    list = []
    for i in range(1,p+1):
        if pow(i, k, p) == 1 and get_order(i,p) == k:
            #print(i, "^", order, " = ", 1, " (mod ", modulus, ")", sep="")
            list.append(i)
    print(list)
    return(list)


def gcd_search(k,p,m):    #finds the gcd(a,i) if k = ord of a^i mod p
    a_list = find_order(k,p)    #numbers (a) with order k mod p
    #for i in range(1,len(a_list)):
    #    a = a_list[i]
    a = a_list[m]
    if a != 1:
        for i in range(1,k+1):      #checks gcd of powers of a with i
            if k == get_order(a**i,p):
                print(math.gcd(a,i))
