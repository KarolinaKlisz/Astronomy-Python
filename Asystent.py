import speech_recognition as sr
import pyttsx3
from konstelacje import *
from wschodyZachody import *
from tranzyty import *
from fazy import *
from pozycje import *

engine = pyttsx3.init()
r = sr.Recognizer()

while True:

    print("Aby zacząć wciśnij enter")
    engine.say("Aby zacząć wciśnij enter")
    engine.runAndWait()
    wyzwalacz = input(" ")

    if wyzwalacz == '':
        print("-----Kategorie-----")
        print("[1] Konstelacje")
        print("[2] Wschody Słońca ")  # niezbyt wykrywa wszystkie słowa dlatego można uruchomić za pomocą cyfr
        print("[3] Zachody Słońca ")
        print("[4] Fazy Księżyca")
        print("[5] Tranzyty planet")
        print("[6] Pozycje planet dzisiaj")
        engine.say("Podaj kategorie z której chcesz zadać pytanie")
        engine.runAndWait()
        with sr.Microphone() as source:
            try:
                audio = r.listen(source)
                text = r.recognize_google(audio, language="pl-PL")

                if text == 'Konstelacje' or text == 'konstelacje' or text == 'Konstelacja' or text == 'konstelacja' or text == '1' or text =='jeden' or text == 'pierwsza':
                    engine.say("Wybrałeś konstelacje, oto możliwe pytania")
                    engine.runAndWait()
                    print("[1] Konstelacja Merkurego")
                    print("[2] Konstelacja Wenus")
                    print("[3] Konstelacja Marsa")
                    print("[4] Konstelacja Jowisza")
                    print("[5] Konstelacja Saturna")
                    print("[6] Konstelacja Urana")
                    print("[7] Konstelacja Neptuna")
                    engine.say("Poproszę o pytanie")
                    engine.runAndWait()
                    try:
                        audio = r.listen(source)
                        pytanie = r.recognize_google(audio, language="pl-PL")
                        engine.say(f'konstelacja tej planety to {konstelacje(pytanie)}')
                        engine.runAndWait()
                    except sr.UnknownValueError:
                        print('nie usłyszałem')
                    except sr.RequestError as e:
                        print('error:', e)
                if text == 'wschody słońca' or text == 'Wschody Słońca' or text == 'dwa' or text == '2' or text == 'druga':
                    engine.say("Wybrałeś kategorię Wschody Słońca, oto możliwe pytania")
                    engine.runAndWait()
                    print("[1] Najbliższy wschód Słońca")
                    print("[2] Wczorajszy wschód Słońca")
                    print("[3] Przeszłe wschody Słońca")
                    print("[4] Przyszłe wschody Słońca")
                    engine.say("Poproszę o pytanie")
                    engine.runAndWait()
                    try:
                        audio = r.listen(source)
                        pytanie = r.recognize_google(audio, language="pl-PL")
                        if pytanie == 'Najbliższy wschód słońca' or pytanie == 'Najbliższy wschód słońca' or pytanie == '1' or pytanie == 'jeden' or pytanie == 'pierwsze':
                            engine.say(f'Najbliższy wschód słońca będzie {wschod()}')
                            engine.runAndWait()
                        if pytanie == 'Wczorajszy wschód słońca' or pytanie == '2' or pytanie == 'dwa' or pytanie == 'drugie':
                            engine.say(f'Wczorajszy wschód słońca był {wschod_wczorajszy()}')
                            engine.runAndWait()
                        if pytanie == 'Przeszłe wschody słońca' or pytanie == '3' or pytanie == 'trzy' or pytanie == 'trzecie':
                            engine.say('Podaj z ilu dni wstecz chcesz otrzymać informację o wschodzie słońca, maksymalna liczba dni to dziesięć')
                            engine.runAndWait()
                            try:
                                audio = r.listen(source)
                                pytanie1 = r.recognize_google(audio, language="pl-PL")
                                engine.say(f' {pytanie1} dni temu wschód słońca był {przeszle_wschody(str_na_int(pytanie1))}')
                                engine.runAndWait()
                            except sr.UnknownValueError:
                                print('nie usłyszałem')
                            except sr.RequestError as e:
                                print('error:', e)
                        if pytanie == 'Przyszłe wschody słońca' or pytanie == '4' or pytanie == 'cztery' or pytanie == 'czwarte':
                            engine.say('Podaj na który dzień do przodu chcesz otrzymać informację o wschodzie słońca, maksymalna liczba dni to dziesieć')
                            engine.runAndWait()
                            try:
                                audio = r.listen(source)
                                pytanie1 = r.recognize_google(audio, language="pl-PL")
                                engine.say(f'za {pytanie1} dni wschód słońca będzie {przyszle_wschody(str_na_int(pytanie1))}')
                                engine.runAndWait()
                            except sr.UnknownValueError:
                                print('nie usłyszałem')
                            except sr.RequestError as e:
                                print('error:', e)
                    except sr.UnknownValueError:
                        print('nie usłyszałem')
                    except sr.RequestError as e:
                        print('error:', e)
                if text == 'Zachody słońca' or text == '3' or text == 'trzy' or text == 'trzecia' or text == 'zachody słońca' or text == 'zachody Słońca':
                    engine.say("Wybrałeś kategorię Zachody Słońca, oto możliwe pytania")
                    engine.runAndWait()
                    print("[1] Najbliższy zachód Słońca")
                    print("[2] Wczorajszy zachód Słońca")
                    print("[3] Przeszłe zachody Słońca")
                    print("[4] Przyszłe zachody Słońca")
                    engine.say("Poproszę o pytanie")
                    engine.runAndWait()
                    try:
                        audio = r.listen(source)
                        pytanie = r.recognize_google(audio, language="pl-PL")
                        print("Text: ", text)
                        if pytanie == 'Najbliższy zachód słońca' or pytanie == 'Najbliższy zachód słońca' or pytanie == '1' or pytanie == 'jeden' or pytanie == 'pierwsze':
                            engine.say(f'Najbliższy zachód słońca będzie {zachod()}')
                            engine.runAndWait()
                        if pytanie == 'Wczorajszy zachód słońca' or pytanie == '2' or pytanie == 'dwa' or pytanie == 'drugie':
                            engine.say(f'Wczorajszy zachód słońca był {zachod_wczorajszy()}')
                            engine.runAndWait()
                        if pytanie == 'Przeszłe wschody słońca' or pytanie == '3' or pytanie == 'trzy' or pytanie == 'trzecie':
                            engine.say('Podaj z ilu dni wstecz chcesz otrzymać informację o zachodzie słońca, maksymalna liczba dni to dziesięć')
                            engine.runAndWait()
                            try:
                                audio = r.listen(source)
                                dni = r.recognize_google(audio, language="pl-PL")
                                engine.say(f' {dni} dni temu zachód słońca był {przeszle_zachody(str_na_int(dni))}')
                                engine.runAndWait()
                            except sr.UnknownValueError:
                                print('nie usłyszałem')
                            except sr.RequestError as e:
                                print('error:', e)
                        if pytanie == 'Przyszłe wschody słońca' or pytanie == '4' or pytanie == 'cztery' or pytanie == 'czwarte':
                            engine.say('Podaj na który dzień do przodu chcesz otrzymać informację o zachodzie słońca, maksymalna liczba dni to dziesieć')
                            engine.runAndWait()
                            try:
                                audio = r.listen(source)
                                dni = r.recognize_google(audio, language="pl-PL")
                                engine.say(f'za {dni} dni zachód słońca będzie {przyszle_zachody(str_na_int(dni))}')
                                engine.runAndWait()
                            except sr.UnknownValueError:
                                print('nie usłyszałem')
                            except sr.RequestError as e:
                                print('error:', e)
                    except sr.UnknownValueError:
                        print('nie usłyszałem')
                    except sr.RequestError as e:
                        print('error:', e)
                if text == 'Fazy Księżyca' or text == 'fazy księżyca' or text == '4' or text == 'cztery' or text == 'czwarta':
                    engine.say('Wybrałeś kategorię fazy księżyca. Oto możliwe pytania')
                    engine.runAndWait()
                    print("[1] Następna pełnia Księżyca")
                    print("[2] Zeszła pełnia Księżyca")
                    print("[3] Następny nów Księżyca")
                    print("[4] Zeszły nów Księżyca")
                    print("[5] Następna pierwsza kwadra Księżyca")
                    print("[6] Zeszła pierwsza kwadra Księżyca")
                    print("[7] Następna ostatnia kwadra Księżyca")
                    print("[8] Zeszła ostatnia kwadra Księżyca")
                    engine.say('Poproszę o pytanie')
                    engine.runAndWait()
                    try:
                        audio = r.listen(source)
                        faza = r.recognize_google(audio, language="pl-PL")
                        if faza == 'następna pełnia księżyca' or faza == 'następna pełnia Księżyca' or faza == '1' or faza == 'jeden' or faza == 'pierwsze':
                            engine.say(f'Następna pełnia księżyca będzie {pelnia()}')
                            engine.runAndWait()
                        if faza == 'zeszła pełnia księżyca' or faza == 'zeszła pełnia Księżyca' or faza == '2' or faza == 'dwa' or faza == 'drugie':
                            engine.say(f'Zeszła pełnia księżyca była {zeszla_pelnia()}')
                            engine.runAndWait()
                        if faza == 'następny nów księżyca' or faza == 'następny nów Księżyca' or faza == '3' or faza == 'trzy' or faza == 'trzecie':
                            engine.say(f'Następny nów księżyca będzie {przyszly_now()}')
                            engine.runAndWait()
                        if faza == 'zeszły nów księżyca' or faza == 'zeszły nów Księżyca' or faza == '4' or faza == 'cztery' or faza == 'czwarte':
                            engine.say(f'Zeszły nów księżyca był {zeszly_now()}')
                            engine.runAndWait()
                        if faza == 'następna pierwsza kwadra księżyca' or faza == 'następna pierwsza kwadra Księżyca' or faza == '5' or faza == 'pięć' or faza == 'piąte':
                            engine.say(f'Następna pierwsza kwadra Księżyca będzie {pierwsza_kwadra()}')
                            engine.runAndWait()
                        if faza == 'zeszła pierwsza kwadra księżyca' or faza == 'zeszła pierwsza kwadra Księżyca' or faza == '6' or faza == 'sześć' or faza == 'szóste':
                            engine.say(f'Zeszła pierwsza kwadra Księżyca była {zeszla_pierwsza_kwadra()}')
                            engine.runAndWait()
                        if faza == 'następna ostatnia kwadra księżyca' or faza == 'następna ostatnia kwadra Księżyca' or faza == '7' or faza == 'siedem' or faza == 'siódme':
                            engine.say(f'następna ostatnia kwadra Księżyca była {ostatnia_kwadra()}')
                            engine.runAndWait()
                        if faza == 'zeszła ostatnia kwadra księżyca' or faza == 'zeszła ostatnia kwadra Księżyca' or faza == '8' or faza == 'osiem' or faza == 'ósme':
                            engine.say(f'zeszła ostatnia kwadra Księżyca była {zeszla_ostatnia_kwadra()}')
                            engine.runAndWait()
                    except sr.UnknownValueError:
                        print('nie usłyszałem')
                    except sr.RequestError as e:
                        print('error:', e)
                if text == 'Tranzyty planet' or text == 'tranzyty planet' or text == 'tranzyty Planet' or text == '5' or text == 'pięć' or text == 'piąta':
                    engine.say("Wybrałeś kategorię tranzyty planet, oto możliwe pytania")
                    engine.runAndWait()
                    print("[1] Najbliższy tranzyt Wenus")
                    print("[2] Najbliższy tranzyt Marsa")
                    print("[3] Zeszły tranzyt Wenus")
                    print("[4] Zeszły tranzyt Marsa")
                    engine.say("Poproszę o pytanie")
                    engine.runAndWait()
                    try:
                        audio = r.listen(source)
                        pytanie = r.recognize_google(audio, language="pl-PL")
                        if pytanie == 'Najbliższy tranzyt Wenus' or pytanie == 'Najbliższy tranzyt wenus' or pytanie == '1' or pytanie == 'jeden' or pytanie == 'pierwsze':
                            engine.say(f'Najbliższy tranzyt Wenus będzie {najblizszy_tranzyt_Wenus()}')
                            engine.runAndWait()
                        if pytanie == 'najbliższy tranzyt Marsa' or pytanie == 'najbliższy tranzyt marsa' or pytanie == '2' or pytanie == 'dwa' or pytanie == 'drugie':
                            engine.say(f'Najbliższy tranzyt Marsa będzie {najblizszy_tranzyt_Marsa()}')
                            engine.runAndWait()
                        if pytanie == 'zeszły tranzyt Wenus' or pytanie == 'zeszły tranzyt wenus' or pytanie == '3' or pytanie == 'trzy' or pytanie == 'trzecie':
                            engine.say(f'Zeszły tranzyt Wenus był {zeszly_tranzyt_Wenus()}')
                            engine.runAndWait()
                        if pytanie == 'zeszły tranzyt Marsa' or pytanie == 'zeszły tranzyt marsa' or pytanie == '4' or pytanie == 'cztery' or pytanie == 'czwarte':
                            engine.say(f'Zeszły tranzyt Marsa był {zeszly_tranzyt_Marsa()}')
                            engine.runAndWait()
                    except sr.UnknownValueError:
                        print('nie usłyszałem')
                    except sr.RequestError as e:
                        print('error:', e)
                if text == 'Pozycje planet dzisiaj' or text == 'pozycje planet dzisiaj' or text == '6' or text == 'sześć' or text == 'szósta':
                    engine.say("Wybrałeś kategorię pozycje planet dzisiaj, oto możliwe pytania")
                    engine.runAndWait()
                    print("[1] Pozycja Merkurego")
                    print("[2] Pozycja Wenus")
                    print("[3] Pozycja Ziemi")
                    print("[4] Pozycja Marsa")
                    print("[5] Pozycja Jowisza")
                    print("[6] Pozycja Saturna")
                    print("[7] Pozycja Urana")
                    print("[8] Pozycja Neptuna")
                    engine.say("Poproszę o pytanie")
                    engine.runAndWait()
                    try:
                        audio = r.listen(source)
                        pozycja = r.recognize_google(audio, language="pl-PL")
                        if pozycja == 'pozycja Merkurego' or pozycja == 'pozycja merkurego' or pozycja == '1' or pozycja == 'jeden' or pozycja == 'pierwsze':
                            engine.say(f'Pozycja Merkurego to {poz_merkury()}')
                            engine.runAndWait()
                        if pozycja == 'pozycja Wenus' or pozycja == 'pozycja wenus' or pozycja == '2' or pozycja == 'dwa' or pozycja == 'drugie':
                            engine.say(f'Pozycja Wenus to {poz_wenus()}')
                            engine.runAndWait()
                        if pozycja == 'pozycja Ziemi' or pozycja == 'pozycja ziemi' or pozycja == '3' or pozycja == 'trzy' or pozycja == 'trzecie':
                            engine.say(f'Pozycja Ziemi to {poz_ziemia()}')
                            engine.runAndWait()
                        if pozycja == 'pozycja Marsa' or pozycja == 'pozycja marsa' or pozycja == '4' or pozycja == 'cztery' or pozycja == 'czwarte':
                            engine.say(f'Pozycja Marsa to {poz_mars()}')
                            engine.runAndWait()
                        if pozycja == 'pozycja Jowisza' or pozycja == 'pozycja jowisza' or pozycja == '5' or pozycja == 'pięć' or pozycja == 'piąte':
                            engine.say(f'Pozycja Jowisza to {poz_jowisz()}')
                            engine.runAndWait()
                        if pozycja == 'pozycja Saturna' or pozycja == 'pozycja saturna' or pozycja == '6' or pozycja == 'sześć' or pozycja == 'szóste':
                            engine.say(f'Pozycja Saturna to {poz_saturn()}')
                            engine.runAndWait()
                        if pozycja == 'pozycja Urana' or pozycja == 'pozycja urana' or pozycja == '7' or pozycja == 'siedem' or pozycja == 'siódme':
                            engine.say(f'Pozycja Urana to {poz_uran()}')
                            engine.runAndWait()
                        if pozycja == 'pozycja Neptuna' or pozycja == 'pozycja Neptuna' or pozycja == '8' or pozycja == 'osiem' or pozycja == 'ósme':
                            engine.say(f'Pozycja Neptuna to {poz_neptun()}')
                            engine.runAndWait()
                    except sr.UnknownValueError:
                        print('nie usłyszałem')
                    except sr.RequestError as e:
                        print('error:', e)
            except sr.UnknownValueError:
                print('nie usłyszałem')
            except sr.RequestError as e:
                print('error:', e)



