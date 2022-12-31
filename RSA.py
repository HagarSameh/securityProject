def gcd(a, b):
    if a > b:
        small = b
    else:
        small = a
    x = 0
    for i in range(1, small + 1):
        if (a % i == 0) and (b % i == 0):
            x = i
    return x


class RSA:
    def RSA_encryption(self, p, q, m):
        p = int(p)
        q = int(q)
        n = p * q
        z = (p - 1) * (q - 1)
        prim = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        e = 0
        for x in prim:
            if gcd(x, z) == 1:
                e = x
                break
        c = pow(m, e) % n
        return c

    def RSA_decryption(self, p, q, c, e):
        p = int(p)
        q = int(q)
        n = p * q
        d = 0
        z = (p - 1) * (q - 1)
        for i in range(1, 20):
            x = ((z * i) + 1)
            x = x % e
            if x == 0:
                x = ((z * i) + 1) / e
                if x != e:
                    d = x
                    print("d", d)
                    break
        m = pow(c, int(d)) % n
        return m

#
# m = int(input("Enter m:"))
# p = int(input("Enter p:"))
# q = int(input("Enter q:"))
# e = 7
# c = RSA_encryption(p, q, m)
# print(c)
# print(RSA_decryption(p, q, c, e))
