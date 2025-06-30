usuario = input("Elige piedra, papel o tijera: ")

if usuario != "piedra" and usuario != "papel" and usuario != "tijera":
    print("Opción no válida")
else:
    maquina = "piedra"  # Cambia a "papel" o "tijera" para probar

    print("La máquina eligió:", maquina)

    if usuario == maquina:
        print("Empate")
    elif (usuario == "piedra" and maquina == "tijera") or \
         (usuario == "papel" and maquina == "piedra") or \
         (usuario == "tijera" and maquina == "papel"):
        print("¡Ganaste!")
    else:
        print("Perdiste")