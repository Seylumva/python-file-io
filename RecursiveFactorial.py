def factorial(x):
    if (x <= 1):
        return 1
    else:
        return x * factorial(x-1)

print('Factorial Calculator v1.0')
n_factorial = input('Up to which factorial should I calculate? ')
n_factorial = int(n_factorial)

print('\ni\tFactorial\n-------------')
for i in range(n_factorial+1):
    print("%d\t%d" % (i, factorial(i)))