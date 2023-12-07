list = []

list.append(1)
list.append("List")
list.append([3, 5, 6])

print(list)

#.append = Adicionar um elemento na lista


#list.clear()
print(list)

#.clear = Limpar uma lista


list.copy()
print(list)

#.copy = copiar uma lista


nomes = ["joao", "fernanda", "joao", "marisa", "luiz", "antonio", "fernanda", "fernanda", "luiz"]
print(nomes.count("fernanda"))

#.count = Conta quantas vezes um objeto da lista aparece


nomes.extend(["java", "c++"])
print(nomes)

#.extend = adiciona elementos no final da lista


print(nomes.index("java"))

#.index = mostra a primeira ocorrencia do objeto solicitado na lista


nomes.pop()
nomes.pop(1)

#.pop = remove o objeto que ocupa a ultima posição (Caso não passe um valor) remove por inidce da posição


nomes.remove("java")

#.remove = passa direto o objeto que quer remover


nomes.reverse()

#.reverse = transpoe sua lista


nomes.sort()
#Coloca em ordem alfabética

nomes.sort(reverse=True)
#Coloca no reverso de ordem alfabética

nomes.sort(key=lambda x: len(x))
#Conta o tamanho ocupado por cada objeto, e coloca eles em ordem crescente.


len(nomes)
#calcula o tamanho ocupado por cada elemento




