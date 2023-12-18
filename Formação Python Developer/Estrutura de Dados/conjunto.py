conjunto_a = {1, 2, 3}
conjunto_b = {4, 5}

conjunto_a.union(conjunto_b) # {1, 2, 3, 4} - Une os dois conjuntos


conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b) # {2, 3} - Numero que está nos dois conjuntos


conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4} - Retorna apenas o que não existe no outro conjunto


conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b) # {1, 4} - Retorna o que existe apenas em um dos dois conjuntos


conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) # True Todos os elementos de A, pertencem a B
conjunto_b.issubset(conjunto_a) # False Os elementos de B não pertencem a A



conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b) # False Os elementos de B não estão todos em A
conjunto_b.issuperset(conjunto_a) # True Os elementos de A estão todos em B




conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}
# Não se tocam, os elementos não estão presentes no outro
conjunto_a.isdisjoint(conjunto_b) # True
conjunto_a.isdisjoint(conjunto_c) # False



sorteio = {1, 23}
# Adiciona um elemento passado ao conjunto, porém não acontece nada se ele já existir
sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42} 
sorteio.add(25) # {1, 23, 25, 42}


teste = {1, 4, 6, 7}
# Limpa os elemntos 
teste.clear() # {}



copia = {3, 56, 76}
# Copia o conjunto
copia.copy() # {3, 56, 76}



numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
# Descarta um elemento passado
numeros.discard(1)
numeros.discard(45) # Se o elemento não existir, não aconltece nada



numeros1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
# Descarta o primeiro valor
numeros1.pop()



numeros2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
# remove o elemento passado
numeros2.remove(0) #0



numeros3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
# Tira o tamanho do conjunto 
len(numeros3) 



