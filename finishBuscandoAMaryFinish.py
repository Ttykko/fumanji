# creamos el menu 

print("bienvenidos a fumanji, juego para fumar ")

menuPrincipal = input("menu principal: \n 1. ingresar al juego \n 2. salir \n")

while menuPrincipal != 2:

    if menuPrincipal == '1':

        # Creamos el mapa con las posiciones en una lista

        map = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ]


        # Identificar a los jugadores

        playerOne = str( input( "INGRESE NOMBRE DEL PRIMER JUGADOR:   " ) )

        playerTwo = str( input( "INGRESE NOMBRE DEL SEGUNDO JUGADOR:   " ) )

        playerThree = str( input( "INGRESE NOMBRE DEL TERCERO JUGADOR:   " ) )

        playerFour = str( input( "INGRESE NOMBRE DEL CUARTO JUGADOR:   " ) )

        # Generamos una lista vacia a cada jugador las cueles tendran que almacenar distintos objetos durante la partida.

        playerOneList = []
        playerTwoList = []
        playerThreeList = []
        playerFourList = []

        # Cremos funcion para simular un dado de 6 caras

        import random
      #funcion de tirar dado y obtener un numero al azar
        def rollDice():
            randomNumber = random.randint(1, 6)
            print("el valor del dado es: ", randomNumber)
            return randomNumber
# funcion que retorna un objeto de la lista objetos al azar
        def randomObject():
            randomNumber = random.randint(0, 6)
            return objects[randomNumber]

#funcion que compara la listra de objetos con la lista del jugador, retorna true o false
        def compareLists( playerList, objects ):

            for object in objects:
                try:
                    resp = playerList.index(object)
                except:
                    return False

            return True

        def trap( positionPlayer, playerList ):
            randomNumber = random.randint(0, 2)
            if randomNumber == 0:
                print("Has caido en la trampa de retroceder 1 espacio")
                positionPlayer = positionPlayer - 1

            if randomNumber == 1:
                print("Has caido en el pastero, te ha quitado tu primer objeto")
                if len(playerList) >= 0:
                    playerList.pop(0)
                    

                else:
                    print("Te has salvado por que no tienes ningun objeto, pero te apuñalo")

            if randomNumber == 2:
                print("Has caido en el angel de la guarda, avanza un espacio")
                positionPlayer = positionPlayer + 1

            return [ positionPlayer, playerList ]

       

        objects = [ "MOLEDOR", "SMOKING", "ENCENDEDOR", "BOQUILLA", "PIPA", "REJILLA", "WEED" ]

        # Comenzamos el juego

        # Asignamos posicion inicial en 0 de cada jugador.

        positionPlayerOne = int(0)
        positionPlayerTwo = int(0)
        positionPlayerThree = int(0)
        positionPlayerFour = int(0)

        print("***** COMENZANDO JUEGO *****")
        

        while True:

            # PLAY PLAYER UNO

            input("Jugador UNO lanze su dado (press enter)")
            positionPlayerOne = positionPlayerOne + rollDice()

            if positionPlayerOne >= 17:
                positionPlayerOne = int(1)

            print("El jugador numero UNO quedo en la posicion ", positionPlayerOne)

        
            # Asignamos el objeto a la lista del jugador

            playerOneList.append(randomObject())

            print("LISTA DEL JUGADOR UNO:  ", playerOneList)

            # Llamamos a la trampa
            resultado =  trap( positionPlayerOne, playerOneList )
            positionPlayerOne = resultado[0]
            playerOneList = resultado[1]

            # Imprimimos nueva posicion y lista del jugador
            print("Nueva posicion del jugador ", positionPlayerOne)
            print("Nueva lista del jugador ", playerOneList)

            resultCompare = compareLists( playerOneList, objects )
                
            if resultCompare == True:
                print("ENHORABUENA CAMARADA, EL JUGADOR UNO HA OBTENIDO EL GOLDEN KUSH!!!")
                break

            # PLAY PLAYER DOS

            input("Jugador DOS lanze su dado (press enter)")
            positionPlayerTwo = positionPlayerTwo + rollDice()

            if positionPlayerTwo >= 17:
                positionPlayerTwo = int(0)

            print("El jugador numero DOS quedo en la posicion ", positionPlayerTwo)

            # Asignamos el objeto a la lista del jugador

            playerTwoList.append(randomObject())

            print("LISTA DEL JUGADOR DOS:  ", playerTwoList)

            # Llamamos a la trampa
            resultado =  trap( positionPlayerTwo, playerTwoList )
            positionPlayerTwo = resultado[0]
            playerTwoList = resultado[1]

            # Imprimimos nueva posicion y lista del jugador
            print("Nueva posicion del jugador ", positionPlayerTwo)
            print("Nueva lista del jugador ", playerTwoList)

            resultCompare = compareLists( playerTwoList, objects )

            if resultCompare == True:
                print("ENHORABUENA CAMARADA, EL JUGADOR DOS HA OBTENIDO EL GOLDEN KUSH!!!")
                break

            # PLAY PLAYER TRES

            input("Jugador TRES lanze su dado (press enter)")
            positionPlayerThree = positionPlayerThree + rollDice()

            if positionPlayerThree>= 17:
                positionPlayerThree = int(0)

            print("El jugador numero TRES quedo en la posicion ", positionPlayerThree)

            # Asignamos el objeto a la lista del jugador

            playerThreeList.append(randomObject())

            print("LISTA DEL JUGADOR TRES:  ", playerThreeList)

            # Llamamos a la trampa
            resultado =  trap( positionPlayerThree, playerThreeList )
            positionPlayerThree = resultado[0]
            playerThreeList = resultado[1]

            # Imprimimos nueva posicion y lista del jugador
            print("Nueva posicion del jugador ", positionPlayerThree)
            print("Nueva lista del jugador ", playerThreeList)

            resultCompare = compareLists( playerThreeList, objects )

            if resultCompare == True:
                print("ENHORABUENA CAMARADA, EL JUGADOR TRES HA OBTENIDO EL GOLDEN KUSH!!!")
                break

            # PLAY PLAYER CUATRO

            input("Jugador CUATRO lanze su dado (press enter)")
            positionPlayerFour = positionPlayerFour + rollDice()

            if positionPlayerFour >= 17:
                positionPlayerFour = int(0)


            print("El jugador numero CUATRO quedo en la posicion ", positionPlayerFour)

            # Asignamos el objeto a la lista del jugador

            playerFourList.append(randomObject())

            print("LISTA DEL JUGADOR CUATRO:  ", playerFourList)

            # Llamamos a la trampa
            resultado =  trap( positionPlayerFour, playerFourList )
            positionPlayerFour = resultado[0]
            playerFourList = resultado[1]

            # Imprimimos nueva posicion y lista del jugador
            print("Nueva posicion del jugador ", positionPlayerFour)
            print("Nueva lista del jugador ", playerFourList)

            resultCompare = compareLists( playerFourList, objects )

            if resultCompare == True:
                print("ENHORABUENA CAMARADA, EL JUGADOR CUATRO HA OBTENIDO EL GOLDEN KUSH!!!")
                break
    else:
        print("adios, fin del juego")
    break    

    
    
    

    

   



