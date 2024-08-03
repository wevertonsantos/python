def double_char():
    s = "Hello World"
    string_dbl_char = []
    star = ""
    for char in s:
        string_dbl_char.append(f"{char}{char}")
    star = str(string_dbl_char)
    return star

retur = double_char()
print(retur)