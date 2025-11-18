# @cikey 2cd86f11bd3b3df9adea2383f79e8846
# @sid 20251174010030
# @aid V8.3

with open('arquivo1.txt', 'r') as origem, open('arquivo2.txt', 'w') as destino:
    for linha in origem:
        destino.write(linha)
    print('texto copiado com sucesso')