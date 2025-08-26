#criar um programa que identifique palavras palíndromos ignorando ponstos e espaços
def eh_palindromo(palavra):
    texto_limpo = ''.join(caractere.lower() for caractere in palavra if caractere.isalnum())
   
    #inverso = texto_limpo[::-1]

    inverso = ''
    for caractere in texto_limpo:
        inverso = caractere + inverso

    if texto_limpo == inverso:
        return True
    else:
        return False
    
entrada = input("Digite uma palavra ou frase: ")
resultado = eh_palindromo(entrada)
print(f"{entrada} > A palavra ou texto é um palíndromo? {resultado}")