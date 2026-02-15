valor = []
for c in range(1,6):
    valor.append(int(input(f'DIGITE O {c} VALOR: ')))
print(f'OS VALORES LISTADOS FORAM {valor}')

maior = max(valor)
menor = min(valor)

print(f'O MAIOR VALOR FOI {maior} NA POSIÇÂO ', end='')
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i+1}...', end='')

print(f'\nO MENOR VALOR FOI {menor} NA POSIÇÃO ', end='')
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i+1}...', end='')
