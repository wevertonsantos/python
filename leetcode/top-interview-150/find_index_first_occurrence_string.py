'''
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=top-interview-150
'''

haystack,needle = "sadbutsad","sad"
if haystack.find(needle) > -1:
    print(haystack.find(needle))
else:
    print(-1)