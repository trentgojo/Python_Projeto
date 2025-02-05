#DATA DE NASCIMENTO

print("<<DATA DE NASCIMENTO>>")

#DADOS DOS MESES

meses = ("Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")
ano = ("1930","1940","1950","1960","1970","1980","1990","2000","2010")
print("-="*20)

#RODANDO
nasc = input("Digite a sua data de nascimento do formato DD-MM-AAAA: ")
indice = int(nasc[3:5])-1
mes = meses[indice]

print("Voce nasceu no mes de: "+mes)
print("-="*20)

input("CLIQUE ENTER P/ SAIR")