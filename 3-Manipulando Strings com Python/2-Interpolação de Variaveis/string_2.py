nome = "Alexandre"
idade = 50
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

print("Nome: %s Idade: %d" % (nome, idade))  # Old Style % - Não é mais usado

print("Nome: {} Idade: {}".format(nome, idade))  # Método Format

print("Nome: {1} Idade: {0}".format(idade, nome))  # Método Format

print("Nome: {1} Idade: {0} Nome: {1} {1}".format(
    idade, nome))  # Método Format


print("Nome: {nome} Idade: {idade}".format(
    nome=nome, idade=idade))  # Método Format

print("Nome: {name} Idade: {age} {name} {name} {age}".format(
    age=idade, name=nome))  # Método Format

print("Nome: {nome} Idade: {idade}".format(**dados))  # Método Format


print(f"Nome: {nome} Idade: {idade}")  # f-string

# f-string utilizando Idef(0) e (número de casas decimais)
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
# f-string utilizando Idef(10) e (número de casas decimais)
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")
