def karatsuba (x, y):
    #Size check
    if(len(str(x)) == 1 or len(str(y)) == 1 ):
        return x*y
    else:
        n = max(len(str(x)) ,len(str(y)))
        tempSize = n/2

        a = x / 10**(tempSize)
        b = x % 10**(tempSize)
        c = y / 10**(tempSize)
        d = y % 10**(tempSize)

        ac = karatsuba(a,c)
        bd = karatsuba(b,d)

        sum_ac_bd = karatsuba(a+b,c+d) - ac -bd

        product = ac * 10**(2*tempSize) + (sum_ac_bd * 10**tempSize) + bd

        return product


print("Resultant: " + str(karatsuba(222,222)))




