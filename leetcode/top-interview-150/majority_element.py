#https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def majorityElement(self, nums):
        self.lista_nums = []
        for n in nums:
            if n not in self.lista_nums:
                self.lista_nums.append(n)
        for n in self.lista_nums:
            if nums.count(n) > len(nums) // 2:
                return n