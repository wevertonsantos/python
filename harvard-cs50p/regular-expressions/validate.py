email = input("What's your e-mail?").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")