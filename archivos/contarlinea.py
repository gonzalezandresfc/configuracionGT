import io
fd = open("archivos/contarlineas.txt","r",encoding="utf-8")
cont = 0
for linea in fd:
    cont +=1

fd.close()
print("cantidad de lineas:",cont)
# wc -l comando para lineas