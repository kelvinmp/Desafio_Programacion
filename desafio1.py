palabras = ["gusta", "Me", "helado", "comer", "mucho"]
indices = [2, 1, 5, 4, 3]
resultado = [None] * len(palabras)   

for i in range(len(palabras)):
    pos = indices[i] - 1          
    resultado[pos] = palabras[i]

oracion = ' '.join(resultado)
print(oracion)
