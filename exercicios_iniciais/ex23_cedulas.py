quantia = int(input("Informe um valor múltiplo de 10: "))

cedulas_50 = quantia // 50
resto_50 = quantia % 50

cedulas_20 = resto_50 // 20
resto_20 = resto_50 % 20

cedulas_10 = resto_20 // 10
resto_10 = resto_20 % 10

print(f"Cédulas de 50: {cedulas_50}\nCédulas de 20: {cedulas_20}\nCédulas de 10: {cedulas_10}")