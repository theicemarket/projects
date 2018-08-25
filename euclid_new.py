a = int(input("Enter a number"))
b = int(input("Enter another"))

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
    return(a_list, b_list, quotent_list, remainder_list)

def linear_solution(a,b):
    coef_lists = gcd(a,b)
    for i in coef_lists:
        i.reverse()
    x_1=1
    y_1=coef_lists[2][1]    #2nd member in 3rd (quotent) list
    for i in range(2, len(coef_lists[2])):       #recursion on a*x_1-b*x_2 = r
        y = coef_lists[2][i]
        x_2 = -y_1
        y_2 = -x_1-y*(y_1)
        x_1 = x_2
        y_1 = y_2
    return(x_1,-y_1)
linear_solution(a,b)
