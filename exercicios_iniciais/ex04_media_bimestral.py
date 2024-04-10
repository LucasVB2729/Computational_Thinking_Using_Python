notas = 1
soma = 0
quantidade = 0
print("\nInsira a nota dos seus quatro bimestres.\n")
while(quantidade < 4):
    notas = input("Informe o próximo número: ")
    soma += float(notas)
    quantidade += 1
print(f"A sua média bimestral é: {soma / quantidade: .1f}")