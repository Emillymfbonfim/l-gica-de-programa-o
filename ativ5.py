while True:
    resp = input("Em qual turno vc estuda? (M, V ou N) ")
    if resp.lower() == "m":
        print("Bom Dia!")
        break
    elif resp.lower() == "v":
        print("Boa Tarde!")
        break
    elif resp.lower() == "n":
        print("Boa Noite!")
        break
    else:
        print("Responde direito.")