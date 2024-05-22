#Escreva um programa que verifique se uma letra inserida pelo usuário é vogal ou consoante.

letra = input("\nDigite uma letra: ")
if letra.lower() in 'aeiou':
    print("A letra inserida é uma vogal.\n")
else:
    print("A letra inserida é uma consoante.\n")