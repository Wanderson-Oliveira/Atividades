valorreal = float (input("Digite o valor em Real que deseja converter: R$ "))
txdolar = 5.2
txeuro = 6.15

r01 = round(valorreal / txdolar, 2)
r02 = round(valorreal / txeuro, 2)

print("Valor em Real: R$", valorreal)
print("Taxa de conversão Dólar: U$", r01)
print("Taxa de conversão Euro: €", r02)