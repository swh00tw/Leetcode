# easy
# O(n^2)
# best solution is below

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            for i in range(n):
                nums1[i]=nums2[i]
            return
        elif n==0:
            return
        else:
            i=0
            i_max=m
            j=0
            while True:
                if (i>=i_max or j>=n):
                    break
                elif nums1[i]<=nums2[j]:
                    i+=1
                else:
                    for k in range(m+n-2,i-1,-1):
                        nums1[k+1]=nums1[k]
                    nums1[i]=nums2[j]
                    
                    i+=1
                    i_max+=1
                    j+=1
            if (i==i_max and j==n):
                return
            elif i==i_max and j<n:
                for k in range(i_max,m+n):
                    nums1[k]=nums2[j]
                    j+=1
            elif j==n and i<i_max:
                return

# O(n)
# best solution
# https://leetcode.com/problems/merge-sorted-array/discuss/1176400/Best-Python-Solution-Faster-Than-99-One-Loop-No-Splicing-No-Special-Case-Loop
# Fill nums1 backward (non-increasingly)
def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    a, b, write_index = m-1, n-1, m + n - 1

    while b >= 0:
        if a >= 0 and A[a] > B[b]:
            A[write_index] = A[a]
            a -= 1
        else:
            A[write_index] = B[b]
            b -= 1

        write_index -= 1