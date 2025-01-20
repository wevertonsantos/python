import re

#compile - create pattern

string = "learning python python"
pattern = re.compile("python")

result = re.fullmatch(pattern,string) #try to apply the pattern to all of the string

result = re.search(pattern,string) #scan through string looking for a match to the pattern

result = re.findall(pattern,string) #return a list of all non-overlapping matches in the string.

print(result)