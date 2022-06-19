import datetime

dateWithTime = datetime.datetime.strptime('2021/03/01', '%Y/%m/%d') #De string a datetime
date = datetime.datetime.strptime('2021/03/01', '%Y/%m/%d').date()  #De string a date
now = datetime.datetime.now()                                       #datetime que representa este momento

d = datetime.datetime(date.year, date.month, date.day)              #datetime creada con año, mes dia

stringDateTime = dateWithTime.strftime("%d/%m/%y")    #De datetime a String
stringDate = date.strftime("%d/%m/%y")                #De date a String

print("Comparaciones")
print(dateWithTime < now)
print(dateWithTime <= now)

print()
print("Tiempo transcurrido")
diff = now - dateWithTime
print(diff)
print(diff.total_seconds())


# Para usos avanzados mirar:
# https://docs.python.org/3/library/datetime.html
# Revisar Format Codes, tabla para fomatos

#=============================
# Extra
#=============================
import sys
print()
print("datetime es mas grande que date")
print(sys.getsizeof(dateWithTime) > sys.getsizeof(date))

