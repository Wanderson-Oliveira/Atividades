numero1 = float (input("Digite o primeiro número: "))
numero2 = float (input("Digite o segundo número: "))
operacao = input("Digite o operador (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Divisão por ZERO NÃO"
else:
    resultado = "operador inválido"

print("Resultado = ",resultado)