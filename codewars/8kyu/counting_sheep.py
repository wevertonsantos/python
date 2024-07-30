'''
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined
'''

array1 = [True,  True,  True,  None,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ]

def count_sheeps(sheep):
    present = []
    missing = []
    null = []
    for i in sheep:
        if i == True:
            present.append(i)
        elif i == False:
            missing.append(i)
        else:
            null.append(i)
    result = len(present)
    return result

print(count_sheeps(array1))