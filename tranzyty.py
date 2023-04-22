from ephem import *

krakow = Observer()
krakow.lat = '50:05:21'
krakow.lon = '19:56:21'
mars = Mars()
wenus = Venus()


def najblizszy_tranzyt_Wenus():
    krakow.date = now()
    return krakow.next_transit(wenus)

def najblizszy_tranzyt_Marsa():
    krakow.date = now()
    return krakow.next_transit(mars)

def zeszly_tranzyt_Wenus():
    krakow.date = now()
    return krakow.previous_transit(wenus)

def zeszly_tranzyt_Marsa():
    krakow.date = now()
    return krakow.previous_transit(mars)
