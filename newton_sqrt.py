import math


def newton_sqrt(y):
    # x**2 - y =0
    # f' = 2x
    # x_n1 = x_n - (x**2 - y)/2x
    # x_n1 = x_n - x_n/2 + y/2x_n
    # x_n1 = x_n/2 + y/2x_n
    x = y / 2
    while True:
        x1 = x / 2 + y / (2 * x)
        if math.fabs(x1 - x) < 1e-5:
            break
        x = x1
    return x1


print(newton_sqrt(5))
print(math.sqrt(5))
