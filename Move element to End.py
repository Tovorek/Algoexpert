# solution
# Time complexity O(n)

def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1

    while i < j:
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
            j -= 1
        else:
            i += 1

    return array
