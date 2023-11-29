import pickle

def nuskaityti():
    try:
        with open("zurnalas.pkl", 'rb') as file:
            zurnalas = pickle.load(file)
    except:
        zurnalas = []
    return zurnalas

zurnalas = nuskaityti()

def irasyti():
    with open("zurnalas.pkl", 'wb') as file:
        pickle.dump(zurnalas, file)

while True:
    veiksmas = int(input("1 - įvesti\n2 - ataskaita\n3 - balansas\n4 - išeiti\n"))
    match veiksmas:
        case 1:
            suma = float(input("Suma: "))
            zurnalas.append(suma)
            irasyti()
        case 2:
            for irasas in zurnalas:
                print(irasas)
        case 3:
            print(sum(zurnalas))
        case 4:
            print("Viso gero")
            break
        case _:
            print("Neteisingai pasirinktas veiksmas")