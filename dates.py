import pytz
import calendar
from datetime import date, timedelta, datetime
# ADDING UTC TIME ZONE TO NAIVE DATETIME (RETURNS LIKE AWARE BUT +00)  >> DATETIME.astimezone(pytz.timezone(TIME_ZONE))
deadline = DATETIME.astimezone(pytz.timezone(TIME_ZONE))


# Localtime to UTC Time
from django.utils import timezone
import pytz

timezone.now() # equivale a un objeto datetime en UTC

my_time = datetime.now() # Crea un datetime limpio, sin utc
time_zone = pytz.timezone(TIME_ZONE) # jala timezone desde donde se recibe my_time
localized = time_zone.localize(my_time) # localiza my_time, ahora es un objecto consciente de su UTC
my_time_utc = localized.astimezone(pytz.utc) # se convierte en UTC, my_time_utc == timezone.now(), listo para ser guardado

##############
# COMPRIMIDO #
##############
my_time = datetime.now() 
my_time_utc = pytz.timezone(TIME_ZONE).localize(my_time).astimezone(pytz.utc)


# UTC to Localtime
local_time = my_time_utc.astimezone(pytz.timezone(TIME_ZONE))
