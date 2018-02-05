# Merge sort algo from Wiki
import timeit


def merge_sort(A):
    if len(A) <= 1:
        return A

    mid = len(A) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])

    out = []
    while left and right:
        if left[0] <= right[0]:
            out.append(left.pop(0))
        else:
            out.append(right.pop(0))

    while left:
        out.append(left.pop(0))
    while right:
        out.append(right.pop(0))

    return out


A = [4, 5, 7, 9, 7, 5, 1, 0, 7, -2, 3, -99, 6]
start = timeit.default_timer()
print(merge_sort(A))
stop = timeit.default_timer()
print(stop - start)
