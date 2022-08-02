def findMedianSortedArrays(nums1, nums2) :
        a=len(nums1)
        b=len(nums2)
        i,j,k=0,0,0
        nums3=[None]*(a+b)
        while i<a and j<b:
            if nums1[i]<nums2[j]:
                nums3[k]=nums1[i]
                i+=1
            else:
                nums3[k]=nums2[j]
                j+=1
            k+=1
        while i<a:
            nums3[k]=nums1[i]
            i+=1
            k+=1
        while j<b:
            nums3[k]=nums2[j]
            j+=1
            k+=1
        
        if len(nums3)%2!=0:
            return float(nums3[int(len(nums3)/2)])
        else:
            return float(   (   nums3[int(len(nums3)/2)]   +   nums3[int((len(nums3)-1)/2)]   )   /   2.0   )
arr1=[1,2]
arr2=[3,4]
print(findMedianSortedArrays(arr1,arr2))
#2.5