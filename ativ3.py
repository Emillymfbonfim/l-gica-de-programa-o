ah = input("Quer converter?\n ")
while ah.lower() == "sim":
    resp = input("Converter m ou cm?\n ")
    if resp.lower() == "m":
        m = float(input("Diga o valor em metros:\n "))
        conv = m * 100
        print(f"{m}m, em cm é: {conv}")
        ah = input("Quer converter?\n ")
    elif resp.lower() == "cm":
        cm = float(input("Diga o valor em centimetros:\n "))
        conv = cm / 100
        print(f"{cm}m, em cm é: {conv}")
        ah = input("Quer converter?\n ")
    else:
        print("Responde direito")



""" print(float(input("Qual o valor em metros que será transformado para centímetros?\n "))*100) """