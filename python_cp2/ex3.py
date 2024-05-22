#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh 
#consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar 
#de acordo com a tabela do exercício.

kwh_consumida = float(input("\nDigite a quantidade de kWh consumida: "))
tipo_instalacao = input("Digite o tipo de instalação (R para residências, I para indústrias, C para comércios): ")

if tipo_instalacao.upper() == 'R':  # Residencial
    if kwh_consumida <= 500:
        preco_pagar = kwh_consumida * 0.40
    else:
        preco_pagar = kwh_consumida * 0.65
elif tipo_instalacao.upper() == 'C':  # Comercial
    if kwh_consumida <= 1000:
        preco_pagar = kwh_consumida * 0.55
    else:
        preco_pagar = kwh_consumida * 0.60
elif tipo_instalacao.upper() == 'I':  # Industrial
    if kwh_consumida <= 5000:
        preco_pagar = kwh_consumida * 0.55
    else:
        preco_pagar = kwh_consumida * 0.60
else:
    print("Tipo de instalação inválido!\n")
    exit()

print(f"O preço a pagar pelo fornecimento de energia elétrica é: R$ {preco_pagar:.2f}\n")