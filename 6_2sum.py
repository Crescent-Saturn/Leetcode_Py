def twoSum(array, number):
    dict = {}
    for i in range(len(array)):
        x = array[i]
        if number - x in dict:
            print(dict)
            return (dict[number - x] + 1, i + 1)
        dict[x] = i


A = [2, 7, 11, 17]
b = 12

print(twoSum(A, b))
