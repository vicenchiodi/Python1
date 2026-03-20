import random
palabras = {
    "animales": ["gato", "perro", "elefante", "zorrino"],
    "deportes": ["futbol", ]

}
categoria_seleccionada = ""
while(not categoria_seleccionada):
    num_categoria = input("Selecciona categoria: 1: animales.     2: deportes")
    if(num_categoria == "1"):
        categoria_seleccionada = "animales"
    elif(num_categoria=="2"):
        categoria_seleccionada="deportes"

        


word = random.choice(palabras[categoria_seleccionada])
guessed = []
attempts = 6
ok = True
puntaje=0


print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
# Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
# Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        print("Puntaje de la partida: ", puntaje+6)
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ")
    ok=False
    while(ok==False):
        if(len(letter)!=1) or (not letter.isalpha()): #nombre_de_variable.isalphaee checkea que sea una letra 
            print("el carcacter ingresado no es valido.")
            letter = input("Ingresá una letra: ")
        else:
            ok=True

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntaje-=1
        print("Esa letra no está en la palabra.")
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    puntaje=0
    print("El puntaje de la partida es: ",puntaje)