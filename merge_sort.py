def merge_sort(A):
    if len(A) < 2:
        return A
    mid = len(A) // 2
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])
    return merge(L, R)


def merge(L, R):
    out = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            out.append(L[i])
            i += 1
        else:
            out.append(R[j])
            j += 1
    out += L[i:]
    out += R[j:]
    return out


A = [4, 5, 7, 9, 7, 5, 1, 0, 7, -2, 3, -99, 6]
print(merge_sort(A))
