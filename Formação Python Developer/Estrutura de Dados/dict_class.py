# {}.formkeys
dict.fromkeys(["nome", "telefone"]) # Cria chaves no dicionário sem passar o valor, fica com valor none #{"nome": none, "telefone": none}
dict.fromkeys(["nome", "telefone"], "vazio") # Cria um conjunto de chaves, e coloca um valor padrão nelas #{"nome": "vazio", "telefone": "vazio"}


# {}.get # Busca chaves no dicionário
contatos = {
    "joaopaulo@gmail.com": {"nome": "João", "telefone": "2121-2121"}
}
contatos.get("chave") # None
contatos.get("chave", {}) #{} Define o retorno quando não encontra o elemento
contatos.get("joaopaulo@gmail.com", {}) #{ "joaopaulo@gmail.com": {"nome": "João", "telefone": "2121-2121"}}


# {}.keys # Retorna uma lista com apenas as chaves
contatos1 = {
    "joaopaulo@hotmail.com": {"name": "João Paulo", "celular": "2121-9999"}
}
contatos1.keys() # disct_keys(['joaopaulo@hotmail.com'])


# {}.setdefault Se o atributo existir no dicionário, ele retorna o valor. Se não existir, ele cria com a chave e vaor declarado
dicionario = {'nome': 'Juan', 'telefone': '2121-2121'}

dicionario.setdefault("nome", "Fernanda") # "Juan" Como a chave nome existe, ele mantém 
dicionario.setdefault("idade", 27) # 27 Como a chave não existe, é criada com o valor declarado


# {}.update Atualiza o dicionário com outro dicionário
contatos2 = {
    "joaopaulo@hotmail.com": {"name": "João Paulo", "celular": "2121-9999"}
}
contatos2.update({"joaopaulo@gmail.com": {"name": "João"}}) # {'joaopaulo@gmail,com': {'name': João}}
contatos2.update({"lula@gmail.com": {"name": "Lula", "telefone": "2123-5678"}}) # {'joaopaulo@gmail,com': {'name': João}}{"lula@gmail.com": {"name": "Lula", "telefone": "2123-5678"}


# {}.values Retorna apenas os valores amarrados as chaves
contatos3 = {
    "joaopaulo@hotmail.com": {"name": "João Paulo", "celular": "2121-9999"}
}
contatos3.values() # {"name": "João Paulo", "celular": "2121-9999"}


# in verifica se o valor é uma chave dentro de um dicionário
contatos4 = {
    "joaopaulo@hotmail.com": {"name": "João Paulo", "celular": "2121-8888"},
    "joaopedro@hotmail.com": {"name": "João Pedro", "celular": "2121-7777"},
    "joaolucas@hotmail.com": {"name": "João Lucas", "celular": "2121-6666"},
}
"joaopaulo@hotmail.com" in contatos4 # True



