def dec2bin():
    valor = int(input('número pra binário: '))
    listaBin = []

    while valor > 0:
        (valor, numBin) = divmod(valor, 2)
        listaBin.insert(0, numBin)

    print(listaBin)


dec2bin()
