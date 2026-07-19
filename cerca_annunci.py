import requests
from bs4 import BeautifulSoup


def cerca_canton_ticino():

    url = "https://www4.ti.ch/dfe/de/concorsi"

    offerte = []

    try:

        pagina = requests.get(
            url,
            timeout=20
        )

        pagina.raise_for_status()


        soup = BeautifulSoup(
            pagina.text,
            "html.parser"
        )


        testi = soup.get_text(
            separator=" ",
            strip=True
        )


        offerte.append({
            "ente": "Cantone Ticino",
            "testo": testi[:1000],
            "link": url
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
