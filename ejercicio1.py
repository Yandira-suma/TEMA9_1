países = input("Introduce una lista de países separados por comas: ")
países_lista = países.split(',')
países_ordenados = sorted(list(set(países_lista)))
print(', '.join(países_ordenados))