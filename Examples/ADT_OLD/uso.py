import fechaNumero
import fechaString


fecha = fechaNumero.nuevaFecha(2022, 1, 1)
print(fechaNumero.darYear(fecha))


fecha2 = fechaString.nuevaFecha(2022, 1, 1)
print(fechaString.darYear(fecha2))

# Un TAD fecha define los metodos:
#    nuevaFecha()
#    darYear()
#    #etc.
#
# fechaNumero y fechaString ambos implmentan esos metodos
# 
# fechaNumero es una implmentacion del TAD fecha
# fechaString es una implmentacion del TAD fecha
