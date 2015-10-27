def solution(A, X):
    N = len(A)

    if N == 0:
        return -1

    left_index = 0
    right_index = N - 1

    while left_index < right_index:
        mid = (left_index + right_index) // 2
        if A[mid] == X:
            return mid
        elif A[mid] > X:
            right_index = mid - 1
        else:
            left_index = mid + 1

        if A[left_index] == X:
             return left_index


    return -1



