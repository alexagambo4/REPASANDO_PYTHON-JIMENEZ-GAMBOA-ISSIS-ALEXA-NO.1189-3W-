#imprime los datos de la autora 
print("Jimenez Gamboa Issis Alexa ")
print("no.1189")
print("3W")
#imprime linea en banco para qu se vea mas limpio
print("")
#imprime el titulo del prgrama 
print("Ejercicio no.2")
#imprime las instrucciones
print("Dada una nota almacenada en una variable, imprime su equivalente:")
print("• Mayor o igual a 0, pero menor que 5, SUSPENSO.")
print("• Mayor o igual a 5, pero menor que 6, SUFICIENTE.")
print("• Mayor o igual a 6, pero menor que 7, BIEN.")
print("• Mayor o igual a 7, pero menor que 9, NOTABLE.")
print("• Mayor o igual a 9, pero menor o igual a 10, SOBRESALIENTE.")
print("En cualquier otro caso, imprimir el texto: NOTA NO VÁLIDA.")
#imprime una linea en blanco 
print("")

nota = 8  # Puedes cambiar este valor para probar

if 0 <= nota < 5:
    print("SUSPENSO")
elif 5 <= nota < 6:
    print("SUFICIENTE")
elif 6 <= nota < 7:
    print("BIEN")
elif 7 <= nota < 9:
    print("NOTABLE")
elif 9 <= nota <= 10:
    print("SOBRESALIENTE")
else:
    print("NOTA NO VÁLIDA")
