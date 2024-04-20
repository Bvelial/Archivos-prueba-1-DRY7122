firstName = input("¿Cuál es tu primer nombre? ")
lastName = input("¿Cuales son tus apellidos? ")
seccion = input("¿Cuál es tu Sección? ")
sede = input("¿Cuál es tu Sede? ")

if seccion.upper() == "DRY7122-003V":
    print ("\nDatos ingresados:", 
            '\n' + firstName + 
            '\n' + lastName + 
            '\n' + seccion + 
            '\n' + sede + 
            '\n', '\n',
        
        "Hola " + firstName +" perteneces a la sección: " + seccion.upper() + ". Debes entrar a clases")
else:
    print ("\nDatos ingresados:", 
            '\n' + firstName + 
            '\n' + lastName + 
            '\n' + seccion + 
            '\n' + sede + 
            '\n', '\n',

        "Hola " + firstName +" tu no perteneces a la sección DRY7122-003V, tu sección es: " + seccion.upper() + ". Por favor vete")
