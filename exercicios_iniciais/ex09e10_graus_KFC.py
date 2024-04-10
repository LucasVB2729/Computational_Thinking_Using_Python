medida = input("Conversor de Medidas de Temperatura\n\nIndique a medida de temperatura a ser convertida (Celsius, Fahrenheit, Kelvin): ")
temperatura = float(input("Indique o valor da temperatura: "))
if(medida == "celsius" or medida == "Celsius" or medida == "graus celsius"):
    print(f"Temperatura em Fahrenheit: ", round((temperatura * 9/5) + 32, 2), "\nTemperatura em Kelvin: ", round(temperatura + 273.15, 2), "\n")
if(medida == "fahrenheit" or medida == "Fahrenheit" or medida == "graus fahrenheit"):
    print(f"Temperatura em Celsius: ", round((temperatura - 32) * 5/9, 2), "\nTemperatura em Kelvin: ", round((temperatura - 32) * 5/9 + 273.15, 2))
if(medida == "kelvin" or medida == "Kelvin"):
    print(f"Temperatura em Celsius: ", round(temperatura - 273.15, 2), "\nTemperatura em Fahrenheit: ", round((temperatura - 273.15) * 9/5 + 32, 2))