import random
def lancar_dado():
    return random.randint(1, 6)
num_lancamentos = 50
ocorrencias_face_6 = 0
for _ in range(num_lancamentos):
    resultado = lancar_dado()
    if resultado == 6:
        ocorrencias_face_6 += 1
percentual_face_6 = (ocorrencias_face_6 / num_lancamentos) * 100
print("Número de lançamentos:", num_lancamentos)
print("Número de ocorrências da face 6:", ocorrencias_face_6)
print("Percentual de ocorrências da face 6: {:.2f}%".format(percentual_face_6))
