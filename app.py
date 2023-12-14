import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from dotenv import load_dotenv

load_dotenv()

def getLLMStory(navn, beskrivelse, morsom):
    llm = OpenAI(
        model_name="text-davinci-003", 
        temperature=0.9
    )
    examples = [
        {
            "question":"",
            "answer":""
        },
    ]

    examples_template = """
    question:{question}
    answer:{answer}
    """

    examples_prompt = PromptTemplate(
        input_variables=["question", "answer"],
        template=examples_template
    )

    # prefix = """
    # Du skal skrive hvordan min ai vertøy som lager markedsføring innlegg vil hjelpe bedriften.

    # """

    # suffix = """
    # Samlet informasjon om bedriften her: {template_navn} {template_beskrivelse} {template_morsom}.

    # Skriv i perspektivet jeg, og start med som bedrift kan min ai hjelpe med med...
     
    # jeg ønsker du bruker teksten under for å forme teksten som passer med bedriften og kunden deres.
    # Jeg ønsker å markedsføre min spesifikke tjeneste. Hva er det? Jeg deler disse detaljene med mitt eget Ai-verktøy, og det lager fengslende innlegg for å promotere min spesifikke tjeneste. Jeg kopierer og limer inn for å dele den der kunden min er.

    # mitt ai-verktøy er opplært av markedsfører, som fant fengslende innlegg som brukeren min liker, tok forretningstjenestene og lagde eksempler på hva ai-verktøyet vil skape, og sørger for at innleggene stemmer overens med kundenes motivasjoner og praksisens verdier.

    # vi har forstått hvordan vi kan gi verdi på riktig måte, og oppnå det mest kritiske med mine forretningsmål.

    # som forretningseier av kunden min vil se et innlegg som taler direkte til deres behov, noe som gjør din praksis til det beste valget.
    # """

    # ...

    # prefix = """
    # Dette er hvordan min AI-verktøy for markedsføring, som jeg har utviklet, vil hjelpe bedriften din:

    # AI-verktøyet er en avansert digital assistent som benytter seg av maskinlæring og naturlig språkforståelse for å skape engasjerende og målrettede markedsføringsinnlegg. Den analyserer din bedrifts unike behov og mål, og tilpasser innholdet deretter.

    # Forståelse: Det første trinnet er at AI-verktøyet forstår hva din tjeneste handler om. Ved å analysere din bedrifts beskrivelse og mål, lager det relevant og tilpasset innhold.

    # Tro: AI-verktøyet er designet og opplært av erfarne markedsførere. Dette sikrer at hvert innlegg det produserer, resonnerer med målgruppen og bygger tillit.

    # Ønske: Med dette verktøyet kan du skape innhold som vekker interesse og ønske hos dine potensielle kunder. Det sikrer at markedsføringsbudskapet ditt er både overbevisende og relevant.

    # Valg: Til slutt, gjennom engasjerende og målrettet innhold, hjelper AI-verktøyet deg å overbevise potensielle kunder om at din tjeneste er det beste valget, noe som vil bidra til økt synlighet og kundetilstrømning for din bedrift.
    # """

    prefix = """
    svar bare basert på forretningstype og hva de selger og deretter være i stand til å lage Ai-forslag som ligner på produksjonen under; 
    1. **Eget ai robot lager innlegg**:
    - **Se for deg dette**: Du ønsker å markedsføre en bestemt tjeneste. Hva er det? Del disse detaljene med vår AI.
    - **AIs magi**: Den lager et fengslende innlegg, og sikrer at det stemmer perfekt med kundens motivasjoner og praksisens verdier.
    - **Gjennom Jennys øyne**: Hun ser et innlegg som taler direkte til hennes behov, noe som gjør treningen din til det beste valget.
    """
    suffix = """
        Samlet informasjon om bedriften her: {template_navn} {template_beskrivelse} {template_morsom}.

        Basert på disse detaljene, vil mitt AI-verktøy lage skreddersydd markedsføringsinnhold som resonnerer med dine kunder og forsterker din merkevareidentitet. La oss se hvordan det kan transformere din markedsføringsstrategi.
        """

    # ...



    example_selector = LengthBasedExampleSelector(
        examples=examples,
        example_prompt=examples_prompt,
        max_length=200
    )

    new_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=examples_prompt,
        prefix=prefix,
        suffix=suffix,
        input_variables=["template_navn","template_beskrivelse","template_morsom"],
        example_separator="\n"
    )

    print(new_prompt.format(template_navn=navn,template_beskrivelse=beskrivelse,template_morsom=morsom))

    response=llm(new_prompt.format(template_navn=navn,template_beskrivelse=beskrivelse,template_morsom=morsom))

    print(response)

    return response



st.subheader('Forbedre din bedrift med din egen AI løsning. Fortell oss litt om din bedrift')

# En morsom detalj eller karakteristikk ved dyret 
navn = st.text_input('Hva slags bedrift er du?')
beskrivelse = st.text_input('hva slags ønsker du å selge?')
morsom = st.text_area('Hvor ønsker du å nå til kunden?', height=40)

st.subheader('Forhåndsvisning av tekst under:')

if st.button('Lag innlegg'):
    # Her kan du legge til funksjonalitet for å publisere innlegget.
    st.write(getLLMStory(navn, beskrivelse, morsom))

# st.markdown("<div style='padding: 200px;'></div>", unsafe_allow_html=True)
