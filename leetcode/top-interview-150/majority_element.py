#https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

nums =  [2,2,1,1,1,2,2]
for num in nums:
    if nums.count(num) > len(nums) / 2:
        ...

i = 0
while i < sum(nums):
    if nums.count(nums[i]) > len(nums) / 2:
        print(nums[i])
    i += 1