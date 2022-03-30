#De pesos a dólares
def conversor(tipo_pesos , valor_dolar):  
    pesos =  input('¿Cuántos pesos ' + tipo_pesos + ' tienes?:')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

#De dólares a pesos
def consersor2(tipo_peso2, valor_peso):
    dolares2 = input("¿Cuántos dólares tienes?:")
    dolares2 = float(dolares2)
    pesos2 = dolares2 * valor_peso
    pesos2 = int(pesos2)
    pesos2 = str(pesos2)
    print("Tienes " + pesos2 + tipo_peso2)

menu = """
Bienvenido al conversor de monedas 😊

¿Quiere pasar de? 

1 - Pesos a dólares.
2 - Dólares a pesos.
"""
opcion = int(input(menu))

if opcion == 1:
    menu1 = """
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicamos

Elige una opción: """

    opcion1 = int(input(menu1))
 
    if opcion1 == 1:
        conversor('colombianos', 3807)
    elif opcion1 == 2:
        conversor('argentinos', 97.71)
    elif opcion1 == 3:
        conversor('mexicanos', 20.12 )
    else:
        print('Por favor,ingresa una opción correcta.')

elif opcion == 2:
    menu2="""
    1 - A pesos colombianos
    2 - A pesos argentinos
    3 - A pesos mexicanos

Elige una opción: """
    
    opcion2 = int(input(menu2))

    if opcion2 == 1:
        conversor('colombianos', 3807)
    elif opcion2 ==2:
        conversor('argentinos', 97.71)
    elif opcion2 ==3:
        conversor('mexicanos', 20.12)
    else: 
        print('Por favor,ingresa una opción correcta.')
else:
    print('Elige una opción 😁')