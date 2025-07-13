'''
https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e/train/python

8 kyu - Sum of differences in array
'''
arr = [2,1,10]
def sum_of_differences(arr):
    arr = [2,1,10]
    arr.sort(reverse=True)
    if len(arr) < 1:
        return 0
    
    if len(arr) % 2 == 0:
        for item in arr:
            ...

    
print(sum_of_differences(arr))