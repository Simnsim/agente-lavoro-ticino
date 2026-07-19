from cerca_annunci import cerca_offerte
from fonti_lavoro import cerca_tutte_fonti


risultati = []


# Cerca Cantone Ticino
risultati.extend(
    cerca_offerte()
)


# Cerca altre fonti
risultati.extend(
    cerca_tutte_fonti()
)



print("====================")
print("RISULTATI TROVATI")
print("====================")



if len(risultati) == 0:

    print("nessun posto vacante")


else:

    for posto in risultati:

        print("\nENTE:")
        print(posto["ente"])

        print("\nPOSIZIONE:")
        print(posto["titolo"])

        print("\nLINK CANDIDATURA:")
        print(posto["link"])

        print("--------------------")
