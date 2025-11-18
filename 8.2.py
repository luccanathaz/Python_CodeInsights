# @cikey 2cd86f11bd3b3df9adea2383f79e8846
# @sid 20251174010030
# @aid V8.2

numero_de_linhas = 0

with open('texto5.txt', 'r') as arquivo:
    for linha in arquivo:
        numero_de_linhas += 1
print(f"O arquivo tem {numero_de_linhas} linhas")