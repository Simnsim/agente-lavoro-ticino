def valuta_offerta(offerta):

    testo = (
        offerta["titolo"]
        .lower()
    )

    parole_positive = [
        "econom",
        "finanz",
        "controller",
        "controlling",
        "finance",
        "buchhaltung",
        "rechnungswesen",
        "business analyst",
        "analista",
        "specialista",
        "amministr",
        "project",
        "compliance"
    ]


    parole_negative = [
        "apprend",
        "stage",
        "tirocin",
        "vendita",
        "call center"
    ]


    punteggio = 0


    for parola in parole_positive:

        if parola in testo:
            punteggio += 10


    for parola in parole_negative:

        if parola in testo:
            punteggio -= 30


    return punteggio



def filtra_offerte(lista):

    risultati = []


    for offerta in lista:

        score = valuta_offerta(offerta)

        if score >= 10:

            offerta["compatibilita"] = score

            risultati.append(offerta)


    return risultati
