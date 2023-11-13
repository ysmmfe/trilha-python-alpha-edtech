numero = int(input("Informe um número de 4 dígitos para encriptar: "))

milhar = numero//1000
centena = (numero%1000)//100
dezena = (numero%100)//10
unidade = numero - (milhar*1000) - (centena*100) - (dezena*10)

#criptografado = (((milhar + 1)%10) * 1000) + (((centena + 1)%10) * 100) + (((dezena + 1)%10) * 10) + ((unidade + 1)%10)
milhar = ((milhar + 1)%10)
centena = ((centena + 1)%10)
dezena = ((dezena + 1)%10)
unidade = ((unidade + 1)%10)

print(f"O número {numero} encriptado fica {milhar}{centena}{dezena}{unidade}")
