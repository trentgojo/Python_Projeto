print("<<<DADOS ESCOLAR>>>")

#DADOS DO ALUNO
nome=input("Digite um funcionario: ")
empresa=input("Digite a instituicao: ")
qtdefuncionarios=int(input("Digite a quantidade de funcionarios: "))
valormensalidade=float(input("Digite o valor da mensalidade: "))
print("-="*30)

#IMPRESSÃO DOS DADOS
print(nome,"trabalha na empresa",empresa)
print("O valor da mensalidade é de R$",str(valormensalidade),"reais")
print("A soma de três meses de mensalidade é R$",valormensalidade * 3, "reais")

#TIPOS DE DADOS
print("-="*30)
print("==============Verifique os tipos de dados abaixo==============")
print("O tipo de dado da variavel [nome] é:",type(nome))
print("O tipo de dado da variavel [empresa] é:",type(empresa))
print("O tipo de dado da variavel [qtdefuncionarios] é:",type(qtdefuncionarios))
print("O tipo de dado da variavel [valormensalidade] é:",type(valormensalidade))
print("-="*30)
input("Clique para sair")