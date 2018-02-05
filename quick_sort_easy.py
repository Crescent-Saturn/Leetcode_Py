# Quick Sort for Python
import timeit


def quickSort(A):
    if len(A) < 1:
        return A

    pivot = A[-1]
    left = []
    right = []
    base = []

    for i in A:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            base.append(i)

    left = quickSort(left)
    right = quickSort(right)

    return left + base + right


A = [3, 7, 8, 5, 2, 1, 9, 5, 4]
start = timeit.default_timer()
print(quickSort(A))
stop = timeit.default_timer()
print(stop - start)
