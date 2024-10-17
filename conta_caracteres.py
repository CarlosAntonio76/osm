def conta_caracteres(s):
    """
    Faça uma função que conte quantos caracteres de uma string

    >>> frase 'banana'

    """

    caracteres_ordenados = sorted(s)
    caracter_anterior = caracteres_ordenados[0]

    contagem = 1

    for caractere in caracteres_ordenados[1:]:
        if caractere == caracter_anterior:
            contagem += 1
        else:
            print(f'Contagem é: {caracter_anterior}: {contagem}')
            caracter_anterior = caractere
            contagem = 1
    print(f'Contagem é: {caracter_anterior}: {contagem}')


if __name__=="__main__":
    conta_caracteres('paralelepipedo')

