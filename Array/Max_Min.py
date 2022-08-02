'''Maximum and minimum of an array using minimum number of comparisons'''

class pair:
    def __init__(self):
        self.min=0
        self.max=0
def Min_Max(arr):
    n=len(arr)
    minmax=pair()
    if n==1:
        minmax.min=arr[0]
        minmax.max-arr[0]
    else:
        if arr[0]>arr[1]:
            minmax.min=arr[1]
            minmax.max=arr[0]
        else:
            minmax.min=arr[0]
            minmax.max=arr[1]
        for i in range(2,n):
            if arr[i]<minmax.min:
                minmax.min=arr[i]
            if arr[i]>minmax.max:
                minmax.max=arr[i]
    return minmax
arr=[1,2,4,3,6,8,90,0,7,7]
minmax=Min_Max(arr)
print("Minimum ele is ",minmax.min)
print("Minimum ele is ",minmax.max)
# Minimum ele is  0
# Minimum ele is  90

'''Time Complexity: O(n)

Auxiliary Space: O(1) as no extra space was needed.

In this method, the total number of comparisons is 1 + 2(n-2) in the worst case and 1 + n – 2 in the best case. 
In the above implementation, the worst case occurs when elements are sorted in descending order and the best case occurs when elements are sorted in ascending order.'''


def MinMax(arr):
    min=0
    max=0
    if len(arr)==1:
        min=arr[0]
        max=arr[0]
    else:
        if arr[0]>arr[1]:
            min=arr[1]
            max=arr[0]
        else:
            min=arr[0]
            max=arr[1]
        for i in range(2,len(arr)):
            if arr[i]<min:
                min=arr[i]
            if arr[i]>max:
                max=arr[i]
    return min,max
# min,max=Min_Max([1,2,4,3,6,8,90,0,7,7])
# print("Minimum ele is ",min)
# print("Minimum ele is ",max)

#    min,max=Min_Max([1,2,4,3,6,8,90,0,7,7])
# TypeError: cannot unpack non-iterable pair object