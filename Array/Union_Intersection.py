'''Union and Intersection of two sorted arrays'''


#Union
'''1) Use two index variables i and j, initial values i = 0, j = 0 
2) If arr1[i] is smaller than arr2[j] then print arr1[i] and increment i. 
3) If arr1[i] is greater than arr2[j] then print arr2[j] and increment j. 
4) If both are same then print any of them and increment both i and j. 
5) Print remaining elements of the larger array.'''

def union(a1,a2):
    l1=len(a1)
    l2=len(a2)
    i,j=0,0
    while i<l1 and j<l2:
        if a1[i]<a2[j]:
            print(a1[i],end=" ")
            i+=1
        elif a2[j]<a1[i]:
            print(a2[j],end=" ")
            j+=1
        else:                   #a1[i]==a2[j]
            print(a2[j],end=" ")
            i+=1
            j+=1
    while i<l1:
        print(a1[i],end=" ")
        i+=1
    while j<l2:
        print(a2[j],end=" ")
        j+=1
a1 = [1, 2, 4, 5, 6]
a2 = [2, 3, 5, 7]
# union(a1,a2)
#1 2 3 4 5 6 7 

'''Time Complexity : O(m + n)
Auxiliary Space: O(1)
Handling duplicates in any of the arrays: Above code does not handle duplicates in any of the arrays. '''


# Python3 program to find union of two sorted arrays (Handling Duplicates)
def union(a1,a2):
    l1=len(a1)
    l2=len(a2)
    prev=None
    i=j=0
    while i<l1 and j<l2:
        if a1[i]<a2[j]:
            if a1[i]!=prev:
                print(a1[i],end=" ")
                prev=a1[i]
            i+=1
        elif a2[j]<a1[i]:
            if a2[j]!=prev:
                print(a2[j],end=" ")
                prev=a2[j]
            j+=1
        else:
            if a2[j]!=prev:
                print(a2[j],end=" ")
                prev=a2[j]
                i+=1
                j+=1
    while i<l1:
        if a1[i]!=prev:
            print(a1[i],end=" ")
            prev=a1[i]
            i+=1
    while j<l2:
        if a2[j]!=prev:
            print(a2[j],end=" ")
            prev=a2[j]
            j+=1
arr1 = [1, 2, 2, 2, 3]
arr2 = [2, 3, 4, 5]	
# union(arr1, arr2)
#1 2 3 4 5 

'''Time Complexity: O(l1 + l2) 
Auxiliary Space: O(n)'''


def union(a1,a2):
    s=set()
    for i in a1:
        s.add(i)
    for j in a2:
        s.add(j)
    for k in s:
        print(k,end=" ")
a1=[2,7,9,4,1,6,3,2,2]
a2=[3,4,2,1,4,3,2,5,6,0]
# union(a1,a2)
#0 1 2 3 4 5 6 7 9 


#Intersection
'''1) Use two index variables i and j, initial values i = 0, j = 0 
2) If arr1[i] is smaller than arr2[j] then increment i. 
3) If arr1[i] is greater than arr2[j] then increment j. 
4) If both are same then print any of them and increment both i and j.'''

# Python program to find intersection of two sorted arrays
def Intersection(a1,a2):
    l1=len(a1)
    l2=len(a2)
    i=j=0
    while i<l1 and j<l2:
        if a1[i]<a2[j]:
            i+=1
        elif a2[j]<a1[i]:
            j+=1
        else:
            print(a2[j],end=" ")
            i+=1
            j+=1
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
# Intersection(arr1,arr2)
#2 5 
'''Time Complexity : O(m + n)
Auxiliary Space: O(1)




Handling duplicate in Arrays : 
The above code does not handle duplicate elements in arrays. The intersection should not count duplicate elements.'''

# Python3 program to find Intersection of two
# Sorted Arrays (Handling Duplicates)
def IntersectionArray(a, b, n, m):
	'''
	:param a: given sorted array a
	:param n: size of sorted array a
	:param b: given sorted array b
	:param m: size of sorted array b
	:return: array of intersection of two array or -1
	'''

	Intersection = []
	i = j = 0
	
	while i < n and j < m:
		if a[i] == b[j]:

			# If duplicate already present in Intersection list
			if len(Intersection) > 0 and Intersection[-1] == a[i]:
				i+= 1
				j+= 1

			# If no duplicate is present in Intersection list
			else:
				Intersection.append(a[i])
				i+= 1
				j+= 1
		elif a[i] < b[j]:
			i+= 1
		else:
			j+= 1
			
	if not len(Intersection):
		return [-1]
	return Intersection


arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 6, 7, 8]
	
# l = IntersectionArray(arr1, arr2, len(arr1), len(arr2))
# print(*l)

'''Time Complexity : O(m + n) 
Auxiliary Space : O(min(m, n))'''



def intersection(a,b,n,m):
    i=j=0
    ans=[]
    while i<n and j<m:
        if a[i]==b[j]:
            if len(ans)>0 and ans[-1]==a[i]:
                i+=1
                j+=1
            else:
                ans.append(a[i])
                i+=1
                j+=1
        elif a[i]<b[j]:
            i+=1
        else:
            j+=1
    for i in ans:
        print(i,end=" ")
arr1 = [1, 2, 2, 3, 4 ,6]
arr2 = [2, 2, 4, 6, 7, 8]
intersection(arr1, arr2, len(arr1), len(arr2))
#2 4 6 