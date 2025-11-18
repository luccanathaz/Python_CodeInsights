# @cikey 2cd86f11bd3b3df9adea2383f79e8846
# @sid 20251174010030
# @aid V5.1


#begin_inputs

#end_inputs
peso_total = 0
while True:
    p = input()
    if peso_total + p >= 500:
        print("Peso excedido")
        break
    peso_total += p