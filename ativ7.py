def converter(valor, cotacao, tipo):
    if tipo == 1:  # Dólar para Real
        return valor * cotacao
    elif tipo == 2:  # Real para Dólar
        return valor / cotacao

hist_dolar = []

cotacao = 0

while True:
    print("\n--- MENU ---")
    print("1 - Converter Dólar para Real")
    print("2 - Converter Real para Dólar")
    print("3 - Atualizar cotação do dólar")
    print("4 - Mostrar Histórico")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor = float(input("Digite o valor em dólar: "))
        resultado = converter(valor, cotacao, 1)
        print(f"Valor em reais: R$ {resultado:.2f}")

    elif opcao == 2:
        valor = float(input("Digite o valor em reais: "))
        resultado = converter(valor, cotacao, 2)
        print(f"Valor em dólares: $ {resultado:.2f}")

    elif opcao == 3:
        cotacao = float(input("Digite a nova cotação do dólar: "))
        hist_dolar.append(cotacao)
        print("Cotação atualizada com sucesso!")
    
    elif opcao == 4:
        print("\nEsse é o histórico da cotação inserida: ")
        for i in hist_dolar:
            print(f"{i:.2f}")

    elif opcao == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")