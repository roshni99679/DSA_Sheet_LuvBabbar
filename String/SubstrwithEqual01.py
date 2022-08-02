'''Split the binary string into substrings with equal number of 0s and 1s'''

'''
Given a binary string str of length N, the task is to find the maximum count of consecutive substrings str can be divided into such that all the substrings are balanced i.e. they have equal number of 0s and 1s. If it is not possible to split str satisfying the conditions then print -1.
Example: 
 

Input: str = “0100110101” 
Output: 4 
The required substrings are “01”, “0011”, “01” and “01”.
Input: str = “0111100010” 
Output: 3 

Input: str = “0000000000” 

Output: -1'''


def fn(str):
    c0=0
    c1=0
    c=0
    for i in range(len(str)):
        if str[i]=="0":
            c0+=1
        else:
            c1+=1
        if c0==c1:
            c+=1
    if c0!=c1:
        return -1
    return c
print(fn("0000000000"))

'''Time complexity: O(N) where N is the length of string 
Space Complexity: O(1)'''