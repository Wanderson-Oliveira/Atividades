#Conversor de Temperatura
#Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
#O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

temperatura = float(input("Informe a temperatura: "))
unidade_origem = input("Informe a unidade de origem (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()

if unidade_origem == 'C':
    temperatura_Fahrenheit = (temperatura * 9/5) + 32
    temperatura_Kelvin = temperatura + 273.15
    print(f"A temperetura de {temperatura}°C é igual a {temperatura_Fahrenheit}°F que também equivale a {temperatura_Kelvin} K")
elif unidade_origem == 'F':
    temperatura_Celsius = (temperatura - 32) * 5/9
    temperatura_Kelvin = temperatura_Celsius + 273.15
    print(f"A temperetura de {temperatura}°F é igual a {temperatura_Celsius}°C que também equivale a {temperatura_Kelvin} K")
elif unidade_origem == 'K':
    temperatura_Celsius = temperatura - 273.15
    temperatura_Fahrenheit = (temperatura_Celsius * 9/5) + 32
    print(f"A temperetura de {temperatura} K é igual a {temperatura_Celsius}°C que também equivale a {temperatura_Fahrenheit}°F")
else:
    print("Unidade de origem inválida. Por favor, use C, F ou K.")
# Fim do programa