# Lista para armazenar os cadastros
cadastros = []

# Função para cadastrar uma nova pessoa
def cadastrar_pessoa():
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    endereco = input("Digite o endereço: ")

    # Verifica se o CPF já está cadastrado
    for pessoa in cadastros:
        if pessoa['cpf'] == cpf:
            print("CPF já cadastrado!")
            return

    # Adiciona os dados à lista de cadastros
    cadastros.append({'nome': nome, 'cpf': cpf, 'endereco': endereco})
    print("Cadastro realizado com sucesso!")

# Função para visualizar todos os cadastros
def visualizar_cadastros():
    if not cadastros:
        print("Nenhum cadastro encontrado.")
    else:
        print("\n--- Cadastros ---")
        for pessoa in cadastros:
            print(f"Nome: {pessoa['nome']}, CPF: {pessoa['cpf']}, Endereço: {pessoa['endereco']}")

# Menu principal
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar pessoa")
        print("2. Visualizar cadastros")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_pessoa()
        elif opcao == '2':
            visualizar_cadastros()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    menu()