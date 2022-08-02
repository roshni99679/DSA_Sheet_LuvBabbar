'''Move all negative numbers to beginning and positive to end with constant extra space'''
def move_neg(arr):
    n=len(arr)
    low=0
    high=n-1
    while low<high:
        if arr[low]<0:
            low+=1
        elif arr[high]>0:                
            high-=1
        else:
            arr[low],arr[high]=arr[high],arr[low]
arr=[1, 2,  -4, -5, 2, -7, 3, 2, -6, -8, -9, 3, 2,  1]
move_neg(arr)
print(arr)
#[-9, -8, -4, -5, -6, -7, 3, 2, 2, 2, 1, 3, 2, 1]
'''Time complexity: O(N) 
Auxiliary Space: O(1)'''   
