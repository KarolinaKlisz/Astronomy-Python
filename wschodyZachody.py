from datetime import datetime, timedelta

from ephem import *
# Tworzenie obiektu Słońca
sun = Sun()
krakow = Observer()
krakow.lat = '50:05:21'
krakow.lon = '19:56:21'



def wschod():
    krakow.date = now()
    wschod = krakow.next_rising(sun)
    # Wydruk wschodu Słońca
    return wschod

def wschod_wczorajszy():
    krakow.date = datetime.now() - timedelta(days=1)
    wschod = krakow.next_rising(sun)
    return wschod

def przeszle_wschody(dni):
    krakow.date = datetime.now() - timedelta(days=dni)
    wschod = krakow.next_rising(sun)
    return wschod

def przyszle_wschody(dni):
    krakow.date = datetime.now() + timedelta(days=dni)
    wschod = krakow.next_rising(sun)
    return wschod

def zachod():
    krakow.date = now()
    zachod = krakow.next_setting(sun)
    # Wydruk wschodu Słońca
    return zachod

def zachod_wczorajszy():
    krakow.date = datetime.now() - timedelta(days=1)
    zachod = krakow.next_setting(sun)
    return zachod

def przeszle_zachody(dni):
    krakow.date = datetime.now() - timedelta(days=dni)
    zachod = krakow.next_setting(sun)
    return zachod

def przyszle_zachody(dni):
    krakow.date = datetime.now() + timedelta(days=dni)
    zachod = krakow.next_setting(sun)
    return zachod



def str_na_int(slowo):
    if slowo == 'jeden':
        return 1
    elif slowo == 'dwa':
        return 2
    elif slowo == 'trzy':
        return 3
    elif slowo == 'cztery':
        return 4
    elif slowo == 'pięć':
        return 5
    elif slowo == 'sześć':
        return 6
    elif slowo == 'siedem':
        return 7
    elif slowo == 'osiem':
        return 8
    elif slowo == 'dziewięć':
        return 9
    elif slowo == 'dziesięć':
        return 10
    else:
        return slowo

