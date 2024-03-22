numint1 = int(input("Insira um número Inteiro: "))
numint2 = int(input("Insira outro número Inteiro: "))
numreal = float(input("Agora insira um número Real: "))

a = (numint1 * 2) * (numint2 / 2)
b = (numint1 * 3) + numreal
c = numreal ** 3

print(f"{a:.4f}\n{b:.4f}\n{c:.4f}")