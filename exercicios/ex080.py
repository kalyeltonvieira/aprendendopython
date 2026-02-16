lista = []
for c in range(0,5):
    n = int(input('DIGITE O VALOR: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('ADICIONADO NO FINAL DA LISTA')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'ADICIONADO NA POSICAO {pos} DA LISTA')
                break
            pos +=1

print('=' * 30)
print(f'OS VALORES DIGITADOS FORAM {lista}')
print('=' * 30)

