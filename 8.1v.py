# @cikey 2cd86f11bd3b3df9adea2383f79e8846
# @sid 20251174010030
# @aid V8.1

def abrir_arquivo():
    with open('texto.txt', 'w', encoding= 'utf-8') as arquivo:
        print("Escreva abaixo")
        arquivo.write(input(": "))
def ler_arquivo():
    with open('texto.txt', 'r') as arquivo:
        print('Leia o arquivo abaixo')
        conteudo = arquivo.read()
    print(conteudo)

print('Escolha oque vai fazer no arquivo. Ler ou Escrever?')

escolha = input(":").lower().strip()

if escolha == 'ler':
    ler_arquivo()
elif escolha == 'escrever':
    abrir_arquivo()
else:
    print('Escolha ler ou escrever no arquivo!')
    exit()