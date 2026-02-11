# i need to make a sort numbers, but how to do it?
# first i need to think if is some randoms value
from random import randint

numeros = []

for _ in range(5):
    numeros.append(randint(0,11))
    
numeros = tuple(numeros)
print(f'OS VALORES SORTEADOS FORAM', *sorted(numeros))
print(f'o maior valor e {max(numeros)}')
print(f'o menor valor e {min(numeros)}')