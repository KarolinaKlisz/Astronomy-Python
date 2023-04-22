from ephem import *
from planety import *
dzis = now()

def poz_jowisz():
    jowisz.compute(dzis)
    pozycja = '%s %s' % (jowisz.ra, jowisz.dec)
    return pozycja

def poz_merkury():
    merkury.compute(dzis)
    pozycja = '%s %s' % (merkury.ra, merkury.dec)
    return pozycja

def poz_wenus():
    wenus.compute(dzis)
    pozycja = '%s %s' % (wenus.ra, wenus.dec)
    return pozycja

def poz_ziemia():
    krakow = Observer()
    krakow.lat = '50:05:21'
    krakow.lon = '19:56:21'
    krakow.date = now()
    slonce.compute(krakow)
    pozycja = '%s %s' % (slonce.ra, slonce.dec)
    return pozycja

def poz_mars():
    mars.compute(dzis)
    pozycja = '%s %s' % (mars.ra, mars.dec)
    return pozycja

def poz_saturn():
    saturn.compute(dzis)
    pozycja = '%s %s' % (saturn.ra, saturn.dec)
    return pozycja

def poz_uran():
    uran.compute(dzis)
    pozycja = '%s %s' % (uran.ra, uran.dec)
    return pozycja

def poz_neptun():
    neptun.compute(dzis)
    pozycja = '%s %s' % (neptun.ra, neptun.dec)
    return pozycja

