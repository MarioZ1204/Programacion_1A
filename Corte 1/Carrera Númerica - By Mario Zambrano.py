import os
from random import randint

# funciones

def validplayers():
    global player, cont_par1, cont_par2, cont_par3, cont_par4, cont_ret1, cont_ret2, cont_ret3, cont_ret4, ac_d1, ac_d2, ac_d3, ac_d4, listplayers, player1, player2, player3, player4

    listplayers=[]
    player1=[]
    player2=[]
    player3=[]
    player4=[]

    cont_players=0

    cont_ret1=0
    cont_ret2=0
    cont_ret3=0
    cont_ret4=0
    
    cont_par1=0
    cont_par2=0
    cont_par3=0
    cont_par4=0

    ac_d1=0
    ac_d2=0
    ac_d3=0
    ac_d4=0

    os.system("cls")

    print("::::::::::::::::::::::::::::::::::::::::::::")
    print(":::            CARRERA NÚMERICA          :::")
    print("::::::::::::::::::::::::::::::::::::::::::::")
    
    estado = True
    while estado:
        print("¿Cuantos jugadores quieres en pista?")
        players = int(input("Ten en cuenta que deben ser al menos 2 y máximo 4\n"))

        if(players == 2 or players == 3 or players == 4):
            estado = False
        
        else:
            print("\n::: La cantidad de jugadores es incorrecta")
            key = input(". Presiona una tecla para ingresar de nuevo .")
            validplayers()

    for x in range (players):
        cont_players=cont_players+1
        listplayers.append(input(f"Jugador {cont_players} escribe tu nombre: \n"))

    menu()

def menu():

    global op

    os.system("cls")
    print("::::::::::::::::::::::::::::::::::")
    print(":::        MENÚ PRINCIPAL      :::")
    print("::::::::::::::::::::::::::::::::::")
    print("¿Que nivel deseas jugar?:")
    print("[1] Nivel básico (Tablero de 50 posiciones)")
    print("[2] Nivel intermedio (Tablero de 100 posiciones)")
    print("[3] Nivel avanzado (Tablero de 200 posiciones)")
    print("[4] Info")
    print("[5] Salir")
    
    op = int(input(". Ingresa una opción: "))
    
    if op == 1:
        basic()
    elif op == 2:
        inter()
    elif op == 3:
        avan()
    elif op == 4:
        infor()
    elif op == 5:
        print("°°° Has salido del juego °°°")
    else:
        print("°°° Opción incorrecta, intente nuevamente °°°")
        key = input("°°° Presiona una tecla para volver al menú °°°")
        menu()

#NIVELES
    
def basic():
    
    global positions
    
    os.system("cls")
    print("")
    print(":::::::::::::::::::::::::::::::::::::::::::")
    print("::::     BIENVENIDO AL NIVEL BÁSICO    ::::")
    print(":::::::::::::::::::::::::::::::::::::::::::")
    print("")
    key = input(". Presiona una tecla para tirar los dados .")

    positions=50

    juego()

def inter():

    global positions
    
    os.system("cls")
    print("")
    print(":::::::::::::::::::::::::::::::::::::::::::::")
    print(":::     BIENVENIDO AL NIVEL INTERMEDIO    :::")
    print(":::::::::::::::::::::::::::::::::::::::::::::")
    print("")
    key = input(". Presiona una tecla para tirar los dados .")

    positions=100

    juego()

def avan():

    global positions

    os.system("cls")
    print(":::::::::::::::::::::::::::::::::::::::::::")
    print(":::     BIENVENIDO AL NIVEL AVANZADO    :::")
    print(":::::::::::::::::::::::::::::::::::::::::::")
    key = input(".:: Presiona una tecla para lanzar los dados ::.")

    positions=200
    
    juego()

#INICIACION

def juego():
    global cont_par1, cont_par2, cont_par3, cont_par4, cont_ret1, cont_ret2, cont_ret3, cont_ret4, ac_d1, ac_d2, ac_d3, ac_d4, listplayers, player1, player2, player3, player4

    estado=True
    while estado :
        i = 0
        found = False
        while i < len(listplayers):
            found = True
            i = i + 1
# JUGADOR 1

        if(found):
            if ac_d1 >= positions-6:
                dice1=0
                dice2=0
                dice1=randint(1,6)            
        
                print(f"\n.                       {listplayers[0]} - Es tu turno!                     .")
                print("\nDado uno: ",dice1)

                ac_d1=ac_d1+dice1
                if ac_d1<=positions and (dice1 != 1 or dice2 !=1):
                    print(f"\n {listplayers[0]} Has avanzado {ac_d1} posiciones de {positions}")

            if ac_d1 < positions-6:
                dice1=0
                dice2=0

                dice1=randint(1,6)
                dice2=randint(1,6)

                print("")
                print(f"\n.                       {listplayers[0]} - Es tu turno!                     .")
                print("\nDado uno: ",dice1)
                print("Dado dos: ",dice2)   

                ac_d1=ac_d1+(dice1+dice2)
                if ac_d1<=positions and (dice1 != 1 or dice2 !=1):
                    print(f"\n {listplayers[0]} Has avanzado {ac_d1} posiciones de {positions}")
                        
            if dice1==1 and dice2==1:
                ac_d1=ac_d1-(dice1+dice2)
                ac_d1=ac_d1+21
                if ac_d1<positions:
                    print(f" {listplayers[0]} Has avanzado {ac_d1} posiciones de {positions}")
                elif ac_d1 > positions:
                    ac_d1=ac_d1-21
                    ac_d1=ac_d1+(dice1+dice2)          
                    print(f"\n {listplayers[0]} Has avanzado {ac_d1} posiciones de {positions}")          

            if ac_d1 == ac_d2 and ac_d1 < positions:
                ac_d2=ac_d2-ac_d2
                print(f"\n {listplayers[0]} chocó con  {listplayers[1]}")
                print(f" {listplayers[1]} Regresas al punto de inicio\n")  

            if len(listplayers) == 3:
                if ac_d1 == ac_d3 and ac_d1 < positions:
                    ac_d3=ac_d3-ac_d3
                    print(f"\n {listplayers[0]} chocó con  {listplayers[2]}")
                    print(f" {listplayers[2]} Regresas al punto de inicio\n")

            if len(listplayers) == 4:
                if ac_d1 == ac_d4 and ac_d1 < positions:
                    ac_d1=ac_d1-ac_d1
                    print(f"\n {listplayers[0]} chocó con  {listplayers[3]}")
                    print(f" {listplayers[3]} Regresas al punto de inicio\n")


            while ac_d1 > positions:  
                if True:
                    ac_d1=ac_d1-(dice1+dice2)
                    print(f"Te encuentras en la posición {ac_d1} de {positions}\n")
                    print("El resultado sobrepasa la cantidad de posiciones")
                    print(f" {listplayers[0]} Has perdido el turno\n")

                    break

            if dice1 == dice2:
                cont_par1=cont_par1+1
            else:
                cont_par1=0

            while dice1==dice2: 

                if ac_d1 >= positions-6:
                    dice1=0
                    dice2=0
                    dice1=randint(1,6)            
                    key = input(".:: Presiona una tecla para volver a tirar ::.")   
                    
                    print(f"\n.                       {listplayers[0]} - Es tu turno!                     .") 
                    print("\nDado uno: ",dice1)

                    ac_d1=ac_d1+dice1
                    if ac_d1<=positions and (dice1 != 1 or dice2 !=1):
                        print(f"\n {listplayers[0]} Has avanzado {ac_d1} posiciones de {positions}")

                if ac_d1 < positions-6:
                    dice1=0
                    dice2=0

                    dice1=randint(1,6)
                    dice2=randint(1,6)
                    key = input(".:: Presiona una tecla para volver a tirar ::.") 

                    print("")
                    print(f"\n.                       {listplayers[0]} - Es tu turno!                      .")
                    print("\nDado uno: ",dice1)
                    print("Dado dos: ",dice2)    

                    ac_d1=ac_d1+(dice1+dice2)
                    if ac_d1<=positions and (dice1 != 1 or dice2 !=1):
                        print(f"\n {listplayers[0]} Has avanzado {ac_d1} posiciones de {positions}")

                if dice1 == dice2:
                    cont_par1=cont_par1+1
                else:
                    cont_par1=0   

                if cont_par1==3 or ac_d1==positions:
                    fin()

                if dice1==1 and dice2==1:
                    ac_d1=ac_d1-(dice1+dice2)
                    ac_d1=ac_d1+21
                    if ac_d1<positions:
                        print(f" {listplayers[0]} Has avanzado {ac_d1} posiciones de {positions}")
                    elif ac_d1 > positions:
                        ac_d1=ac_d1-21
                        ac_d1=ac_d1+(dice1+dice2)          
                        print(f"\n {listplayers[0]} Has avanzado {ac_d1} posiciones de {positions}")

                if ac_d1 == ac_d2 and ac_d1 < positions:
                    cont_ret2=cont_ret2+1
                    ac_d2=ac_d2-ac_d2
                    print(f"\n {listplayers[0]} chocó con  {listplayers[1]}")
                    print(f" {listplayers[1]} Regresas al punto de inicio\n")  

                if len(listplayers) == 3:                
                    if ac_d1 == ac_d3 and ac_d1 < positions:
                        cont_ret3=cont_ret3+1
                        ac_d3=ac_d3-ac_d3
                        print(f"\n {listplayers[0]} chocó con  {listplayers[2]}")
                        print(f" {listplayers[2]} Regresas al punto de inicio\n")

                if len(listplayers) == 4:
                    if ac_d1 == ac_d4 and ac_d1 < positions:
                        cont_ret4=cont_ret4+1
                        ac_d1=ac_d1-ac_d1
                        print(f"\n {listplayers[0]} chocó con  {listplayers[3]}")
                        print(f" {listplayers[3]} Regresas al punto de inicio\n")

                while ac_d1 > positions:  
                    if True:
                        ac_d1=ac_d1-(dice1+dice2)
                        print(f"Te encuentras en la posición {ac_d1} de {positions}\n")
                        print("El resultado sobrepasa la cantidad de posiciones")
                        print(f" {listplayers[0]} Has perdido el turno\n")

                        break               
                                 

        player1.append(ac_d1)
        if ac_d1==positions or cont_par1==3:
                fin()         
        if ac_d1 < positions:
            key = input(".:: Presiona una tecla para continuar con el siguiente turno")
        
# JUGADOR 2
        if(found):
            if ac_d2 >= positions-6:
                dice3=0
                dice4=0
                dice3=randint(1,6)            
        
                print(f"\n.                       {listplayers[1]} - Es tu turno!                     .")
                print("\nDado uno: ",dice3)

                ac_d2=ac_d2+dice3
                if ac_d2<=positions and (dice3 != 1 or dice4 !=1):
                    print(f"\n {listplayers[1]} Has avanzado {ac_d2} posiciones de {positions}")

            if ac_d2 < positions-6:
                dice3=0
                dice4=0

                dice3=randint(1,6)
                dice4=randint(1,6)

                print("")
                print(f"\n.                       {listplayers[1]} - Es tu turno!                     .")
                print("\nDado uno: ",dice3)
                print("Dado dos: ",dice4)   

                ac_d2=ac_d2+(dice3+dice4)
                if ac_d2<=positions and (dice3 != 1 or dice4 !=1):
                    print(f"\n {listplayers[1]} Has avanzado {ac_d2} posiciones de {positions}")
                        
            if dice3==1 and dice4==1:
                ac_d2=ac_d2-(dice3+dice4)
                ac_d2=ac_d2+21
                if ac_d2<positions:
                    print(f" {listplayers[1]} Has avanzado {ac_d2} posiciones de {positions}")
                elif ac_d2 > positions:
                    ac_d2=ac_d2-21
                    ac_d2=ac_d2+(dice3+dice4)          
                    print(f"\n {listplayers[1]} Has avanzado {ac_d2} posiciones de {positions}")         

            if ac_d2 == ac_d1 and ac_d2 < positions:
                cont_ret1=cont_ret1+1
                ac_d1=ac_d1-ac_d1
                print(f"\n {listplayers[1]} chocó con  {listplayers[0]}")
                print(f" {listplayers[0]} Regresas al punto de inicio\n")  

            if len(listplayers) == 3:
                if ac_d2 == ac_d3 and ac_d2 < positions:
                    cont_ret3=cont_ret3+1
                    ac_d3=ac_d3-ac_d3
                    print(f"\n {listplayers[1]} chocó con  {listplayers[2]}")
                    print(f" {listplayers[2]} Regresas al punto de inicio\n")

            if len(listplayers) == 4:
                if ac_d2 == ac_d4 and ac_d2 < positions:
                    cont_ret4=cont_ret4+1
                    ac_d4=ac_d4-ac_d4
                    print(f"\n {listplayers[1]} chocó con  {listplayers[3]}")
                    print(f" {listplayers[3]} Regresas al punto de inicio\n")
   

            while ac_d2 > positions:  
                if True:
                    ac_d2=ac_d2-(dice3+dice4)
                    print(f"Te encuentras en la posición {ac_d2} de {positions}\n")
                    print("El resultado sobrepasa la cantidad de posiciones")
                    print(f" {listplayers[1]} Has perdido el turno\n")

                    break

            if dice3 == dice4:
                cont_par2=cont_par2+1
            else:
                cont_par2=0

            while dice3 == dice4:

                if ac_d2 >= positions-6:
                    dice3=0
                    dice4=0
                    dice3=randint(1,6)            
                    key = input(".:: Presiona una tecla para volver a tirar ::.")  

                    print(f"\n.                       {listplayers[1]} - Es tu turno!                      .")
                    print("\nDado uno: ",dice3)

                    ac_d2=ac_d2+dice3
                    if ac_d2<=positions and (dice3 != 1 or dice4 !=1):
                        print(f"\n {listplayers[1]} Has avanzado {ac_d2} posiciones de {positions}")

                if ac_d2 < positions-6:
                    dice3=0
                    dice4=0

                    dice3=randint(1,6)
                    dice4=randint(1,6)
                    key = input(".:: Presiona una tecla para volver a tirar ::.")  

                    print("")
                    print(f"\n.                       {listplayers[1]} - Es tu turno!                      .")
                    print("\nDado uno: ",dice3)
                    print("Dado dos: ",dice4)    

                    ac_d2=ac_d2+(dice3+dice4)
                    if ac_d2<=positions and (dice3 != 1 or dice4 !=1):
                        print(f"\n {listplayers[1]} Has avanzado {ac_d2} posiciones de {positions}")
                            
                if dice3 == dice4:
                    cont_par2=cont_par2+1
                else:
                    cont_par2=0

                if cont_par2==3 or ac_d2==positions:
                    fin()

                if dice3==1 and dice4==1:
                    ac_d2=ac_d2-(dice3+dice4)
                    ac_d2=ac_d2+21
                    if ac_d2<positions:
                        print(f" {listplayers[1]} Has avanzado {ac_d2} posiciones de {positions}")
                    elif ac_d2 > positions:
                        ac_d2=ac_d2-21
                        ac_d2=ac_d2+(dice3+dice4)          
                        print(f"\n {listplayers[1]} Has avanzado {ac_d2} posiciones de {positions}")          


                if ac_d2 == ac_d1 and ac_d2 < positions:
                    cont_ret1=cont_ret1+1
                    ac_d1=ac_d1-ac_d1
                    print(f"\n {listplayers[1]} chocó con  {listplayers[0]}")
                    print(f" {listplayers[0]} Regresas al punto de inicio\n")  

                if len(listplayers) == 3:
                    if ac_d2 == ac_d3 and ac_d2 < positions:
                        cont_ret3=cont_ret3+1
                        ac_d3=ac_d3-ac_d3
                        print(f"\n {listplayers[1]} chocó con  {listplayers[2]}")
                        print(f" {listplayers[2]} Regresas al punto de inicio\n")

                if len(listplayers) == 4:
                    if ac_d2 == ac_d4 and ac_d2 < positions:
                        cont_ret4=cont_ret4+1
                        ac_d2=ac_d2-ac_d2
                        print(f"\n {listplayers[1]} chocó con  {listplayers[3]}")
                        print(f" {listplayers[3]} Regresas al punto de inicio\n") 

                while ac_d2 > positions:  
                    if True:
                        ac_d2=ac_d2-(dice3+dice4)
                        print(f"Te encuentras en la posición {ac_d2} de {positions}\n")
                        print("El resultado sobrepasa la cantidad de posiciones")
                        print(f" {listplayers[1]} Has perdido el turno\n")

                        break
                                 

        player2.append(ac_d2)
        if ac_d2==positions or cont_par2==3:
                fin()         
        if ac_d2 < positions:
            key = input(".:: Presiona una tecla para continuar con el siguiente turno")

#JUGADOR 3

        if len(listplayers) == 3 or len(listplayers) == 4:
            if(found):
                if ac_d3 >= positions-6:
                    dice5=0
                    dice6=0
                    dice5=randint(1,6)            
            
                    print(f"\n.                       {listplayers[2]}  - Es tu turno!                    .")
                    print("\nDado uno: ",dice5)

                    ac_d3=ac_d3+dice5
                    if ac_d3<=positions and (dice5 != 1 or dice6 !=1):
                        print(f"\n {listplayers[2]} Has avanzado {ac_d3} posiciones de {positions}")

                if ac_d3 < positions-6:
                    dice5=0
                    dice6=0

                    dice5=randint(1,6)
                    dice6=randint(1,6)

                    print("")
                    print(f"\n.                       {listplayers[2]} - Es tu turno!                     .")
                    print("\nDado uno: ",dice5)
                    print("Dado dos: ",dice6)    

                    ac_d3=ac_d3+(dice5+dice6)
                    if ac_d3<=positions and (dice5 != 1 or dice6 !=1):
                        print(f"\n {listplayers[2]} Has avanzado {ac_d3} posiciones de {positions}")
                            
                
                if dice5==1 and dice6==1:
                    ac_d3=ac_d3-(dice5+dice6)
                    ac_d3=ac_d3+21
                    if ac_d3<positions:
                        print(f" {listplayers[2]} Has avanzado {ac_d3} posiciones de {positions}")
                    elif ac_d3 > positions:
                        ac_d3=ac_d3-21
                        ac_d3=ac_d3+(dice5+dice6)          
                        print(f"\n {listplayers[2]} Has avanzado {ac_d3} posiciones de {positions}")          

                if ac_d3 == ac_d1 and ac_d3 < positions:
                    cont_ret1=cont_ret1+1
                    ac_d1=ac_d1-ac_d1
                    print(f"\n {listplayers[2]} chocó con {listplayers[0]}")
                    print(f" {listplayers[0]} Regresas al punto de inicio\n")  

                if ac_d3 == ac_d2 and ac_d3 < positions:
                        cont_ret2=cont_ret2+1
                        ac_d2=ac_d2-ac_d2
                        print(f"\n {listplayers[2]} chocó con {listplayers[1]}")
                        print(f" {listplayers[1]} Regresas al punto de inicio\n")

                if len(listplayers) == 4:
                    if ac_d3 == ac_d4 and ac_d3 < positions:
                        cont_ret4=cont_ret4+1
                        ac_d3=ac_d3-ac_d3
                        print(f"\n {listplayers[2]} chocó con {listplayers[3]}")
                        print(f" {listplayers[3]} Regresas al punto de inicio\n")

                while ac_d3 > positions:  
                    if True:
                        ac_d3=ac_d3-(dice5+dice6)
                        print(f"Te encuentras en la posición {ac_d3} de {positions}\n")
                        print("El resultado sobrepasa la cantidad de posiciones")
                        print(f" {listplayers[2]} Has perdido el turno\n")

                        break

                if dice5== dice6:
                    cont_par3=cont_par3+1
                else:
                    cont_par3=0
                while dice5 == dice6: 

                    if ac_d3 >= positions-6:
                        dice5=0
                        dice6=0
                        dice5=randint(1,6)            
                        key = input(".:: Presiona una tecla para volver a tirar ::.")  
                        print(f"\n.                       {listplayers[2]} - Es tu turno!                     .")
                        print("\nDado uno: ",dice5)

                        ac_d3=ac_d3+dice5
                        if ac_d3<=positions and (dice5 != 1 or dice6 !=1):
                            print(f"\n {listplayers[2]} Has avanzado {ac_d3} posiciones de {positions}")

                    if ac_d3 < positions-6:
                        dice5=0
                        dice6=0

                        dice5=randint(1,6)
                        dice6=randint(1,6)
                        key = input(".:: Presiona una tecla para volver a tirar ::.")  
                        
                        print("")
                        print(f"\n.                       {listplayers[2]} - Es tu turno!                     .")
                        print("\nDado uno: ",dice5)
                        print("Dado dos: ",dice6)    

                        ac_d3=ac_d3+(dice5+dice6)
                        if ac_d3<=positions and (dice5 != 1 or dice6 !=1):
                            print(f"\n {listplayers[2]} Has avanzado {ac_d3} posiciones de {positions}")


                    if dice5 == dice6:
                        cont_par3=cont_par3+1
                    else:
                        cont_par3=0

                    if cont_par3==3 or ac_d3==positions:
                        fin()

                    if dice5==1 and dice6==1:
                        ac_d3=ac_d3-(dice5+dice6)
                        ac_d3=ac_d3+21
                        if ac_d3<positions:
                            print(f" {listplayers[2]} Has avanzado {ac_d3} posiciones de {positions}")
                        elif ac_d3 > positions:
                            ac_d3=ac_d3-21
                            ac_d3=ac_d3+(dice5+dice6)          
                            print(f"\n {listplayers[2]} Has avanzado {ac_d3} posiciones de {positions}")          

                    if ac_d3 == ac_d1 and ac_d3 < positions:
                        cont_ret1=cont_ret1+1
                        ac_d1=ac_d1-ac_d1
                        print(f"\n {listplayers[2]} chocó con {listplayers[0]}")
                        print(f" {listplayers[0]} Regresas al punto de inicio\n")  

                    if ac_d3 == ac_d2 and ac_d3 < positions:
                        cont_ret2=cont_ret2+1
                        ac_d2=ac_d2-ac_d2
                        print(f"\n {listplayers[2]} chocó con {listplayers[1]}")
                        print(f" {listplayers[1]} Regresas al punto de inicio\n")

                    if len(listplayers) == 4:
                        cont_ret4=cont_ret4+1
                        if ac_d3 == ac_d4 and ac_d3 < positions:
                            ac_d3=ac_d3-ac_d3
                            print(f"\n {listplayers[2]} chocó con  {listplayers[3]}")
                            print(f" {listplayers[3]} Regresas al punto de inicio\n") 

                    while ac_d3 > positions:  
                        if True:
                            ac_d3=ac_d3-(dice5+dice6)
                            print(f"Te encuentras en la posición {ac_d3} de {positions}\n")
                            print("El resultado sobrepasa la cantidad de posiciones")
                            print(f" {listplayers[2]} Has perdido el turno\n")

                            break
                        
                                
            player3.append(ac_d3)
            if ac_d3==positions or cont_par3==3:
                    fin()         
            if ac_d3 < positions:
                key = input(". Presiona una tecla para continuar con el siguiente turno .")

#JUGADOR 4

        if len(listplayers) == 4:
            if(found):
                if ac_d4 >= positions-6:
                    dice7=0
                    dice8=0
                    dice7=randint(1,6)            
            
                    print(f"\n.                       {listplayers[3]} - Es tu turno!                    .")
                    print("\nDado uno: ",dice7)

                    ac_d4=ac_d4+dice7
                    if ac_d4<=positions and (dice7 != 1 or dice8 !=1):
                        print(f"\n {listplayers[3]} Has avanzado {ac_d4} posiciones de {positions}")

                if ac_d4 < positions-6:
                    dice7=0
                    dice8=0

                    dice7=randint(1,6)
                    dice8=randint(1,6)

                    print("")
                    print(f"\n.                       {listplayers[3]} - Es tu turno!                      .")
                    print("\nDado uno: ",dice7)
                    print("Dado dos: ",dice8)    

                    ac_d4=ac_d4+(dice7+dice8)
                    if ac_d4<=positions and (dice7 != 1 or dice8 !=1):
                        print(f"\n {listplayers[3]} Has avanzado {ac_d4} posiciones de {positions}")
                            
                if dice7==1 and dice8==1:
                    ac_d4=ac_d4-(dice7+dice8)
                    ac_d4=ac_d4+21
                    if ac_d4<positions:
                        print(f" {listplayers[3]} Has avanzado {ac_d4} posiciones de {positions}")
                    elif ac_d4 > positions:
                            ac_d4=ac_d4-21
                            ac_d4=ac_d4+(dice7+dice8)          
                            print(f"\n {listplayers[3]} Has avanzado {ac_d4} posiciones de {positions}")          

                if ac_d4 == ac_d1 and ac_d4 < positions:
                    cont_ret1=cont_ret1+1
                    ac_d1=ac_d1-ac_d1
                    print(f"\n {listplayers[3]} chocó con {listplayers[0]}")
                    print(f" {listplayers[0]} Regresas al punto de inicio\n")  

                if ac_d4 == ac_d2 and ac_d4 < positions:
                    cont_ret2=cont_ret2+1
                    ac_d2=ac_d2-ac_d2
                    print(f"\n {listplayers[3]} chocó con {listplayers[1]}")
                    print(f" {listplayers[1]} Regresas al punto de inicio\n")

                if ac_d4 == ac_d3 and ac_d4 < positions:
                    cont_ret3=cont_ret3+1
                    ac_d3=ac_d3-ac_d3
                    print(f"\n {listplayers[3]} chocó con {listplayers[2]}")
                    print(f" {listplayers[2]} Regresas al punto de inicio\n")

                while ac_d4 > positions:  
                    if True:
                        ac_d4=ac_d4-(dice7+dice8)
                        print(f"Te encuentras en la posición {ac_d4} de {positions}\n")
                        print("Tu resultado sobrepasa la cantidad de posiciones")
                        print(f" {listplayers[3]} Has perdido el turno \n")

                        break

                if dice7 == dice8:
                    cont_par4=cont_par4+1
                else:
                    cont_par4=0
                while dice7 == dice8: 

                    if ac_d4 >= positions-6:
                        dice7=0
                        dice8=0
                        dice7=randint(1,6)            
                        key = input(". Presiona una tecla para volver a tirar .")  
                        print(f"\n.                       {listplayers[3]}                      .")
                        print("\nDado uno: ",dice7)

                        ac_d4=ac_d4+dice7
                        if ac_d4<=positions and (dice7 != 1 or dice8 !=1):
                            print(f"\n {listplayers[3]} Has avanzado {ac_d4} posiciones de {positions}")

                    if ac_d4 < positions-6:
                        dice7=0
                        dice8=0

                        dice7=randint(1,6)
                        dice8=randint(1,6)
                        key = input(".:: Presiona una tecla para volver a tirar ::.")  
                        
                        print("")
                        print(f"\n.                       {listplayers[3]}  - Es tu turno!                    .")
                        print("\nDado uno: ",dice7)
                        print("Dado dos: ",dice8)    

                        ac_d4=ac_d4+(dice7+dice8)
                        if ac_d4<=positions and (dice7 != 1 or dice8 !=1):
                            print(f"\n {listplayers[3]} Has avanzado {ac_d4} posiciones de {positions}")

                    if dice7 == dice8:
                        cont_par4=cont_par4+1
                    else:
                        cont_par4=0

                    if cont_par4==3 or ac_d4==positions:
                        fin()

                    if dice7==1 and dice8==1:
                        ac_d4=ac_d4-(dice7+dice8)
                        ac_d4=ac_d4+21
                        if ac_d4<positions:
                            print(f" {listplayers[3]} Has avanzado {ac_d4} posiciones de {positions}")
                        elif ac_d4 > positions:
                            ac_d4=ac_d4-21
                            ac_d4=ac_d4+(dice7+dice8)          
                            print(f"\n {listplayers[3]} Has avanzado {ac_d4} posiciones de {positions}")          

                    if ac_d4 == ac_d1 and ac_d4 < positions:
                        cont_ret1=cont_ret1+1
                        ac_d1=ac_d1-ac_d1
                        print(f"\n {listplayers[3]} chocó con {listplayers[0]}")
                        print(f" {listplayers[0]} Regresas al punto de inicio\n")  

                    if ac_d4 == ac_d2 and ac_d4 < positions:
                        cont_ret2=cont_ret2+1
                        ac_d2=ac_d2-ac_d2
                        print(f"\n {listplayers[3]} chocó con {listplayers[1]}")
                        print(f" {listplayers[1]} Regresas al punto de inicio\n")

                    if ac_d4 == ac_d3 and ac_d4 < positions:
                        cont_ret3=cont_ret3+1
                        ac_d3=ac_d3-ac_d3
                        print(f"\n {listplayers[3]} chocó con {listplayers[2]}")
                        print(f" {listplayers[2]} Regresas al punto de inicio\n")

                    while ac_d4 > positions:  
                        if True:
                            ac_d4=ac_d4-(dice7+dice8)
                            print(f" Te encuentras en la posición {ac_d4} de {positions}\n")
                            print(" Tu resultado sobrepasa la cantidad de posiciones")
                            print(f" {listplayers[3]} Has perdido el turno \n")

                            break                     

            player4.append(ac_d4)
            if ac_d4==positions or cont_par4==3:
                    fin()         
            if ac_d4 < positions:
                key = input(".: Presiona una tecla para continuar con el siguiente turno")
        
        
        
        
        

def fin():
    print("")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("                   EL JUEGO HA TERMINADO                      ")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("")
    estado=True
    while estado:

        if ac_d1==positions or cont_par1 == 3:
            print(f" {listplayers[0]} Has ganado!\n")

        elif ac_d2==positions or cont_par2 == 3:
            print(f" {listplayers[1]} Has ganado!\n")

        elif ac_d3==positions or cont_par3 == 3:
            print(f" {listplayers[2]} Has ganado!\n")

        elif ac_d4==positions or cont_par4 == 3:
            print(f" {listplayers[3]} Has ganado!\n")


        print("¿ Que quieres hacer ?\n")
        print("[1] Ver tabla de jugadores")
        print("[2] Jugar de nuevo ")
        print("[3] Salir ")
        op = int(input("\n Escoge una opción: "))

        if op == 1:
            table()
        elif op == 2:
            validplayers()
        elif op == 3:
            print("::: Has salido del juego :::")
            quit()

def table():
    os.system("cls")
    print("\n°°°°°               ZONA DE PUNTAJE                 °°°°°\n")
    estado=True
    while estado :
        i = 0
        found = False
        while i < len(listplayers):
            found = True
            i = i + 1
        
        if(found):
            print(f"Jugador 1: {listplayers[0]}\n")
            print(f"Posiciones recorridas: {player1[-1]}")
            if ac_d1<positions:
                print(f"Posiciones para ganar: {positions-ac_d1}\n")
            print(f"Regresos al punto de inicio: {cont_ret1}\n")

            if ac_d1==positions or cont_par1 == 3:
                print(f"{listplayers[0]} Ganó la partida!\n")
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n")

        if(found):
            print(f"Jugador 2: {listplayers[1]}\n")
            print(f"Posiciones recorridas: {player2[-1]}")
            if ac_d2<positions:
                print(f"Posiciones para ganar: {positions-ac_d2}\n")
            print(f"Regresos al punto de inicio: {cont_ret2}\n")

            if ac_d2==positions or cont_par2 == 3:
                print(f"{listplayers[1]} Ganó la partida!\n")
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n") 

        if len(listplayers) == 3 or len(listplayers) == 4:
            if(found):
                print(f"Jugador 3: {listplayers[2]}\n")
                print(f"Posiciones recorridas: {player3[-1]}")
                if ac_d3<positions:
                    print(f"Posiciones para ganar: {positions-ac_d3}\n")
                    print(f"Regresos al punto de inicio: {cont_ret3}\n")

            if ac_d3==positions or cont_par3 == 3:
                print(f"      {listplayers[2]} Ganó la partida!\n        ")
                print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n")

        if len(listplayers) == 4:
            if(found):
                print(f"Jugador 4: {listplayers[3]}\n")
                print(f"Posiciones recorridas: {player4[-1]}")
                if ac_d4<positions:
                    print(f"Posiciones para ganar: {positions-ac_d4}\n")
                    print(f"Regresos al punto de inicio: {cont_ret4}\n")

            if ac_d4==positions or cont_par4 == 3:
                print(f"     {listplayers[3]} Ganó la partida!         \n")
                print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n")

        print("¿ Que quieres hacer ?\n")
        print("[1] Jugar de nuevo ")
        print("[2] Salir ")
        op = int(input("\n Escoge una opción: "))

        if op == 1:
            validplayers()
        elif op == 2:
            print("::: Has salido del juego :::")
            quit()

def infor():
    os.system("cls")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("       DESARROLLADOR        ")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("Programa:    Carrera Númerica")
    print("Autor  :    Mario Fernando Zambrano M.")


    key = input("\n... Presiona cualquier tecla para volver al menu ")
    os.system("cls")
    menu()


validplayers()