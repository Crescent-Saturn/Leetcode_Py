def first_recu(g_str):
    counts = {}
    # out = []
    a = ""
    for i in g_str:
        if i in counts:
            a += i
        else:
            counts[i] = 1
            # else:
    return a


A = "DBCABA"
print(first_recu(A))
