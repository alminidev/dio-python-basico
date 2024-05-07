while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break  # Quando quer cortar a execução de uma exibição

    if numero % 2 == 0:
        continue  # Quando quer pular uma exibição

    print(numero)


# for numero in range(100):

#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")
