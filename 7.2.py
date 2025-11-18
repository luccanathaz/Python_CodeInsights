# @cikey 2cd86f11bd3b3df9adea2383f79e8846
# @sid 20251174010030
# @aid V7.2

def adivinhou(letras, palavra):
    for letra in palavra:
        if letra not in letras:
            return False
    return True
#begin_inputs
letras = input('').split()
palavra = input("")
#end_inputs
print(adivinhou(letras, palavra))
