import csv

def ler_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        return(f"Encontrei nada não")



nome_arquivo = input("Digite o nome do arquivo CSV que deseja ler (ex: pessoas.csv): ")
print(ler_csv(nome_arquivo))