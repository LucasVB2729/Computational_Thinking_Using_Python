# Escreva um programa que pergunte a temperatura em celsius e converta para Kelvin.

graus = float(input("Informe a temperatura em Graus Celsius (apenas o valor): "))
print(f"{graus}° Celsius são equivalentes a {round(graus + 273.15, 2)} Kelvins")