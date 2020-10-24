# by Joshua
import time, os, random

def printTitle():
    print("+========================================================+")
    print("+                                           __________   +")
    print("+    _______ ____  _____________________    ___(_)_  /   +")
    print("+    __  __ `/  / / /  _ \_  ___/_  ___/    __  /_  __/  +")
    print("+    _  /_/ // /_/ //  __/(__  )_(__  )     _  / / /_    +")
    print("+    _\__, / \__,_/ \___//____/ /____/      /_/  \__/    +")
    print("+    /____/                                              +")
    print("+====================Joshua Ayala========================+")
    print("")

def facil():
    i=0
    intentos = 3
    os.system('cls')
    numeroCorrecto = random.randrange(20)
    numeroCercaMenosCorrecto = numeroCorrecto - 3
    numeroCercaMasCorrecto = numeroCorrecto + 3
    printTitle()
    print("Adivina el numero del 0 al 20.")
    while(i<intentos):
        i+=1
        numeroIntento = int(input("Intento: "))
        if(numeroIntento == numeroCorrecto):
            print("+============================================================+")
            print("+  ____________________   ________________________________   +")
            print("+  __  ____/__    |__  | / /__    |_  ___/__  __/__  ____/   +")
            print("+  _  / __ __  /| |_   |/ /__  /| |____ \__  /  __  __/      +")
            print("+  / /_/ / _  ___ |  /|  / _  ___ |___/ /_  /   _  /___      +")
            print("+  \____/  /_/  |_/_/ |_/  /_/  |_/____/ /_/    /_____/      +")
            print("+============================================================+")
            print("")
            volver = int(input("¿Quieres volver al inicio?\n[1] Sí.\n[2] No.: "))
            if(volver==1):
                main()
            elif(volver==2):
                os.system('exit')
            break
        elif(numeroIntento>20):
            print("El número que introduciste es mayor que el límite.")
        elif(numeroIntento>=numeroCercaMenosCorrecto and numeroIntento<=numeroCercaMasCorrecto):
            print("Cerca...")
            if(i==intentos):
                print("Mmm...")
                time.sleep(2)
                print("Perdiste.")
                break;
        elif(i==intentos):
            print("Mmm...")
            time.sleep(2)
            print("Perdiste.")
            volver = int(input("¿Quieres volver al inicio?\n[1] Sí.\n[2] No.\n>: "))
            if(volver==1):
                main()
            elif(volver==2):
                os.system('exit')

            break;
            
def medio():
    i=0
    intentos = 3
    os.system('cls')
    numeroCorrecto = random.randrange(100)
    numeroCercaMenosCorrecto = numeroCorrecto - 10
    numeroCercaMasCorrecto = numeroCorrecto + 10
    printTitle()
    print("Adivina el numero del 0 al 100.")
    while(i<intentos):
        i+=1
        numeroIntento = int(input("Intento: "))
        if(numeroIntento == numeroCorrecto):
            print("+============================================================+")
            print("+  ____________________   ________________________________   +")
            print("+  __  ____/__    |__  | / /__    |_  ___/__  __/__  ____/   +")
            print("+  _  / __ __  /| |_   |/ /__  /| |____ \__  /  __  __/      +")
            print("+  / /_/ / _  ___ |  /|  / _  ___ |___/ /_  /   _  /___      +")
            print("+  \____/  /_/  |_/_/ |_/  /_/  |_/____/ /_/    /_____/      +")
            print("+============================================================+")
            print("")
            volver = int(input("¿Quieres volver al inicio?\n[1] Sí.\n[2] No.: "))
            if(volver==1):
                main()
            elif(volver==2):
                os.system('exit')
            break
        elif(numeroIntento>100):
            print("El número que introduciste es mayor que el límite.")
        elif(numeroIntento>=numeroCercaMenosCorrecto and numeroIntento<=numeroCercaMasCorrecto):
            print("Cerca...")
            if(i==intentos):
                print("Mmm...")
                time.sleep(2)
                print("Perdiste.")
                break;
        elif(i==intentos):
            print("Mmm...")
            time.sleep(2)
            print("Perdiste.")
            volver = int(input("¿Quieres volver al inicio?\n[1] Sí.\n[2] No.\n>: "))
            if(volver==1):
                main()
            elif(volver==2):
                os.system('exit')

            break;

def dificil():
    i=0
    intentos = 3
    os.system('cls')
    numeroCorrecto = random.randrange(500)
    numeroCercaMenosCorrecto = numeroCorrecto - 30
    numeroCercaMasCorrecto = numeroCorrecto + 30
    printTitle()
    print("Adivina el numero del 0 al 500.")
    while(i<intentos):
        i+=1
        numeroIntento = int(input("Intento: "))
        if(numeroIntento == numeroCorrecto):
            print("+============================================================+")
            print("+  ____________________   ________________________________   +")
            print("+  __  ____/__    |__  | / /__    |_  ___/__  __/__  ____/   +")
            print("+  _  / __ __  /| |_   |/ /__  /| |____ \__  /  __  __/      +")
            print("+  / /_/ / _  ___ |  /|  / _  ___ |___/ /_  /   _  /___      +")
            print("+  \____/  /_/  |_/_/ |_/  /_/  |_/____/ /_/    /_____/      +")
            print("+============================================================+")
            print("")
            volver = int(input("¿Quieres volver al inicio?\n[1] Sí.\n[2] No.: "))
            if(volver==1):
                main()
            elif(volver==2):
                os.system('exit')
            break
        elif(numeroIntento>500):
            print("El número que introduciste es mayor que el límite.")
        elif(numeroIntento>=numeroCercaMenosCorrecto and numeroIntento<=numeroCercaMasCorrecto):
            print("Cerca...")
            if(i==intentos):
                print("Mmm...")
                time.sleep(2)
                print("Perdiste.")
                break;
        elif(i==intentos):
            print("Mmm...")
            time.sleep(2)
            print("Perdiste.")
            volver = int(input("¿Quieres volver al inicio?\n[1] Sí.\n[2] No.\n>: "))
            if(volver==1):
                main()
            elif(volver==2):
                os.system('exit')

            break;

def ifs():
    elección=0
    elección = int(input(">: "))
    if(elección==1):
        facil()
    elif(elección==2):
        medio()
    elif(elección==3):
        dificil()
    elif(elección==0):
        print("Hasta luego :)")
        os.system('exit')
    else:
        print("Error.")

def main():
    os.system('cls')
    printTitle()
    print("Elige una opcion:\n [1] Fácil.\n [2] Medio.\n [3] Difícil.\n\n [0] Salir.\n")
    ifs()

os.system('cls')
printTitle()
print("Elige una opcion:\n [1] Fácil.\n [2] Medio.\n [3] Difícil.\n\n [0] Salir.\n")
ifs()