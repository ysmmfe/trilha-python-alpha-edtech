# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 07 - Questão 7:
# Faça um programa que lê duas strings e imprime quais letras existem nas duas strings.
# Transformar tudo em maiúsculas com o método texto.upper().

primeira_frase = input("Digite uma frase: ")
segunda_frase = input("Agora digite outra frase: ")

primeira_frase = str.upper(primeira_frase) # Converte a string para letras maiúsculas
segunda_frase = str.upper(segunda_frase) # Converte a string para letras maiúsculas
letras_comuns = ""

for letra in primeira_frase:
    if letra in segunda_frase and letra not in letras_comuns and letra != " ": 
        letras_comuns += letra + ", " # Recebendo como resultado apenas as letras que estão nas duas strings
        
print(f"\n> As letras: {letras_comuns}existem nas duas strings!")