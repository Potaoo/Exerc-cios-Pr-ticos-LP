
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, -52]
maior_elemento = max(lista)
menor_elemento = min(lista)
numeros_pares = [numero for numero in lista if numero % 2 == 0]
primeiro_elemento = lista[0]
ocorrencias_primeiro_elemento = lista.count(primeiro_elemento)
media_elementos = sum(lista) / len(lista)
soma_negativos = sum(numero for numero in lista if numero < 0)
print("a) Maior elemento:", maior_elemento)
print("b) Menor elemento:", menor_elemento)
print("c) Números pares:", numeros_pares)
print("d) Número de ocorrências do primeiro elemento:", ocorrencias_primeiro_elemento)
print("e) Média dos elementos:", media_elementos)
print("f) Soma dos elementos de valor negativo:", soma_negativos)
