from datetime import date

ano_nascimento = int(input("\nDigite o ano de nascimento: "))
idade = date.today().year - ano_nascimento
if idade < 16:
   print(f"Você tem {idade} anos de idade, portanto, você ainda não pode votar.\n")
elif 18 <= idade < 70:
   print(f"Você tem {idade} anos de idade, portanto, seu voto é obrigatório.\n")
else:
   print(f"Você tem {idade} anos de idade, portanto, seu voto é facultativo.\n")