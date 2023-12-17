# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# Ciclo 1 > Módulo 1 - Python Essentials > Aula 03 - Desvio Condicional > Questão 8:
# Como você lê um arquivo de texto em Python e quais são as melhores práticas para fechar o arquivo após a leitura? Crie um exemplo simples.

# Explicação:
# A melhor prática para fechar um arquivo após a leitura é utilizar o método "with open", que fecha o arquivo automaticamente. Para ler
# um arquivo em Python, é preciso utilizar a estrutura with open("a", "b") as variável, em que "a" é o nome do arquivo em formato .txt
# e "b" é o que você quer fazer com o arquivo, seja ler ("r"), escrever ("w"), adicionar algo ("a"), etc. A variável é utilizada para
# armazenar o conteúdo que está dentro do arquivo, conforme o exemplo.

with open("exercicio08.txt", "r") as arquivo2:
    mensagem = arquivo2.read()
    
print(mensagem)