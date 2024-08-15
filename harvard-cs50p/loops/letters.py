def main():
    names = ["Mario","Luigi","Daisy","Yoshi"]
    sender = "Princess Peach"
    for name in names:
        print(write_letter(name,sender))

def write_letter(receive, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receive},

        You are cordially invited to a ball at  
        Peach's Castle this evening, 7:00PM.

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

main()