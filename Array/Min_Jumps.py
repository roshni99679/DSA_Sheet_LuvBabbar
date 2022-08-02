'''Minimum number of jumps

Given an array of N integers arr[] where each element represents the max number of steps that can be made forward from that element. Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.

Note: Return -1 if you can't reach the end of the array.


Example 1:

Input:
N = 11 
arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} 
Output: 3 
Explanation: 
First jump from 1st element to 2nd 
element with value 3. Now, from here 
we jump to 5th element with value 9, 
and from here we will jump to the last. 
Example 2:

Input :
N = 6
arr = {1, 4, 3, 2, 6, 7}
Output: 2 
Explanation: 
First we jump from the 1st to 2nd element 
and then jump to the last element.

Your task:
You don't need to read input or print anything. Your task is to complete function minJumps() which takes the array arr and it's size N as input parameters and returns the minimum number of jumps. If not possible return -1.


Expected Time Complexity: O(N)
Expected Space Complexity: O(1)


Constraints:
1 ≤ N ≤ 107
0 ≤ arri ≤ 107'''

#youtube link: https://www.youtube.com/watch?v=Yrw3MNh_368&list=PLzffTJx5aHaRMfFodb4O5yyi6uSA4Q3E0&index=10
def minJumps(arr):

    n=len(arr)
    position=0
    destination=0
    jump=0

    #loop till 2nd last ele bcoz we dont have to make jumps on reaching last ele
    for i in range(n-1):

        #find max of prev destination val and current destination val (current ele + index of ele)
        destination=max(destination,arr[i]+i)           

        #if cannot reach destination return -1
        if i>=destination:
            return -1
        #update position and jump only when you get a better position to reach final destination
        if position==i:
            position=destination
            jump+=1
    #return min jumps taken        
    return jump

arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJumps(arr))
#3
'''Time Complexity: O(N)
Space Complexity: O(1)'''


