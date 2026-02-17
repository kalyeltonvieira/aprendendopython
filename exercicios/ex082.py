numeros: list[int] = []

while True:
    numeros.append(int(input("Digite um valor: ")))


    if input("Continuar? [S/N]: ").strip().upper()[0] == "N":
        break

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 1 == 0]

print(f'Numeros {numeros}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')