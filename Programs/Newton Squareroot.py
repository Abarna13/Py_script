def newtonsqrt(n,howmany):
    approx = 0.5 * n
    for i in range(howmany):
        betterapprox = 0.5 * (approx + n/approx)
        approx = betterapprox
    return betterapprox
print(newtonsqrt(4,3))
print(newtonsqrt(3,3))