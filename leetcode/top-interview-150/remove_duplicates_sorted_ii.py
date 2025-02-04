#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

nums = [0,0,1,1,1,1,2,3,3]

for num in nums[:]:
    if nums.count(num) > 2:
        nums.remove(num)
print(len(nums))