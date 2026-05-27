import sys

def ordenar_palabras(palabras,indices):
    resultado = [None] * len(palabras)   

    for i in range(len(palabras)):
        pos = indices[i] - 1          
        resultado[pos] = palabras[i]
    oracion = ' '.join(resultado)

    return oracion

nombre_archivo = sys.argv[1]

archivo = open(nombre_archivo, "r")

for linea in archivo:
    linea = linea.strip()
    if linea == "":
        continue
    
    partes = linea.split(";")
   
    palabras_str = partes[0].strip()
    palabras = palabras_str.split()
   
    indices_str = partes[1].strip()
    indices_texto = indices_str.split()
    
    indices = []
    for num in indices_texto:
        indices.append(int(num))
   
    oracion_final = ordenar_palabras(palabras, indices)
    print(oracion_final)


archivo.close()
