gols_time1 = int(input("Digite a quantidade de gols do primeiro time: "))
gols_time2 = int(input("Digite a quantidade de gols do segundo time: "))

if gols_time1 > gols_time2:
    print("Vitória do primeiro time!")
elif gols_time1 < gols_time2:
    print("Vitória do segundo time!")
else:
    print("Empate!")