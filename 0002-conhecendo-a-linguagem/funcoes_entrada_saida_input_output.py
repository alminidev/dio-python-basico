nome = input("informe o seu nome: ")
idade = input("informe a sua idade: ")

print(nome, idade)

# a aplicação do end significa que no final pode ser algo no final e o "\n" significa quebra de linha
print(nome, idade, end="...\n")

# a aplicação do sep significa que pode ser algo para separa o texto
print(nome, idade, sep="#")

print(nome, idade, sep="#", end="...\n")
