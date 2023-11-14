# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 02 - Questão 10:
# Um aluno projetou um método para encriptar números de 4 dígitos. O método consiste em adicionar 1 em cada dígito do número.
# Por exemplo: O número 1234 ficaria 2345 após a encriptação; O número 9092 ficaria 0103 após a encriptação.
# O aluno então desafiou o professor a escrever o código desse método em Python. Você pode ajudar o professor a escrever esse código? 
# Seu código não pode usar estruturas de dados auxiliares como vetor ou lista.

numero = int(input("Informe um número de 4 dígitos para encriptar: "))

milhar = numero//1000
centena = (numero%1000)//100
dezena = (numero%100)//10
unidade = numero - (milhar*1000) - (centena*100) - (dezena*10)

#criptografado = (((milhar + 1)%10) * 1000) + (((centena + 1)%10) * 100) + (((dezena + 1)%10) * 10) + ((unidade + 1)%10) -> lógica inicial
milhar = ((milhar + 1)%10)
centena = ((centena + 1)%10)
dezena = ((dezena + 1)%10)
unidade = ((unidade + 1)%10)

print(f"O número {numero} encriptado fica {milhar}{centena}{dezena}{unidade}")
