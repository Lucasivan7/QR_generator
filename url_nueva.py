
# Importamos las librerias necesarias para trabajar con fechas.

from datetime import date, datetime
from datetime import timedelta

primer_dia = "2022-11-20"
primer_dia = datetime.strptime(primer_dia, "%Y-%m-%d")
hoy = datetime.now()
dia_de_bootcamp = hoy - primer_dia

def actu_url(url_base, dia_bootcamp): 
    url_nueva = url_base + str(dia_bootcamp)
    return url_nueva



url = actu_url("check-in/", str(dia_de_bootcamp.days))
print(url)
