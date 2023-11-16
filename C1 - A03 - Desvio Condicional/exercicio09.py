# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 03 - Questão 9:
# Como você escreve um arquivo de texto em Python e quais são as melhores práticas para abrir e fechar o arquivo após a leitura?
# Crie um exemplo simples.

# A melhor prática para fechar um arquivo após a abertura é utilizar o método "with open", que fecha o arquivo automaticamente.
# Para criar um arquivo em Python, é preciso utilizar a estrutura with open("a", "b") as variável, em que "a" é o nome do arquivo
# em formato .txt e "b" é o que você quer fazer com o arquivo, seja ler ("r"), escrever ("w"), adicionar algo ("a"), etc. A variável
# é utilizada para armazenar o conteúdo que está dentro do arquivo, conforme o exemplo.

with open("exemplo09.txt", "w") as arquivo:
    arquivo.write("escrita da questão 9")