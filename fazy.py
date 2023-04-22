from ephem import *

dzis = now()

def pelnia():
    return next_full_moon(dzis)

def zeszla_pelnia():
    return previous_full_moon(dzis)

def przyszly_now():  # nów księżyca
    return next_new_moon(dzis)

def zeszly_now():
    return previous_new_moon(dzis)

def pierwsza_kwadra():
    return next_first_quarter_moon(dzis)

def zeszla_pierwsza_kwadra():
    return previous_first_quarter_moon(dzis)

def ostatnia_kwadra():
    return next_last_quarter_moon(dzis)

def zeszla_ostatnia_kwadra():
    return previous_last_quarter_moon(dzis)