
from ephem import *

# tworzymy obiekty

today = now()  # pobieramy aktualną datę i godzinę

moon = Moon()
mars = Mars(today)
wenus = Venus(today)
merkury = Mercury(today)
jowisz = Jupiter(today)
saturn = Saturn(today)
uran = Uranus(today)
neptun = Neptune(today)
slonce = Sun()
