valor_produto = 50.00
porcentagem_desconto = 20

desconto = (valor_produto * porcentagem_desconto) / 100
preco_final = valor_produto - desconto
print(f"Produto: Camiseta")
print(f"Preço original: R$ {valor_produto:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
