#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

nums = [0,0,1,1,1,2,2,3,3,4]

i = 0
while i <= len(nums):
    nums.count(nums[i]) > 1
    nums.remove(nums[i])
    i += 1
print(nums)