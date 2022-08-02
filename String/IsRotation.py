'''A Program to check if strings are rotations of each other or not

Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1? 
(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)

Algorithm: areRotations(str1, str2)

1. Create a temp string and store concatenation of str1 to
   str1 in temp.
                      temp = str1.str1
2. If str2 is a substring of temp then str1 and str2 are 
   rotations of each other.

Example:                 
                 str1 = "ABACD"
                 str2 = "CDABA"

 temp = str1.str1 = "ABACDABACD"
 Since str2 is a substring of temp, str1 and str2 are 
 rotations of each other.'''



def rot(s1,s2):
    n1=len(s1)
    n2=len(s2)
    if n1!=n2:
        return False
    temp=s1+s1
    if temp.count(s2)>0:
        return True
    return False
print(rot("hello","lohel"))
#True

def rota(p,q):
    if len(p)!=len(q):
        return False
    temp=p+p
    if q in temp:
        return True
    return False
print(rota("hello","lohel"))
#True
'''Time Complexity will be O(n*n), where n is the length of the string.
Auxiliary Space: O(n)'''