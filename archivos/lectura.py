import io

# abrirlo
fd = open("archivos/texto.txt" ,"r",encoding="utf-8")
leer = fd.read()

fd.close()

print(leer)