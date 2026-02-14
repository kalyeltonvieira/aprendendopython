lista = ('APRENDER', 'CURSO', 'PYTHON', 'GUANABARA', 'PROGRAMAR', 'LINGUAGEM', 'GRATIS', 'ESTUDAR',
         'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
vogais = 'AEIOU'

for palavra in lista:
    print(f'\nNA PALAVRA {palavra}: ', end='')
    
    tem_vogal = False

    for letra in palavra:
        if letra.upper() in vogais:
            print(letra, end=' ')
            tem_vogal = True

    if not tem_vogal:
        print('NAO TEM VOGAIS')

