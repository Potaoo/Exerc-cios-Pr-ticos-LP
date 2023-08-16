
def contar_valores_diferentes(vetor):
    valores_unicos = set()
    for valor in vetor:
        valores_unicos.add(valor)
    return len(valores_unicos)
vetor = []
for i in range(10):
    valor = int(input("Digite o valor para a posição {}: ".format(i)))
    vetor.append(valor)
numero_valores_diferentes = contar_valores_diferentes(vetor)
print("Número de valores diferentes no vetor:", numero_valores_diferentes)
