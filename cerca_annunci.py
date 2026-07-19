import requests
from bs4 import BeautifulSoup


def cerca_canton_ticino():

    url = "https://www.concorsi.ti.ch/"

    offerte = []

    try:

        pagina = requests.get(
            url,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        pagina.raise_for_status()


        soup = BeautifulSoup(
            pagina.text,
            "html.parser"
        )


        link_trovati = soup.find_all("a")


        for link in link_trovati:

            titolo = link.get_text(
                strip=True
            )

            indirizzo = link.get("href")


            if titolo and indirizzo:

                parole = [
                    "econom",
                    "finanz",
                    "controller",
                    "controlling",
                    "amministr",
                    "specialista",
                    "responsabile",
                    "analista",
                    "project",
                    "management"
                ]


                testo = titolo.lower()


                if any(
                    parola in testo
                    for parola in parole
                ):

                    if indirizzo.startswith("/"):

                        indirizzo = (
                            "https://www.concorsi.ti.ch"
                            + indirizzo
                        )


                    offerte.append({

                        "ente": "Cantone Ticino",

                        "titolo": titolo,

                        "link": indirizzo

                    })


    except Exception as errore:

        print(
            "Errore Canton Ticino:",
            errore
        )


    return offerte



def cerca_offerte():

    risultati = []

    risultati.extend(
        cerca_canton_ticino()
    )

    return risultati
