#https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

nums = [3,3]
val = 3

while val in nums:
    nums.remove(val)
print(f"k = {len(nums)}")