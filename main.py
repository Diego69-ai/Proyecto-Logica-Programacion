import random  # Importa la función random para que la computadora elija al azar

print("Bienvenido al juego Piedra, Papel o Tijera")

jugar = "si"

# Bucle principal que se repite mientras el usuario quiera jugar
while jugar == "si":
    print("Elige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

    jugador = input("Tu elección (1, 2 o 3): ")

    # La computadora elige al azar un número entre 1 y 3
    computadora = str(random.randint(1, 3))

    # Mostrar qué eligió la computadora
    if computadora == "1":
        print("La computadora eligió: Piedra")
    elif computadora == "2":
        print("La computadora eligió: Papel")
    else:
        print("La computadora eligió: Tijera")

    # Comparación de elecciones para determinar el resultado
    if jugador == computadora:
        print("Empate")
    elif jugador == "1" and computadora == "3":
        print("Ganaste")
    elif jugador == "2" and computadora == "1":
        print("Ganaste")
    elif jugador == "3" and computadora == "2":
        print("Ganaste")
    elif jugador == "1" or jugador == "2" or jugador == "3":
        print("Perdiste")
    else:
        print("Opción inválida")

    # Pregunta si quiere jugar otra vez
    jugar = input("¿Quieres jugar otra vez? (si/no): ")
