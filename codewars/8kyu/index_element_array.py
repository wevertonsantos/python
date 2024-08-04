'''
Be Concise IV - Index of an element in an array

- Task -
Provided is a function Kata which accepts two parameters in the following order: array, element and returns the index of the element if found and "Not found" otherwise. Your task is to shorten the code as much as possible in order to meet the strict character count requirements of the Kata. (no more than 161) You may assume that all array elements are unique.
'''

array = [2,3,5,7,11]

#find = lambda arr,elem: map[arr[i] == elem]

#next((i for i in range(len(arr)) if arr[i] == elem),"Not found")

find = lambda arr,elem: next((i for i in range(len(arr)) if arr[i] == elem),"Not found")

res = find(array,0)
print(res)
