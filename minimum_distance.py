
"""
A non-empty zero-indexed array A consisting of N non-negative integers is given.
For elements A[P] and A[Q] that are distinct, i.e. P!= Q, their distance is
defined as:

(A[P] - A[Q]) if (A[P] - A[Q]) >= 0
(A[Q] - A[P]) if (A[P] - A[Q]) < 0

Write a function, that given a zero-indexed array A consisting of N non-negative
integers, returns the minimum distance between two distinct elements
of A.
"""



lst1 = [8, 24, 3, 20, 1, 17]
lst2 = [7, 21, 3, 42, 3, 7]



#Naive method
# n^2 runtime
def solution(array):
    min_distance = None

    for idx_p, P in enumerate(array):

        if len(array) > idx_p + 1:
            for idx_q, Q in enumerate(array[idx_p+1:]):
                distance = abs(P-Q)
                #min distance can never have the value below 0
                if distance == 0:
                    return 0
                else:
                    if min_distance is None or min_distance > distance:
                        min_distance = distance

    return min_distance



print solution(lst1)
print solution(lst2)


#TODO: O(N*log(N))
#Perform merge sort then find min distance