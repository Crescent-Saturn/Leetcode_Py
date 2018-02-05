def twoMult(array, product):
    dict = {}
    for i in range(len(array)):
        x = array[i]
        if product // x in dict:
            return (dict[product // x] + 1, i + 1)
        dict[x] = i


A = [2, 4, 1, 6, 5, 40, -1]
M = 30

print(twoMult(A, M))
