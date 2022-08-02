'''Given an array which consists of only 0, 1 and 2 sort the array without using any sorting algorithm'''

def mySort(arr):
    n=len(arr)
    count0,count1,count2=0,0,0
    for i in range(n):
        if arr[i]==0:
            count0+=1
        elif arr[i]==1:
            count1+=1
        else:
            count2+=1
    i=0
    while count0:
        arr[i]=0
        i+=1
        count0-=1
    while count1:
        arr[i]=1
        i+=1
        count1-=1
    while count2:
        arr[i]=2
        i+=1
        count2-=1
    for i in range(n):
        print(arr[i],end=" ")
mySort([0,2,1,2,1,0,0,1,2,1,2,2,0,0])
#0 0 0 0 0 1 1 1 1 2 2 2 2 2


