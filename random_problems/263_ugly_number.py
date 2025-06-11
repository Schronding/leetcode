def isUgly(n):
    if n<=0:
        return False
    prime_factors = [2,3,5]
    for factor in prime_factors:
        while n % factor == 0:
            n = n // factor
    if n == 1:
        return True
    else:
        return False

n_0=6
n_1=1
n_2=14
n_3=8

print(isUgly(n_0))
print(isUgly(n_1))
print(isUgly(n_2))
print(isUgly(n_3))
