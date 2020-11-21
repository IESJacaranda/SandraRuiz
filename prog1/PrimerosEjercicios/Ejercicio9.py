"""
Ejercicio 9
En un establecimiento en rebajas, hay 3 tipos de productos (A, B y C). El porcentaje de rebaja que se aplicará sobre el 
precio original del producto se calcula de la siguiente forma:
  - Si el producto es de tipo A, independientemente de su precio se aplica un 7% de descuento.
  - Si el producto es de tipo C o bien el precio es inferior a 500€ se aplicará un porcentaje del 12% de descuento.
  - En el resto de casos se aplica un 9% de descuento.
Realizar un programa que solicite los datos necesarios (tipo de producto y precio original) y calcule el precio rebajado. 
Debe comprobarse que los datos de entrada son correctos, y si no lo son mostrar un mensaje de error.

"""

producttype = input("Ingresa el tipo de producto:")
productprice = int(input("¿Qué precio tiene el producto?:"))
if producttype in {"A", "B", "C", "a", "b", "c"}:
    if productprice > 0:
        if producttype in {"A", "a"}:
            finalprice = float(int(productprice)) * 0.93
            print("El precio final del producto es",finalprice)
        elif producttype in {"C", "c"} or productprice < 500:
            finalprice = float(int(productprice)) * 0.88
            print("El precio final del producto es",finalprice)
        elif producttype in {"B", "b"}:
            finalprice = float(int(productprice)) * 0.91
            print("El precio final del producto es",finalprice)
    else:
        print("El precio es incorrecto")
else:
    print("No existe dicho producto en el establecimiento")