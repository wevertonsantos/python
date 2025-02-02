#https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

nums = [3,2,2,3]
val = 2
k = 0

for num in nums:
    if val in nums:
        nums.remove(val)
print(f"k = {len(nums)}")
print(nums)