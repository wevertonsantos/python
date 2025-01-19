import re

email = input("What's your e-mail? ").strip()

if re.search(".+@.+",email):
    print("Valid")
else:
    print("Invalid")