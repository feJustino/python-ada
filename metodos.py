lista = [1,3,12,8,2]

print("Lista original", lista)

#append - Append object to the end of the list.

lista.append(3)

print("Lista depois do append", lista)

#insert - Insert object before index(param).

lista.insert(2, 32)

print("Lista depois do insert", lista)

#extend - Extend list by appending elements from the iterable.


lista2 = [23, 8, 50]

lista.extend(lista2)

print("Lista depois do extend", lista)

#pop - Remove and return item at index (default last).

lista.pop()

print("Lista depois do pop", lista)

#remove - Remove first occurrence of value.

lista.remove(3)

print("Lista depois do remove", lista)

#count - Return number of occurrences of value.

lista.count(3)

print("count do valor 3:", lista.count(3))
print("count do valor 8:", lista.count(8))

#index

lista.index(12)

print("index do valor 12:", lista.index(12))

#sort - Sort the list in ascending order and return None.

lista.sort()

print("Lista depois do sort:", lista)
print("index do valor 12:", lista.index(12))

lista.sort(reverse=True)

print("Lista depois do sort com reverse = true:", lista)
print("index do valor 12:", lista.index(12))

#funções

#len() - Return the number of items in a container.

print("Retorna o tamanho da lista", len(lista))

#sum()

print("Retorna a somas dos valores",sum(lista))

#max()  - return its biggest item

print("Retorna o maior item da lista", max(lista))

#min() - return its smallest item

print("Retorna o menor item da lista", min(lista))