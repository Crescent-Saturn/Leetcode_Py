def Plus_one(array):
    out = array[:]
    s = 0
    carry = 1
    for i in range(len(out))[::-1]:
        s = carry + out[i]
        carry = s // 10
        out[i] = s % 10

    if carry > 0:
        out.insert(0, carry)

    return out


a = [1, 9, 9]

print(Plus_one(a))
