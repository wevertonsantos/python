#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

nums = [1,1,1,1]

for i in range(len(nums)):
    if i >= 2:
        i -= 1
    if nums.count(nums[i]) > 1:
        nums.remove(nums[i])
    else:
        nums.remove(nums[i])
print(nums)