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

# "^" representa início da string, verificação no começo da string

string = "b"
pattern = re.compile("^p")
pattern = re.compile("^b")

result = re.fullmatch(pattern, string)

# "[]" representa um conjunto de alguma operação, isolar um conjunto

string = "a"
pattern = re.compile("^[a]")

result = re.fullmatch(pattern, string)

# "$" representa o final da string, verificação no final da string

string = "a"
pattern = re.compile("a$")
result = re.fullmatch(pattern, string)

# "[^]" verificação se é diferente do caracter passado

string = "a"
pattern = re.compile("[^b]")
result = re.fullmatch(pattern, string)

# "\w" - verificação se aquilo passado é um alfanumérico
# "\W" - verificação se aquilo passado não é um alfanumérico
string = "@1a"
pattern = re.compile("[\W]")
result = re.findall(pattern, string)

print(result)