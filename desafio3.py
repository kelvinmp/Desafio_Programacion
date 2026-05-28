import sys

def contar_combinaciones(monto, monedas=[1, 5, 10, 25, 50]):
    
    lista = [0] * (monto + 1)
    
    lista[0] = 1
    
    for moneda in monedas:
        for i in range(moneda, monto + 1):
            lista[i] += lista[i - moneda]
            
    return lista[monto]

nombre_archivo = sys.argv[1]
archivo = open(nombre_archivo, "r")

for linea in archivo:
    linea = linea.strip()
    if linea == "":
        continue  

    monto_centavos = 0    
    monto_centavos = int(linea)
    
    total = contar_combinaciones(monto_centavos)
    print(f"Número total de combinaciones para {monto_centavos} centavos es: {total}")

    
archivo.close()


