# Rotina que converte um determinado valor em realis em dólares
print("<<Conversão de Real em Dólar>>")
print("-="*15)

#Variáveis
valor_real = 0.0
cotacao_dolar = 0.0
conversao = 0.0

#Inicio
print("Programa para converter reais em dólares")
valor_real = float(input("Informe o valor disponivel em reais (para comprar dólares): R$ "))
cotacao_dolar = float(input("Informe o valor do dólar em reais (cotação do dia): R$ "))
conversao = valor_real / cotacao_dolar
print("Com essa quantia será possível comprar: US$", conversao)
print("Boa viagem!!")
