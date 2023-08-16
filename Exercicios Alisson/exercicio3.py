
def encontrar_posicao(valor, vetor):
    for i, v in enumerate(vetor):
        if v == valor:
            return i
    return -1
vetor = []
for i in range(5):
    valor = int(input("Digite o valor para a posição {}: ".format(i)))
    vetor.append(valor)
x = int(input("Digite o valor 'x' que deseja procurar: "))
posicao_x = encontrar_posicao(x, vetor)
if posicao_x != -1:
    print("O valor", x, "aparece pela primeira vez na posição:", posicao_x)
else:
    print("O valor", x, "não foi encontrado no vetor. Resultado: -1")
