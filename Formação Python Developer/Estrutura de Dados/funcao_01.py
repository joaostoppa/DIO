def exibir_mensagem():
    print("Olá mundo!")

# Não declara o valor nome, precisa declarar depois na exe da função
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

# Já declara o valor de nome, fica opcional a declaração na exe da função. Obs: Se declarar um valor diferente, é substituido
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")