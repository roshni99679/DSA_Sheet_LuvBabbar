def MinOps(arr):
    n=len(arr)
    ops=0
    i,j=0,n-1
    while i<=j:
        if arr[i]==arr[j]:
            i+=1
            j-=1
        elif arr[i]>arr[j]:
            j-=1
            arr[j]+=arr[j+1]
            ops+=1
        elif arr[j]>arr[i]:
            i+=1
            arr[i]+=arr[i-1]
            ops+=1

    return ops
arr=[1,9,1]
print(MinOps(arr))
#0
'''Time Complexity: O(n)
Auxiliary Space: O(1)'''

def isPalin(n):
    rev=0
    temp=n
    while temp>0:
        rev=rev*10+temp%10
        temp=temp//10
    if rev==n:
        return True
    return False
def PalindromicArr(arr):
    n=len(arr)
    for i in range(n):
        if not isPalin(arr[i]):
            return False
    return True
    
arr=[1,8,91]
print(PalindromicArr(arr))
#False


