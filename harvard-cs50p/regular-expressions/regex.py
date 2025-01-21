import re

#compile - create pattern

string = "learning python"
pattern = re.compile("python")

result = re.fullmatch(pattern, string) #try to apply the pattern to all of the string

result = re.search(pattern,string) #scan through string looking for a match to the pattern

result = re.findall(pattern,string) #return a list of all non-overlapping matches in the string.

# "." representa qualquer caracter menos \n
string = "python"
pattern = re.compile("......")

string = "py"
pattern = re.compile("..")

string = "python"
pattern = re.compile("py....")

result = re.fullmatch(pattern, string)

# "^" representa início da string, começo da string

string = "b"
pattern = re.compile("^p")
pattern = re.compile("^b")

result = re.fullmatch(pattern, string)

print(result)