import datetime
from cerca_annunci import cerca_offerte


def leggi_file(nome_file):
    with open(nome_file, "r", encoding="utf-8") as file:
        return file.read()


def analizza_profilo():

    profilo = leggi_file("profilo.txt")

    print("PROFILO CARICATO:")
    print(profilo)


def carica_fonti():

    fonti = leggi_file("fonti.txt")

    print("\nFONTI CARICATE:")
    print(fonti)




def genera_report(offerte):

    oggi = datetime.date.today()

    print("\nREPORT DEL", oggi)

    if len(offerte) == 0:
        print("nessun posto vacante")
    else:
        for offerta in offerte:
            print(offerta)



if __name__ == "__main__":

    analizza_profilo()

    carica_fonti()

    risultati = cerca_offerte()

    genera_report(risultati)
