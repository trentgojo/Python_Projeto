print("DATA DE NASCIMENTO")
print("_"*55)

#TUPLA COM MESES E ANO
meses = ("Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho",
         "Agosto","Setembro","Outubro","Novembro","Dezembro")


#ENTRADA DA DATA DE NASCIMENTO
data_nasc = input("Digite sua data de nascimento no formato DD-MM-AAAA ")

#OBTENDO O DIA, MES E ANO DE NASCIMENTO
dia = data_nasc[:2]
mes = meses [int(data_nasc[3:5]) -1]


print("-="*30)

#IMPRIMINDO O RESULTADO
print("Voce nasceu no dia",dia,"do mes de",mes)


print("-="*30)
input("Aperte enter p/ sair")
