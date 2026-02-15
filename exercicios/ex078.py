valor = []
for c in range(0,5):
    valor.append(int(input(f'DIGITE O VALOR NA POSICAO {c}: ')))
print('=' * 50)
print(f'OS VALORES LISTADOS FORAM {valor}')
print('=' * 50)
maior = max(valor)
menor = min(valor)

print(f'O MAIOR VALOR FOI {maior} NA POSIÇÂO ', end='')
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i+1}...', end='')
print()
print(f'\nO MENOR VALOR FOI {menor} NA POSIÇÃO ', end='')
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i+1}...', end='')
