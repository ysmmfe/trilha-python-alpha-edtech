# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 03 - Questão 4:
# Explique como a função replace() é usada para substituir partes de uma string por outras. 
# Dê um exemplo de como você pode usar replace() para substituir todas as ocorrências de uma palavra em uma frase.

# Explicação:
# A função replace() é utilizada para trocar alguma letra ou palavra de uma string por outra. Ela possui parâmetros ("a", "b),
# em que "a" é a palavra ou letra que está na frase inicialmente e será substituída, e "b" é a palavra ou letra substituinte,
# que vai entrar na frase no lugar do parâmetro "a". Segue em anexo exemplo dos usos de letras e palavras.

# Substituindo uma palavra por outra
frase = "Eu gosto de vitamina de banana"
print("Frase antes do replace: ", frase)
novaFrase = frase.replace("banana", "abacate")
print("A nova frase é: ", novaFrase)

# Substituindo uma letra por outra
frase2 = "Eu me chamo Yasmim"
print("\nSegunda frase antes do replace: ", frase2)
novaFrase2 = frase2.replace("m", "b")
print("A segunda nova frase é: ", novaFrase2)