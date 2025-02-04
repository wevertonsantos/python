#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

nums = [1,1,1,1]

for num in nums:
    n = nums.count(num)
    if n > 1:
        nums.remove(1)
        n -= 1
print(nums)

# preciso remover números duplicados de um array, até ficar apenas 1