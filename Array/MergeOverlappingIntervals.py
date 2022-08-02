
'''Merge Overlapping Intervals

Given a set of time intervals in any order, merge all overlapping intervals into one and output the result which should have only mutually exclusive intervals.

Example:

Input: Intervals = {{1,3},{2,4},{6,8},{9,10}}
Output: {{1, 4}, {6, 8}, {9, 10}}
Explanation: Given intervals: [1,3],[2,4],[6,8],[9,10], we have only two overlapping intervals here,[1,3] and [2,4]. Therefore we will merge these two and return [1,4],[6,8], [9,10].

Input: Intervals = {{6,8},{1,9},{2,4},{4,7}}
Output: {{1, 9}} '''

#youtube link: https://www.youtube.com/watch?v=RGr2RuH6iH4
def mergeIntervals(arr):
    n=len(arr)
    arr.sort(key=lambda x:x[0])
    index=0
    for i in range(1,n):
        if arr[index][1]>=arr[i][0]:
            arr[index][1]=max(arr[index][1],arr[i][1])
        else:
            index+=1
            arr[index]=arr[i]
    for i in range(index+1):
        print(arr[i],end=" ")
arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
mergeIntervals(arr)
#[1, 9]

'''Time Complexity: O(n*log(n))
Auxiliary Space Complexity: O(1)'''
 
