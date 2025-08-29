#Leia um arquivo que contém dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de execução constantes. 
import pandas as pd

def processar_logs(caminho_arquivo):
    try:
        leitura = pd.read_csv(caminho_arquivo)
        tempos_execucao = leitura['tempo_execucao'].mean()
        desvio_padrao = leitura['tempo_execucao'].std()
        return f"""
                Média do tempo de execução: {tempos_execucao} 
                Desvio padrão do tempo de execução: {desvio_padrao} 
                """
    except FileNotFoundError:
        return "Arquivo não encontrado. Verifique o caminho e tente novamente."
    
nome_arquivo = input("Digite o caminho do arquivo de log (ex: logs.csv): ")

print(processar_logs(nome_arquivo))