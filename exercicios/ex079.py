numeros = list()
while True:
    n = int(input('DIGITE UM VALOR: '))
    if n not in numeros:
        numeros.append(n)
        print('VALOR ADICIONADO COM SUCESSO.')
    else:
        print('Valor Duplicado, Nao foi Possivel Adicionar...')
    r = str(input('Deseja Continuar?: ')).upper().strip()[0]
    if r in 'N':
        break
print('=' * 50)
numeros.sort()
print(f'voce digitou os valores {numeros}')
print('=' * 50)