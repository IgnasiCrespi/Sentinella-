import csv
from datetime import datetime
import pandas as pd


def crear():
    file = 'register.csv'
    f = open(file, "a")
    print("Arxiu creat: /" + file)

    val = 'Si'
    return val

def checkFile():
    
    try:
        with open("register.csv", 'r') as f:
            val = 1
    except FileNotFoundError:
        print("Arxiu no trobat:", FileNotFoundError)
        val = 0
    except OSError:
        print("Error de sistema:", OSError)
        val = 0
    except IOError:
        print("Error de sistema:", IOError)
        val = 0 
    return val  

def read():
    f = pd.read_csv("register.csv")
    print(f)
    
def register():
    val = checkFile()
    if (val == 0):
        crear()
        val = 1

    dicc = dict()
    dicc['curs'] = input("Introdueix el curs: ")
    dicc['aula'] = input("Introdueix el número de l'aula: ")
    dicc['num_alumnes'] = int(input("Introdueix el número d'alumnes: "))
    dicc['num_professors'] = int(input("Introdueix el número de professors: "))
    dicc['dia'] = input("Introdueix la data: ")


    print("Indica a quina hora es la classe:")
    print("1.-8:00-9:00")
    print("2.-9:00-10:00")
    print("3.-10:00-11:00")
    print("4.-11:30-12:30")
    print("5.-12:30-13:30")
    print("6.-13:30-14:30")
    print("7.-17:30-18:30")
    print("8.-18:30-19:30")
    print("9.-19:30-20:30")

    num = int(input("Introdueix l'opció: "))
    while (num < 1 or num > 9):
        num = int(input("ERROR! Introdueix una opció vàlida: "))
    if num == 1:
        aux = '8:00-9:00'
    elif num == 2:
        aux = '9:00-10:00'
    elif num == 3:
        aux = '10:00-11:00'
    elif num == 4:
        aux = '11:30-12:30'
    elif num == 5:
        aux = '12:30-13:30'
    elif num == 6:
        aux = '13:30-14:30'
    elif num == 7:
        aux = '17:30-18:30'
    elif num == 8:
        aux = '18:30-19:30'
    elif num == 9:
        aux = '19:30-20:30'


    dicc['hora_classe'] = aux
    dicc['nom_profe'] = input("Introdueix el nom del professor/a: ")
    dicc['assignatura'] = input("Introdueix el nom de la assignatura: ")
    dicc['t_porta_p_oberta'] = int(input("Introdueix en minuts quant de temps ha estat la porta principal oberta: "))
    
    print("La classe disposa d una porta secundaria: ")
    print("1.-Si.")
    print("2.-No.")
    num = int(input("Introdueix l'opció: "))
    while (num < 1 or num > 2):
        num = int(input("ERROR! Introdueix una opció vàlida: "))
    if num == 1:
        segona = 'Si'
        time = int(input('Introdueix en minuts quant de temps ha estat la porta secundaria oberta: '))
    elif num == 2:
        segona = 'No'
        time = 'NULL'

    dicc['porta_secundaria'] = segona
    dicc['temps_porta_sec'] = time

    print("Indica el tipus de finestres que tens al aula: ")
    print("1.-Finestres externes")
    print("2.-Finestres internes")
    num = int(input("Introdueix l'opció: "))
    while (num < 1 or num > 2):
        num = int(input("ERROR! Introdueix una opció vàlida: "))
    if num == 1:
        aux = 'Externes'
    if num == 2:
        aux = 'Internes'
    dicc['finestres'] = aux

    print("Hi ha hagut ventilació creuada: ")
    print("1.-Si")
    print("2.-No")
    num = int(input("Introdueix l'opció: "))
    while (num < 1 or num > 2):
        num = int(input("ERROR! Introdueix una opció vàlida: "))
    if num == 1:
        creu = 'Si'
    elif num == 2:
        creu = 'No'
    dicc['v_creuada'] = creu

    with open('register.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['curs', 'aula', 'num_alumnes', 'num_professors', 'dia', 'hora_classe', 'nom_profe', 'assignatura', 't_porta_p_oberta', 'porta_secundaria', 'temps_porta_sec', 'finestres', 'v_creuada']
        writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if val == 1:
            writeCSV.writeheader()  # Se encarrega que de escriure la capçalera del CSV.
        try:
            writeCSV.writerow(dicc)
        except:
            print("No s'ha inserit el registre.")
        else:
            print("El registre s'ha inserit correctament.")
    

def menu():


    print("Què vols fer:")
    print("1.-Registrar")
    print("2.-Mostrar")
    print("3.-Sortir")
    
    num = int(input("Introdueix una opció: "))
    
    while(num<1 or num>4):
        num = int(input("ERROR! Introdueix una opció correctament: "))
    if num == 1:
        register()
    elif num == 2:
        read()
    elif num == 3:
        print("Sortint del programa")
        return 0

