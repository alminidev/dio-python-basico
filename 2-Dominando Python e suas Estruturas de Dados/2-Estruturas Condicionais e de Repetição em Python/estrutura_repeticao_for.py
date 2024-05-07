texto = input("Informe um texto:")
VOGAIS = "AEIOU"

# EXEMPLO FOR ITERÁVEL
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Executa no final do laço")

# EXEMPLO TABUADA com BULT-IN RANGE (START, STOP , STEP)
for numero in range(0, 51, 5):
    print(numero, end=" ")

print()  # QUEBRA DE LINHA

for numero in range(0, 31, 3):
    print(numero, end=" ")
