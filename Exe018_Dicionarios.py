print("DICIONARIO")
print("-"*30)

#ENTRADA DE DADOS
joao = {"Nome":"joao","Sobrenome":"porto","Profissao":"dev","Idade":"36","Filhos":["pedro","maria"]}

#INFORMACOES
print("Qual o tipo de dado:",type(joao))
print("Quantos dados possui:",len(joao))
print("Sobrenome" in joao)
print("Genero" in joao)
print("Idade" in joao)

print("-="*20)
#Buscar informacao joao(dados)
print("Quais informacoes do joao:")
for x in joao:
    print(x)



print("-"*30)
input("Aperte ENTER p/ sair")