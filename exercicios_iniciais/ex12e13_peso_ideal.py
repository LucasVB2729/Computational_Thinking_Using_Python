#Informar o sexo
sexo = (input("Informe seu sexo (masculino, feminino): "))

#Homem
if sexo == "M" or sexo == "m" or sexo == "Masculino" or sexo == "masculino" or sexo == "Homem" or sexo == "homem":
    alturahomem = float(input("Informe sua altura: "))
    pesoidealhomem = (72.7*alturahomem) - 58
    print(f"Seu peso ideal é {pesoidealhomem:.2f}kg")

#Mulher
elif sexo == "F" or sexo == "f" or sexo == "Feminino" or sexo == "feminino" or sexo == "Mulher" or sexo == "mulher":
    alturamulher = float(input("Informe sua altura: "))
    pesoidealmulher = (62.1*alturamulher) - 44.7
    print(f"Seu peso ideal é {pesoidealmulher:.2f}kg")

#Erro
else:   
    print("[ERRO] Insira um sexo válido!")