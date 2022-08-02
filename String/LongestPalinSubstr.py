'''Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 
'''
def LPS(str):
    n=len(str)
    start=end=0
    for i in range(n):
        len1=expand(str,i,i+1)
        len2=expand(str,i,i)
        length=max(len1,len2)
        if end-start<length:
            start=int(i-(length-1)//2)
            end=int(i+length//2)
    return str[start:end+1]
def expand(s,i,j):
    while i>=0 and j<len(s) and s[i]==s[j]:
        i-=1
        j+=1
    return j-i-1
str="aabbaaca"
print(LPS(str))
#aabbaa
''''''

        