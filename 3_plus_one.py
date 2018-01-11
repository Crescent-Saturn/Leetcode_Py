def Plus_one(array):
    out = array[:]
    if out[-1] != 9:
        out[-1] += 1
    else:
        for i in range(len(out))[::-1]:
            if out[i] == 9:
                out[i] = 0
                continue
            out[i] += 1

        if out[0] == 0:
            out.insert(0, 1)

    return out


a = [9, 9, 9]

print(Plus_one(a))
