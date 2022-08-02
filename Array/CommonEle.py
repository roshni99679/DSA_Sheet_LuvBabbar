'''








































Common elements
EasyAccuracy: 38.69%Submissions: 100k+Points: 2
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?

Example 1:

Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function commonElements() which take the 3 arrays A[], B[], C[] and their respective sizes n1, n2 and n3 as inputs and returns an array containing the common element present in all the 3 arrays in sorted order. 
If there are no such elements return an empty array. In this case the output will be printed as -1.

 

Expected Time Complexity: O(n1 + n2 + n3)
Expected Auxiliary Space: O(n1 + n2 + n3)

 

Constraints:
1 <= n1, n2, n3 <= 10^5
The array elements can be both positive or negative integers.'''

def commonElements (A, B, C, n1, n2, n3):
        # your code here
        a=[]
        i=j=k=0
        prev=-9999
        while i<n1 and j<n2 and k<n3:
            if A[i]==B[j]and B[j]==C[k] and A[i]!=prev:
                    a.append(A[i])
                    prev=A[i]
                    i+=1
                    j+=1
                    k+=1
                    
            elif A[i]<B[j]:
                i+=1
            elif B[j]<C[k]:
                j+=1
            else:
                k+=1
        for i in range(len(a)):
            print(a[i],end=" ")
            
ar1 = [9,9,9]
ar2 = [9,9,9]
ar3 = [9,9,9]
n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)
 
print("Common Elements are ")
commonElements(ar1, ar2, ar3, n1, n2, n3)
#9
        

        

class Solution():
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here

        a=[]
        i=j=k=0
        prev=-9999
        while i<n1 and j<n2 and k<n3:
            if A[i]==B[j]and B[j]==C[k] and A[i]!=prev:
                    a.append(A[i])
                    prev=A[i]
                    i+=1
                    j+=1
                    k+=1
                    
            elif A[i]<B[j]:
                i+=1
            elif B[j]<C[k]:
                j+=1
            else:
                k+=1
        
        
        return a
ar1 = [9,9,9]
ar2 = [9,9,9]
ar3 = [9,9,9]
n1=len(ar1)
n2=len(ar2)
n3=len(ar3)
ans=Solution()
res=ans.commonElements(ar1,ar2,ar3,n1,n2,n3)
for i in range(len(res)):
    print(res[i],end=" ")