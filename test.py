from cerca_annunci import cerca_offerte
from fonti_lavoro import cerca_tutte_fonti
from analisi_ai import valuta_offerta


def leggi_profilo():

    with open(
        "profilo.txt",
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()



profilo = leggi_profilo()


risultati = []


# Ricerca Cantone Ticino

risultati.extend(
    cerca_offerte()
)


# Ricerca altre fonti

risultati.extend(
    cerca_tutte_fonti()
)



print("====================")
print("ANALISI AI IN CORSO")
print("====================")



if len(risultati) == 0:

    print("nessun posto vacante")


else:

    for posto in risultati:


        analisi = valuta_offerta(
            posto,
            profilo
        )


        print("\n====================")

        print(
            posto["ente"]
        )


        print(
            posto["titolo"]
        )


        print(
            posto["link"]
        )


        print("\nVALUTAZIONE AI:")

        print(
            analisi
        )
