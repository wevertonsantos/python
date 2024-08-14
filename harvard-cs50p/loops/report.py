def main():
    spacecraft = {
        "name":"Voyager 1",
        "distance":102
    }
    #spacecraft["distance"] = 0.00 - Cria chave no dicionário: 
    spacecraft.update({"distance":0.01,"orbit":"Sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ======== REPORT ========

    Name: {spacecraft.get("name","Unknown")}
    Distance: {spacecraft.get("distance","Unknown")} AU
    Orbit: {spacecraft.get("orbit","Unknown")}

    ========================
    """

main()