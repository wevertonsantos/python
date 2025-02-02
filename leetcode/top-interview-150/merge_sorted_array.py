#https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

for num1 in nums1[m:]:
    if num1 == 0:
        nums1.remove(num1)
        
for num2 in nums2[:n]:
    nums1.append(num2)

print(nums1)