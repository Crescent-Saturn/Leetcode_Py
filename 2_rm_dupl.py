def rm_dupl(array):
    j = 0
    num = 0
    for i in range(1, len(array)):
        if array[j] == array[i]:
            num += 1
            if num < 2:
                j += 1
                array[j] = array[i]
        else:
            j += 1
            array[j] = array[i]
            num = 0

    return j + 1


a = [1, 1, 1, 2, 2, 3]

print(rm_dupl(a))
