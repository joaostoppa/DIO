nome = "João Paulo"
idade = 27
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 27}

print("nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(idade, nome))

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} nome: {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")

