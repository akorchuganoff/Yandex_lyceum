def f(a, b, x):
    if b*x-a != 0:
        return (a*x-b)/(b*x-a)
    else:
        return 0

a = 100
b = 100
for b in range(1, 1000):
    print(f(a, b, f(a, b, f(a, b, f(a, b, 1212121212121)))))