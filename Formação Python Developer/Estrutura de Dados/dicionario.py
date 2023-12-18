# Dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: {},
# e contém uma lista de pares chave:valor separadas por vírgulas.
# As chaves precisam ser valores imutáveis

pessoa = {"nome": "João", "idade": 27}
# Ou
pessoa = dict(nome="João", idade=27)
# Adicionando uma chave + Valor
pessoa["telefone"] = "3333-5678"

# Acessando os valores

exemplodict = {"nome": "João", "idade": 27, "telefone": "2222-4444"}

exemplodict["nome"] # João
exemplodict["nome"] # 27
exemplodict ["telefone"] # 2222-4444

# Acessando a chave e renomeando o valor
exemplodict["nome"] = "Maria"

# Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável como (string e números).

contatos = {
    "joao@gmail.com": {"nome": "João", "telefone": "1111-1111"},
    "fernanda@gmail.com": {"nome": "Fernanda", "telefone": "2222-2222"},
    "marco@gmail.com": {"nome": "Marco", "telefone": "3333-3333"},
    "luiz@gmail.com": {"nome": "Luiz", "telefone": "4444-4444"},
}
# Acessando 
contatos["joao@gmail.com"]["telefone"] # "1111-1111"

#Forma de iterar 
#for chave, valor in dicionario.intems():
