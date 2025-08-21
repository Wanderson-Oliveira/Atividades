valorproduto = float (input("Digite o valor do produto: R$ "))
valordesconto = float (input("Digite a porcentagem de desconto (%): "))
valordesconto = valordesconto / 100
preco_final = valorproduto - (valorproduto * valordesconto)

print(f"Produto: Camiseta")
print(f"Preço original: R$ {valorproduto:.2f}")
print(f"Desconto: R$ {valordesconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
