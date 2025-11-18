# @cikey 2cd86f11bd3b3df9adea2383f79e8846
# @sid 20251174010030
# @aid V7.4

contatos = []

def adicionar_contato():
    nome = input("Fale o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    contatos.append({"nome": nome, "telefone": telefone})
    print(f"Contato {nome} foi adicionado")

def ver_contato():
    nome = input("Fale o nome para buscar: ")
    encontrado = False
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            print(f"Telefone de {contato['nome']}: {contato['telefone']} \n")
            encontrado = True
            break
        if not encontrado:
            print("Contato não encontrado \n")
while True:
    
    print("CONTATOS")
    print("1 - Adicionar")
    print("2 - Procurar")
    print("3 - Sair")

    print("Escolha 1, 2 ou 3")

    escolha = input(":")

    if escolha == '1':
        adicionar_contato()
    elif escolha == '2':
        ver_contato()
    elif escolha == '3':
        exit()
    else:
        print('Escolha errada tente de novo')
    