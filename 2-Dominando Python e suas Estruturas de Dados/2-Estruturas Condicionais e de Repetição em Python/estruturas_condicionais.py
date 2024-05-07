# EXEMPLOS DE IF
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade:"))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

# EXEMPLOS DE IF, ELSE
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

else:
    print("Ainda não pode tirar a CNH.")

# EXEMPLOS DE IF, ELIF, ELSE
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas e não as práticas")
else:
    print("Ainda não pode tirar a CNH.")
