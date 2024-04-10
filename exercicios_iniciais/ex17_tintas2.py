import math
#Área a ser pintada
areaPintura = float(input("\nInforme o tamanho em metros quadrados da área a ser pintada: "))
calculoFolga = areaPintura * 10 / 100
areaPintura2 = areaPintura + calculoFolga
 
#Lata de 18 litros
quantidadeLatas = math.ceil(areaPintura / 18 / 6)
precoLatas = math.ceil(quantidadeLatas * 80)
 
#Galão de 3,6 litros
quantidadeGaloes = math.ceil(areaPintura / 3.6 / 6)
precoGaloes = math.ceil(quantidadeGaloes * 25)
 
#Misturando Latas e Galões
lata = areaPintura2 // 108
restoLata = areaPintura2 % 108
custoLata = math.ceil(lata * 80)
galao = math.ceil(restoLata / 21.6)
custoGalao = math.ceil(galao * 25)
 
#Impressão dos textos
print(f"\nComprando apenas latas de 18 litros:\nQuantidade de latas: {quantidadeLatas:.2f}\nPreço: R$ {precoLatas:.2f}\n")
print(f"Comprando apenas galões de 3,6 litros:\nQuantidade de galões: {quantidadeGaloes:.2f}\nPreço: R$ {precoGaloes:.2f}\n")
print(f"Misturando latas e galões:\nQuantidade de latas: {lata:.2f}\nQuantidade de galões: {galao:.2f}\nPreço: R$ {custoLata + custoGalao:.2f}")