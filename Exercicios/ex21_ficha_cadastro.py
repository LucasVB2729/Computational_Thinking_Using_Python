#Variáveis
nomeCompleto = str(input("Informe seu nome completo: "))
idade = int(input("Informe sua idade: "))
genero = str(input("Informe seu gênero: "))
estadoCivil = str(input("Informe seu estado civil: "))
salario = float(input("Informe seu salário: "))
anosTrabalhados = int(input("Informe seu tempo de contribuição trabalhista: "))
diasTrabalhados = anosTrabalhados * 294
horasTrabalhadas = diasTrabalhados * 8
anosAposentadoria = (90 - idade + anosTrabalhados) / 2

#Impressão
print(f"\nNome: {nomeCompleto}\nIdade: {idade}\nGênero: {genero}\nEstado civil: {estadoCivil}\nSalário: {salario}\nAnos trabalhados: {anosTrabalhados}\nDias trabalhados: {diasTrabalhados}\nHoras trabalhadas: {horasTrabalhadas}\nAnos para aposentar: {anosAposentadoria:.0f}\n\n")
print(f"{nomeCompleto.upper()}\n{nomeCompleto.lower()}\n{nomeCompleto.title()}")