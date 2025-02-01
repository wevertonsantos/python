#https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3

nums1.sort()
for num1 in nums1[0:m]:
    if num1 == 0:
        nums1.remove(0)

for num2 in nums2[0:n]:
    nums1.append(num2)

nums1.sort()
print(nums1)