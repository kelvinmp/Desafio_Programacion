# lista = ["Cabernet Merlot Noir | ot"]

# Separar por lineas 
# Se parar cadena inicial usando | como separador
# Separar primera parte en palabras separadas
# Comparar cada palabra con ot:
    #recorrer toda la palabra buscando una letra específica de la pista, si laa tiene, sigo, sino, false
    #si efectivamente la tiene, pruebo con la siguiente letra de la pista y así hasta cubrirlas todas como correctas
    # Contar letras en cada lado a ver si se repite la misma cantidad de veces en el otro lado
    #guardar dicha palabra si si tiene


vinos = ["Cabernet", "Merlot", "Noir"] 
recuerdo = "ot"

resultado = []   

for vino in vinos:
    bandera = True
    for letra in recuerdo:
        if vino.count(letra) < recuerdo.count(letra):
            bandera = False
            break
    if bandera:
            resultado.append(vino)

print(", ".join(resultado))



