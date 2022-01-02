salary = input()
a = float(salary)
b = 0
if a > 1000000:
    b = (0.04 * a)
    print(b)
elif a > 500000 and a <= 1000000:
    b = (0.02 * a)
    print(int(b))
elif a <= 500000:
    b = (a * 0)
    print(int(b))
