while True:
    salario = float(input("Qual é o teu salario? "))
    if salario <= 280.00:
        salario2 = salario * 1.2
        percentual = 20
    elif salario > 280.00 and salario <= 700.00:
        salario2 = salario * 1.15
        percentual = 15
    elif salario > 700.00 and salario <= 1500.00:
        salario2 = salario * 1.1
        percentual = 10
    elif salario > 1500.00:
        salario2 = salario * 1.05
        percentual = 5

    aumento = salario2 - salario

    print(f"Seu salario antigo era de {salario}")
    print(f"Seu percentual de aumento foi de {percentual}%, ou seja, aumentou {aumento}")
    print(f"Seu novo salario é {salario2}")