while True:
    resp1 = float(input("Diz um número aí:\n"))
    resp2 = float(input("Diz outro número aí:\n"))
    try:
        resp3 = resp1 / resp2
    except ZeroDivisionError:
        print("\nDa não pô, faz direito.\n")
    else:
        print(f"\nBoa, deu {resp3}.")
        print("Cabô.")
        break