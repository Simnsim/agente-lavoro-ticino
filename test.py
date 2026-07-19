from cerca_annunci import cerca_offerte


risultati = cerca_offerte()


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
