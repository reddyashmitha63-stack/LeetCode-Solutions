class Solution(object):
    def intersection(self, nums1, nums2):
        n1=len(nums1)
        n2=len(nums2)
        N=[]
        for i in range(n1):
            for j in range(n2):
                if nums1[i]==nums2[j]:
                    if nums1[i] not in N:
                        N.append(nums1[i])
        return N