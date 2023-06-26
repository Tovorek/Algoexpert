 # solution
# Time complexity O(n)
# space complexity O(1)


def isMonotonic(array):
    isNI = True
    isND = True

    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            isNI = False
        if array[i] > array[i-1]:
            isND = False

    return isNI or isND
