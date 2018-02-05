def merge_arr(A, m, B, n):
    i = m + n - 1
    j = m - 1
    k = n - 1
    while i >= 0:
        if j >= 0 and k >= 0:
            if A[j] > B[k]:
                A[i] = A[j]
                j -= 1
            else:
                A[i] = B[k]
                k -= 1
        elif j >= 0:
            A[i] = A[j]
            j -= 1
        elif k >= 0:
            A[i] = B[k]
            k -= 1
        i -= 1


def me_sorted(A, B):
    out = []
    while A and B:
        if A[0] <= B[0]:
            out.append(A.pop(0))
        else:
            out.append(B.pop(0))
    while A:
        out.append(A.pop(0))
    while B:
        out.append(B.pop(0))

    return out


A = [1, 3, 5, 7, 9]
B = [2, 4, 6, 8, 10]

print(me_sorted(A, B))
