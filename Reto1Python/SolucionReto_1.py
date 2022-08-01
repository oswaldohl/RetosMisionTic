#reto_1

faltanProductos = 'S'
lista=[]
while faltanProductos == 'S':
    
    producto=int(input('ingrese el valor unitario:' ))
    iva=input('¿El producto cuenta con IVA? S/N:')
    cantidadProducto= int(input('ingrese la cantidad que lleva el cliente del producto a resgistrar: '))
    if iva == 'S':
        print('IVA incluido')
        valor = (producto + (producto * 0.19)) * cantidadProducto
        lista.append(valor)
        print('SUBTOTAL:' + str(sum(lista)))
        
    else:
        print('PRODUCTO SIN IVA')
        valorsinIVA = producto * cantidadProducto
        lista.append(valorsinIVA)
        print('SUBTOTAL:' + str(sum(lista)))
        
    faltanProductos=input('¿faltan productos por cobrar? S/N:')
else:
    totalCobrar= sum(lista)
    print('TOTAL A COBRAR:' + str(totalCobrar))