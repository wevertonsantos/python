'''
https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150
'''

s = "A man, a plan, a canal: Panama"
new_s = ""
for c in s:
    if c.isalpha():
        new_s += c.lower()
print(new_s)