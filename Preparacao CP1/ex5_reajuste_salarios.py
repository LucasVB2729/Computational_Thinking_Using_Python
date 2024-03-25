'''
Uma empresa concederá um aumento de rio ao salá s seus funcionários, variável de acordo com o cargo, conforme a tabela abaixo. Faça um algoritmo que leia o salário e calcule o novo salário, mostrando todas as variações para os cargos e exiba uma observação, “verifique seu novo salário de acordo com o seu cargo”. Se o cargo do funcionário não estiver na tabela, ele deverá, então, receber 40% de aumento. Mostre o salário antigo, os novos salários e a diferença. 

Código	Cargo		Percentual	
101		Gerente	10%
102		Engenheiro	20%
103		Técnico	30%
'''

salarioAtual = float(input("\nInforme seu salário atual: "))
salarioGerente = salarioAtual + (salarioAtual*10/100)
salarioEngenheiro = salarioAtual + (salarioAtual*20/100)
salarioTecnico = salarioAtual + (salarioAtual*30/100)
salarioDemaisCargos = salarioAtual + (salarioAtual*40/100)

print(f"Verifique seu novo salário de acordo com o seu cargo\n101 Gerente: R${salarioGerente:.2f}\n102 Engenheiro: R${salarioEngenheiro:.2f}\n103 Técnico: R${salarioTecnico:.2f}\nDemais Cargos: R${salarioDemaisCargos:.2f}\n")