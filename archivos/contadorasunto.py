# ejercicio 3 busacar todo los from
import io
fd = open("archivos/contarlineas.txt","r",encoding="utf-8")
cont = 0
for linea in fd:
    if linea.count("subject"):
        cont +=1

fd.close()
print("lineas que ingrese con subject:", cont)
# wc -l comando para lineas
