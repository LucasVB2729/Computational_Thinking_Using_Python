salarioAtual = float(input("\nInforme seu salário atual: "))
salarioGerente = salarioAtual + (salarioAtual*10/100)
salarioEngenheiro = salarioAtual + (salarioAtual*20/100)
salarioTecnico = salarioAtual + (salarioAtual*30/100)
salarioDemaisCargos = salarioAtual + (salarioAtual*40/100)

print(f"Verifique seu novo salário de acordo com o seu cargo\n101 Gerente: R${salarioGerente:.2f}\n102 Engenheiro: R${salarioEngenheiro:.2f}\n103 Técnico: R${salarioTecnico:.2f}\nDemais Cargos: R${salarioDemaisCargos:.2f}\n")