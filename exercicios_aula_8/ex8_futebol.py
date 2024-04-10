gols_time1 = int(input("\nDigite a quantidade de gols do primeiro time: "))
gols_time2 = int(input("Digite a quantidade de gols do segundo time: "))

if gols_time1 > gols_time2:
    print("Vitória do primeiro time!\n")
elif gols_time1 < gols_time2:
    print("Vitória do segundo time!\n")
else:
    print("Empate!\n")