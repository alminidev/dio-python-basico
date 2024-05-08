nome = "AlExAnDrE"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".")  # corta espaços em brancoS
print(texto.rstrip() + ".")  # corta espaços individualmente direita
print(texto.lstrip() + ".")  # corta espaços individualmente esquerda

menu = "Python"

print("####" + menu + "####")  # inclui caracteres calculado
print(menu.center(14))  # inclui espaços
print(menu.center(14, "#"))  # inclui caracteres sem calcular
print("-".join(menu))  # inclui caracteres em cada letra
