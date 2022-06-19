# fechaNumero es una implmentacion del TAD fecha

def nuevaFecha(year, month, day):
  return year*10000 + month*100 + day

def darYear(fecha):
  return round(fecha/10000)
