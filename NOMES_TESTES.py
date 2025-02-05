#TESTE DE NOMES

print("<<Teste de nomes>>")
print("-="*20)

#DADOS
nome = "Thiago"
sobrenome_pai = "Porto"
sobrenome_mae = "Carvalho"
iniciais = nome[0] + sobrenome_mae[0] + sobrenome_pai[0]
empresa = "Kaisen"

#RESOLUÇÃO
print("<Informações>")
print("Nome do usuário:"+nome+" "+sobrenome_pai+" "+sobrenome_mae)
print("Quais são as iniciais: "+iniciais)
print("Nome da empresa: "+empresa)

#RODANDO APLICAÇÃO
print(">>>INICIO")
print("O nome completo é: "+nome+" "+sobrenome_pai+" "+sobrenome_mae+" e as inicias são: " +iniciais)
print("Criando o e-mail: " +nome+"."+sobrenome_pai+"@"+empresa+".com")
print("-="*20)
input("Clique para sair")

