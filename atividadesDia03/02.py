# Solicita o peso e a altura do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
# Calcula o IMC
imc = peso / (altura ** 2)
# Exibe o IMC
print(f"Seu IMC é: {imc:.2f}")
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"
print(f"Classificação: {classificacao}")