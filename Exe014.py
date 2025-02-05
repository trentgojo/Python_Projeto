 print("<<BOLETIM ESCOLAR>>")

print("-="*30)
#DADOS DA AVALIAÇÃO
AV1 = float(input("Digite a nota AV1: "))
AV2 = float(input("Digite a nota AV2: "))
print("-="*30)

#RESULTADO DAS AVALIAÇÕES
print("A avaliação N1(",AV1,")+ avaliação N2(",AV2,")o resultado é:",(AV1+AV2))
print("Média final:",(AV1+AV2)/2)
print("-="*30)

#RESULTADO: APROVADO E REPROVADO
media = float(input("Qual é a média final: "))
if media >=5.0:
    print("<O aluno obteve a nota acima de 5.0: Aprovado")
else:
    print("O aluno obteve a nota abaixo de 5.0: Reprovado")
print("-="*30)

print("Boas Férias")