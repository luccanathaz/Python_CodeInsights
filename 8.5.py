# @cikey 2cd86f11bd3b3df9adea2383f79e8846
# @sid 20251174010030
# @aid V8.5

contatos = []

def adicionar_contato():
    nome = input("Fale o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    contatos.append({"nome": nome, "telefone": telefone})
    print(f"Contato {nome} foi adicionado\n")

def ver_contato():
    nome = input("Fale o nome para buscar: ")
    encontrado = False
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            print(f"Telefone de {contato['nome']}: {contato['telefone']}\n")
            encontrado = True
            break
    if not encontrado:
        print("Contato não encontrado\n")

def ler_contato_em_arquivo():
    try:
        with open('teste.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print("Contato salvo:\n")
            print(conteudo)
    except FileNotFoundError:
        print("Nenhum arquivo encontrado\n")

def salvar_contato_em_arquivo():
    with open('teste.txt', 'a', encoding='utf-8') as arquivo:
        print('Escreva abaixo as informações do contato:')
        nome = input('nome: ')
        telefone = input('telefone: ')
        arquivo.write(f"{nome} - {telefone}\n")
        print(f"Contato {nome} foi salvo no arquivo\n")

while True:
    print("CONTATOS")
    print("1 - Adicionar")
    print("2 - Procurar")
    print("3 - Ler contato salvo em arquivo")
    print("4 - Salvar contato em arquivo")
    print("5 - Sair")
    escolha = input("Escolha 1, 2, 3, 4 ou 5: ")

    if escolha == '1':
        adicionar_contato()
    elif escolha == '2':
        ver_contato()
    elif escolha == '3':
        ler_contato_em_arquivo()
    elif escolha == '4':
        salvar_contato_em_arquivo()
    elif escolha == '5':
        break
    else:
        print('Erro! escolha um dos números mostrados\n')


    escolha = input(":")

    if escolha == '1':
        adicionar_contato()
    elif escolha == '2':
        ver_contato()
    elif escolha == '3':
        ler_contato_em_arquivo()
    elif escolha == '4':
        salvar_contato_em_arquivo
    elif escolha == '5':
        break
    else:
        print('Erro! escolha um dos números mostrados')
        
    