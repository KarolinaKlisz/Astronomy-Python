from ephem import *
from planety import *
def zmiana(gwiazdozbior):
    if gwiazdozbior == 'Taurus':
        nazwa = 'Byk'
        return nazwa
    elif gwiazdozbior == 'Aquarius':
        nazwa = 'Wodnik'
        return nazwa
    elif gwiazdozbior == 'Pisces':
        nazwa = 'Ryby'
        return nazwa
    elif gwiazdozbior == 'Aries':
        nazwa = 'Baran'
        return nazwa
    elif gwiazdozbior == 'Gemini':
        nazwa = 'Bliźnięta'
        return nazwa
    elif gwiazdozbior == 'Cancer':
        nazwa = 'Rak'
        return nazwa
    elif gwiazdozbior == 'Leo':
        nazwa = 'Lew'
        return nazwa
    elif gwiazdozbior == 'Virgo':
        nazwa = 'Panna'
        return nazwa
    elif gwiazdozbior == 'Libra':
        nazwa = 'Waga'
        return nazwa
    elif gwiazdozbior == 'Scorpio':
        nazwa = 'Skorpion'
        return nazwa
    elif gwiazdozbior == 'Sagittarius':
        nazwa = 'Strzelec'
        return nazwa
    elif gwiazdozbior == 'Capricornus':
        nazwa = 'Koziorożec'
        return nazwa
    else:
        return gwiazdozbior



def konstelacje(text):

    if text == 'konstelacja saturna' or text == 'konstelacja Saturna' or text == 'instalacje Saturna' or text == 'pięć':  # bardzo czesto wylapuje instalacje zamiast konstelacje
        odpowiedz = zmiana(constellation(saturn)[1])
        return odpowiedz
    if text == 'konstelacja marsa' or text == 'konstelacja Marsa' or text == 'instalacje Marsa' or text == 'trzy':
        odpowiedz = zmiana(constellation(mars)[1])
        print(odpowiedz)
        return odpowiedz
    if text == 'konstelacja Wenus' or text == 'konstelacja Venus' or text == 'instalacje Venus' or text == 'instalacje Wenus' or text == 'dwa':
        odpowiedz = zmiana(constellation(wenus)[1])
        return odpowiedz
    if text == 'konstelacja Merkurego' or text == 'konstelacja merkurego' or text == 'instalacje Merkurego' or text == 'jeden':
        odpowiedz = zmiana(constellation(merkury)[1])
        return odpowiedz
    if text == 'konstelacja Jowisza' or text == 'konstelacja jowisza' or text == 'instalacje Jowisza' or text == 'cztery':
        odpowiedz = zmiana(constellation(jowisz)[1])
        return odpowiedz
    if text == 'konstelacja Urana' or text == 'konstelacja urana' or text == 'instalacje Urana' or text == 'sześć':
        odpowiedz = zmiana(constellation(uran)[1])
        return odpowiedz
    if text == 'konstelacja Neptuna' or text == 'konstelacja neptuna' or text == 'instalacje Neptuna' or text == 'siedem':
        odpowiedz = zmiana(constellation(neptun)[1])
        return odpowiedz

