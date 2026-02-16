lista = []

while True:
    try:
        lista.append(int(input('DIGITE UM VALOR: ')))
    except ValueError:
        print('DIGITE UM NUMERO VALIDO!')
        continue

    continuar = str(input('Deseja Continuar?: [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        print('PROGRAMA FINALIZADO...')
        break

print('=' * 50)

if 5 in lista:
    print('O NUMERO 5 APARECE NA LISTA!')
else:
    print('O NUMERO 5 NAO APARECE NA LISTA')

print(f'OS NUMEROS SALVOS FORAM {lista}')
lista.sort()
print(f'OS VALORES EM ORDEM CRESCENTE SÂO {lista}')
lista.sort(reverse=True)
print(f'OS VALORES EM FORMA DECRESCENTE SAO {lista}')
print(f'FORAM DIGITADOS {len(lista)} NUMEROS')
if lista:
    print(f'O MAIOR VALOR SERA {max(lista)}')
    print(f'O MENOR VALOR SERA {min(lista)}')
else:
    print('NENHUMA LISTA FOI ADICIONADA')
print('=' * 50)