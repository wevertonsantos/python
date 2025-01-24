import re

email = input("What's your e-mail? ").strip()

if re.search(r".+@.+\.edu",email):
    print("Valid")
else:
    print("Invalid")