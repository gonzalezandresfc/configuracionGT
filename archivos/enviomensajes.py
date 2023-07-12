import io
fd = open("archivos/contarlineas.txt","r",encoding="utf-8")
correo = set()
for linea in fd:
    if linea.startswith("from"):
        linea=linea[6:]
        correo.add(linea)
enviar = list(correo)
for i in range(len(enviar)-1,0,1:):
    correo = enviar[i]
    print("enviado ok/t",correo.rstrip())
    fd.close()
