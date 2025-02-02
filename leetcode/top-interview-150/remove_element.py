#https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

nums = [3,2,2,3]
val = 3

k = 0
for i in range(len(nums)):
    if val in nums:
        if nums[i] == val:
            k += 1
            nums.remove(val)
print(f"k = {k}")
print(nums)