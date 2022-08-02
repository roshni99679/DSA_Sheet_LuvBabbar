def isSubset( a1, a2, n, m):

    s = set()
    for i in range(n) :
        s.add(a1[i])
     
    p = len(s)
    for i in range(m) :
        s.add(a2[i])
     
    if (len(s) == p) :
        return "Yes"
    return "No"
arr1=[1, 5, 4, 2, 1, 3, 14, 20, 20, 98, 87, 32, 54]
arr2=[1, 5, 4, 2, 14, 20, 32, 54, 87, 98, 3, 1, 999]
print(isSubset(arr1,arr2,len(arr1),len(arr2)))
#No
'''Time Complexity: O(m+n) because we are using unordered_set and inserting in it, If we would be using a ordered set inserting would have taken log n increasing the TC to O(mlogm+nlogn); but order does not matter in this approach.
Auxiliary Space: O(n+m)'''

#using hashing
def subset(p,q):
    a=len(p)
    b=len(q)
    hash=[]#or hash=set()
    for i in range(a):
        hash.append(p[i])#or hash.add(p[i])
    for j in range(b):
        if q[j] in hash:
            continue
        else:
            return False
    return True
arr1=[1, 5, 4, 2, 1, 3, 14, 20, 20, 98, 87, 32, 54]
arr2=[1, 5, 4, 2, 14, 20, 32, 54, 87, 98, 3, 1, 20]
print(subset(arr1,arr2))
#True
'''Time Complexity: O(n*logn)
Auxiliary Space: O(n)'''