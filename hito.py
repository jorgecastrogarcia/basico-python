acceso=input('que deseas hacer:login o registrarse ')

if acceso=='login' or acceso=='registrarse':
    input('usuario ')
    input('contraseña ')
    
    camisetas=25
    peluches=15
    pantalones=30
    zapatillas=45
    pantallas=125
    pc=1200
    
    
    listado=[camisetas,peluches,pantalones,zapatillas,pantallas,pc]
    productos=['camisetas,peluches,pantalones,zapatillas,pantallas,pc']
    print(productos)
    pedido=input('por favor introduzca los articulos que deseas de esta lista ')
    
    
    if pedido!=listado:
        print('elija algo de la lista')
    else:
        respuesta=input('¿desea comprar algo mas?')
        if respuesta=='no':
            print(f'el pedido es de {respuesta+pedido}')
        else:
            respuesta=input('introduzca los productos deseados')
            
        
else:
    print('opcion no valida,rellene los campos de forma adecuada')
    
    
    
print(f'su ticket tiene un total de {respuesta+pedido}')
print('la factura ha sido enviada a su correo electronico en formato pdf ')
print ('tambien se le ha enviado un sms con el codigo de seguimiento de su pedido a su telefono')
