import re

#compile - create pattern

string = "python"
pattern = re.compile("python")

result = re.fullmatch(pattern,string) #try to apply the pattern to all of the string

print(result)