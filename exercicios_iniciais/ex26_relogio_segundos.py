#Coletar informação
tempoMinutos = int(input("\nInforme a quantidade de segundos para converter em horas/minutos/segundos: "))

#Cálculo de horas, minutos e segundos
horas = tempoMinutos // 3600
restoHora = tempoMinutos % 3600
minutos = restoHora // 60
restoMinutos = restoHora % 60
segundos = restoMinutos // 1
restoSegundos = restoMinutos % 1

#Impressão
print(f"{horas}h{minutos}m{segundos}s\n")