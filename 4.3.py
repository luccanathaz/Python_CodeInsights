# @cikey 2cd86f11bd3b3df9adea2383f79e8846
# @sid 20251174010030
# @aid V4.3


#begin_inputs
mes = int(input(""))
#end_inputs
meses = ["","janeiro", "fevereiro", "marco","abril","maio","junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
if 1 <= mes <= 12:
    print(meses[mes])
else:
    print("mes invalido")