def f(n):
    k = 0
    a = []
    while n != 1:
        if n % 2 != 0:
            n = (3 * n) + 1
        else:
            n = n / 2
        k += 1
        a.append(n)
    for N in a:
        print(N)
    return ("n: " + str(n) + " Steps:" + str(k))


print(f(77))
