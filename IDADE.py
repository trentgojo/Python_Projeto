print("<<<IDADE>>>")

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
prioridade="NAO"
if idade>=65:
    prioridade="SIM"
print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)