#4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
import datetime
def calcular_dias_vivo(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade * 365

ano_nascimento = int(input("Digite o ano do seu nascimento: "))
dias_vivo = calcular_dias_vivo(ano_nascimento)
print(f"Você está vivo há aproximadamente {dias_vivo} dias.")