import re

#compile - create pattern

string = "learning python"
pattern = re.compile("python")

result = re.fullmatch(pattern,string) #try to apply the pattern to all of the string

result = re.search(pattern,string) #scan through string looking for a match to the pattern

print(result)