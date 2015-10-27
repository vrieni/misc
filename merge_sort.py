unsorted_list = [5, 2, 4, 3, 8, 9, 7]

def mergeSort(alist):
    print ("Splitting", alist)

    if len(alist) > 1:
        mid = len(alist)//2
        left_half = alist[:mid]
        right_half = alist[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        left_index=0
        right_index=0
        main_index=0


        while left_index < len(left_half) and right_index < len(right_half):

            if left_half[left_index]<right_half[right_index]:
                alist[main_index] = left_half[left_index]
                left_index = left_index + 1
            else:
                alist[main_index] = right_half[right_index]
                right_index = right_index + 1

            main_index = main_index + 1

        while left_index < len(left_half):
            alist[main_index]=left_half[left_index]
            left_index = left_index + 1
            main_index = main_index + 1

        while right_index < len(right_half):
            alist[main_index] = right_half[right_index]
            right_index = right_index + 1
            main_index = main_index + 1