# From Quick Sort in Wikipedia


def quicksort(lst, lo, hi):
    if lo < hi:
        p = partition(lst, lo, hi)
        quicksort(lst, lo, p)
        quicksort(lst, p + 1, hi)
    return lst


def partition(lst, lo, hi):
    pivot = lst[hi - 1]
    i = lo - 1
    for j in range(lo, hi):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    if lst[hi - 1] < lst[i + 1]:
        lst[i + 1], lst[hi - 1] = lst[hi - 1], lst[i + 1]
    return i + 1


A = [12, 4, 5, 6, 7, 3, 1, 15]
print(quicksort(A, 0, len(A) - 1))
