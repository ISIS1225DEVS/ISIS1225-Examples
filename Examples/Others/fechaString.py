# fechaString es una implmentacion del TAD fecha

def nuevaFecha(year, month, day):
  return str(year) + "-" + str(month) + "-" + str(day)

def darYear(fecha):
  return int(fecha[0:4])
