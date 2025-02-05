print("-=-=-=-=-=-=DECLARACAO DA EMPRESA-=-=-=-=-=-=")

#DECLARAÇÃO DA EMPRESA
responsavel=input("Digite o nome do responsavel: ")
funcionario=input("Digite o nome do funcionario: ")
evento=input("Digite o nome do evento: ")
valor=float(input("Digite o valor que sera ressarcido: "))
print("-="*30)

#SOLUÇÃO
print("Declaro para o senhor",responsavel,"e o senhor",funcionario,
      "estiveram presentes no evento",evento,"e gastou o valor de R$",str(valor),"reais com a entrada.")
print("-="*30)

input("Clique no ENTER para sair")