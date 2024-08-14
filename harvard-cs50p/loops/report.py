def main():
    spacecraft = {
        "name":"Voyager 1"
    }
    #spacecraft["distance"] = 0.00 - Cria chave no dicionário: 
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ======== REPORT ========

    Name: {spacecraft.get("name","Unknown")}
    Distance: {spacecraft.get("distance","Unknown")} AU

    ========================
    """

main()