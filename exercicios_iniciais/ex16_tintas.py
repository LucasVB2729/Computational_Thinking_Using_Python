areaPintura = float(input("\nInforme o tamanho em metros quadrados da área a ser pintada: "))
quantidadeLatas = areaPintura / 18 / 3
precoTotal = quantidadeLatas * 80

print(f"Para pintar uma área de {areaPintura:.2f} m² será necessário comprar {quantidadeLatas:.2f} lata(s) 
de tinta de 18 litros, investindo um valor de R${precoTotal:.2f}!")