numero = (int(input('Digite Um Numero: ')),
    int(input('Digite Outro Numero: ')),
    int(input('Digite Mais Outro Numero: ')),
    int(input('Digite O Ultimo Numero: ')))



if 3 in numero:
    print(f'O numero 3 apareceu na posicao {numero.index(3)+1}')
else:
    print('O Numero 3 Apareceu em nenhuma posicao.')

print(f'O numero 9 aparece {numero.count(9)} vezes')
print(f'Voce Digitou Os Valores {numero}')
print(f'Os valores pares foram ', end='')

for n in numero:
    if n % 2 == 0:
        print(n, end=' ')
        