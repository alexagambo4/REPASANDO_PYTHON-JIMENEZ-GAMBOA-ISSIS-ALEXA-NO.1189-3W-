#imprime los datos de la autora 
print("Jimenez Gamboa Issis Alexa ")
print("no.1189")
print("3W")
#imprime linea en banco para qu se vea mas limpio
print("")
#imprime el titulo del prgrama 
print("Ejercicio no.3 ")
#imprime las instrucciones
print("Existen dos variables, una con un nombre y otra con un apellido. Primero se ha de comprobar el")
print("nombre, si es igual a Daniel, se comprueba el apellido, si es igual a Ramos, se imprime por pantalla el texto Nombre y apellido correctos. En caso de que el nombre sea Daniel,")
print("pero el apellido no sea Ramos, se imprime por pantalla el texto Apellido incorrecto. En caso que el nombre no sea Daniel, se imprime por pantalla el texto Usuario desconocido.")
#imprime una linea en blanco 
print("")

nombre = "Alexa"  
apellido = "Gamboa" 

if nombre == "Alexa ":
    if apellido == "Gamboa":
        print("Nombre y apellido correctos")
    else:
        print("Apellido incorrecto")
else:
    print("Usuario desconocido")
