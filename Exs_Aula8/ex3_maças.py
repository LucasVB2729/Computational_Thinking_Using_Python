quantidade = int(input("\nInforme o número de maçãs compradas: "))
valor = 0
if quantidade < 12:
    valor = 0.30 * quantidade
else:
    valor = 0.25 * quantidade
print(f"Maçãs Compradas: {quantidade}\nValor Total: R$ {valor:.1f}\n")