
# solution for smallest difference
# Solution #1
# Time complexity O(n log n)
# This solution is more efficient

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    pointer1 = 0
    pointer2 = 0
    minDiff = float('inf')
    output = []
    
    while pointer1 < len(arrayOne) and pointer2 < len(arrayTwo):
        currentDiff = abs(arrayOne[pointer1] - arrayTwo[pointer2])
        
        if currentDiff < minDiff:
            minDiff = currentDiff
            output = [arrayOne[pointer1], arrayTwo[pointer2]]
        
        if arrayOne[pointer1] < arrayTwo[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1
    
    return output

#-------------------------------------------------------------------------------------------

# Solution#2
# Time complexity 
''' However, it's worth noting that this implementation has a time complexity of O(n^2) due to the nested loops, 
where n is the length of the arrays. 
This means the code may become inefficient for large input arrays. If efficiency is a concern, 
using a more optimized algorithm such as sorting the arrays and employing 
two pointers would yield better performance with a time complexity of O(n log n). ''' 


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    min = float('inf')
    output=[]
    for i in arrayOne:
        for j in arrayTwo:
            if abs(i-j) < min:
                min = abs(i-j)
                output = [i,j]
    return output
