def solution(array, v):
    j = 0
    new_arr = []
    for i in range(len(array)):
        if array[i] == v:
            continue
        else:
            new_arr.append(array[i])
        array[j] = array[i]
        j += 1

    return j, new_arr


a = [1, 2, 2, 3, 2, 4]

b, out = solution(a, 2)

print(b)
print(out)
