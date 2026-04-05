def inicializar_tabla(tabla, rounds):
    for p in rounds[0]["scores"]: #incializo la tabla con los participantes, e inicianlizo todos los valores en 0
        tabla[p] = {
            "total" : 0,
            "ganadas": 0,
            "mejor" : 0,
            "rondas" : 0
        }


def calcular_puntaje (jueces) :
    return sum(jueces.values()) #suma los puntajes de los jueces para un participante en una ronda

def retornar_ganador (players):
    act=0
    max=-1
    ganador=""
    for p in players:
        jueces=players[p]
        act = calcular_puntaje(jueces) 
        if act > max :
            max = act
            ganador = p
    return ganador, max #retorna el participante ganador y su puntaje total en esa ronda

def actualizar_tabla(tabla, ronda, ganador):
    for p in ronda["scores"] :
        jueces = ronda["scores"][p]
        puntaje = calcular_puntaje(jueces)

        tabla[p]["total"] += puntaje #actualizo el puntaje total

        if puntaje > tabla[p]["mejor"] :
            tabla[p]["mejor"] = puntaje #actualizo el valor de la mejor ronda
        
        tabla[p]["rondas"] += 1 #actualizo cantidad de rondas para luego calcular el promedio

    tabla[ganador]["ganadas"] += 1 #actualizo la cantidad de rondas ganadas al ganador
        

def imprimir_tabla(tabla):
     aux = ""
     ordenados = sorted(tabla, key=lambda x: tabla[x]['total'], reverse=True) #ordena la tabla por el total de sus puntos, reverse hace que quede de mayor a menor        
     for p in ordenados:
        aux += (
                f"Participante: {p}, "
                f"puntaje: {tabla[p]['total']}, "
                f"rondas ganadas: {tabla[p]['ganadas']}, "
                f"mejor ronda: {tabla[p]['mejor']}, "
                f"promedio: {tabla[p]['total']/tabla[p]['rondas']:.2f}\n"
                )
     return aux


