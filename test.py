from cerca_annunci import cerca_offerte


risultati = cerca_offerte()


print("\n====================")
print("RISULTATI TROVATI")
print("====================")


if len(risultati) == 0:
    print("nessun posto vacante")

else:
    for posto in risultati:
        print("\nENTE:")
        print(posto["ente"])

        print("\nLINK:")
        print(posto["link"])

        print("\nTESTO:")
        print(posto["testo"][:500])
