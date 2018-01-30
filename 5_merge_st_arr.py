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
