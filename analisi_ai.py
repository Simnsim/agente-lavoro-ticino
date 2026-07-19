import os
import google.generativeai as genai


genai.configure(
    api_key=os.environ["GEMINI_API_KEY"]
)


model = genai.GenerativeModel(
    "gemini-1.5-flash"
)



def valuta_offerta(offerta, profilo):


    prompt = f"""

Sei un selezionatore del personale.

Valuta questa offerta rispetto al candidato.

PROFILO:
{profilo}


OFFERTA:
{offerta}


Rispondi SOLO con questo formato:

Compatibilita: XX%

Motivo:
- punto 1
- punto 2

Decisione:
INTERESSANTE oppure SCARTARE

"""


    risposta = model.generate_content(
        prompt
    )


    return risposta.text
