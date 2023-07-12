import io
fd = open("archivos/contarlineas.txt","r",encoding="utf-8")
cont = 0
for linea in fd:
    if linea.startswith("From"):
        cont +=1

fd.close()
print("cantidad de lineas que empiezan con from:",cont)
# wc -l comando para lineas

# ejercicio 3 busacar todo los from
import io
fd = open("archivos/contarlineas.txt","r",encoding="utf-8")
cont = 0
for linea in fd:
    if linea.lower().find("From")>-1:
        cont +=1

fd.close()
print("cantidad de lineas que empiezan con from:",cont)
# wc -l comando para lineas

# 3 contar lineas de archovo con @uct.ac.za
import io
fd = open("archivos/contarlineas.txt","r",encoding="utf-8")
cont = 0
for linea in fd:
    if not "@uct.ac.za" in linea:
        continue

fd.close()
print("cantidad de lineas que empiezan con from:",cont)