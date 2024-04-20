alumnos=[]
file=open ("alumnosDRY7122_003V.txt", "r")
for item in file:
    item=item.strip ()
    alumnos.append (item)
file.close()
print(alumnos)
