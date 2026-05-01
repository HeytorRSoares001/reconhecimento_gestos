def calcular_estatisticas(lista_numeros):

    soma_total = sum(lista_numeros)
    media = soma_total / len(lista_numeros)
    maior_numero = max(lista_numeros)
    menor_numero = min(lista_numeros)

    return soma_total, media, maior_numero, menor_numero


numeros = [23, 7, 45, 2, 67, 12]

resultado = calcular_estatisticas(numeros)

print(resultado)
