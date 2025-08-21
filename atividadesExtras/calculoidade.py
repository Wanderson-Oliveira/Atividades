idade = float(input("Digite sua idade: "))
print(f"Sua idade é: {idade} anos")

if idade < 0:
    print("Você nem nasceu.")
elif 0 <= idade < 12:
    print("Você é uma criança.")
elif 12 <= idade < 18:
    print("Você é um adolescente.")
elif 18 <= idade < 60:
    print("Você é um adulto.")
elif 60 <= idade < 120:
    print("Você é um idoso.")  
else:
    print("Tio Paulo está te chamando.")
