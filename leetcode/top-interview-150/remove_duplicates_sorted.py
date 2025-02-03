#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

nums = [0,0,1,1,1,2,2,3,3,4]

for num in nums:
    if nums.count(num) > 1:
        nums.remove(num)

print(nums)