#3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
    #a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
    #b - Preço final: Determina o novo preço após o desconto.
    #c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
    #d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
def calcular_preco_com_desconto(preco, desconto):
    valor_desconto = preco * (desconto / 100)
    preco_final = preco - valor_desconto
    return round(preco_final, 2)
#codigo main
preco = float(input("Digite o preço do produto: R$"))
desconto = float(input("Digite a porcentagem de desconto: "))
preco_final = calcular_preco_com_desconto(preco, desconto)
print(f"O preço final após {desconto}% de desconto é: R${preco_final}")
