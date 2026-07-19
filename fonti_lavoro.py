import requests
from bs4 import BeautifulSoup


def scarica_pagina(url):

    try:

        risposta = requests.get(
            url,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        risposta.raise_for_status()

        return BeautifulSoup(
            risposta.text,
            "html.parser"
        )


    except Exception as errore:

        print("Errore:", url, errore)

        return None



def cerca_eoc():

    risultati = []

    url = "https://www.eoc.ch/lavora-con-noi.html"

    pagina = scarica_pagina(url)

    if pagina:

        risultati.append({

            "ente": "EOC",

            "titolo": "Offerte lavoro EOC",

            "link": url

        })

    return risultati



def cerca_ffs():

    risultati = []

    url = "https://company.sbb.ch/it/carriera.html"


    pagina = scarica_pagina(url)


    if pagina:

        risultati.append({

            "ente": "FFS",

            "titolo": "Offerte lavoro FFS",

            "link": url

        })


    return risultati



def cerca_aet():

    risultati = []

    url = "https://www.aet.ch/"

    pagina = scarica_pagina(url)


    if pagina:

        risultati.append({

            "ente": "AET",

            "titolo": "Offerte lavoro AET",

            "link": url

        })


    return risultati



def cerca_tutte_fonti():

    offerte = []

    offerte.extend(cerca_eoc())

    offerte.extend(cerca_ffs())

    offerte.extend(cerca_aet())


    return offerte
