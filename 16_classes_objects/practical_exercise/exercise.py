# TODO 1: crea una clase Product.
# Debe tener un metodo __init__ que reciba name, price y stock.
# Dentro de __init__, guarda esos valores en self.name, self.price y self.stock.
# Luego usa la clase en el siguiente TODO.
class Product:
    pass


# TODO 2: crea un objeto product_a de la clase Product con "lapiz", 2.5 y 30.
# Luego revisa el valor de product_a para ver el objeto creado.
product_a =

# TODO 3: obtiene el nombre, precio y stock de product_a.
# Luego revisa el valor de product_name, product_price y product_stock.
product_name =
product_price =
product_stock =

# TODO 4: cambia el stock de product_a a 25.
# Luego revisa el valor de product_a.stock para ver el atributo modificado.


# TODO 5: agrega a Product un metodo instance llamado subtotal.
# El metodo debe recibir quantity y retornar self.price * quantity.
# Luego llama product_a.subtotal(4) y guarda el resultado en subtotal_value.
# Luego revisa el valor de subtotal_value.
subtotal_value =

# TODO 6: agrega a Product un metodo instance llamado is_available.
# El metodo debe retornar True si self.stock es mayor que 0, o False si no.
# Luego llama product_a.is_available() y guarda el resultado en available.
# Luego revisa el valor de available.
available =

# TODO 7: agrega a Product un metodo de clase llamado from_tuple.
# Debe recibir product_data y retornar cls(product_data[0], product_data[1], product_data[2]).
# Luego crea product_b usando Product.from_tuple(("cuaderno", 8.0, 12)).
# Luego revisa el valor de product_b.name, product_b.price y product_b.stock.
product_b =

# TODO 8: agrega a Product un metodo estatico llamado apply_discount.
# Debe recibir price y discount, y retornar price * (1 - discount).
# Luego llama Product.apply_discount(100, 0.1) y guarda el resultado en discounted_price.
# Luego revisa el valor de discounted_price.
discounted_price =

# TODO 9: agrega a Product un metodo __eq__.
# Debe retornar True si other tambien es Product y tiene el mismo name.
# Luego crea product_c con "lapiz", 3.0 y 10.
# Luego compara product_a == product_c y guarda el resultado en same_product.
# Luego revisa el valor de same_product.
product_c =
same_product =

# TODO 10: crea una lista products con product_a, product_b y product_c.
# Luego revisa el valor de products para ver la lista de objetos.
products =

# TODO 11: crea una lista vacia product_summaries.
# Luego revisa el valor de product_summaries para ver que empieza vacia.
product_summaries =

# TODO 12: recorre products.
# Dentro del for, crea product_summary con el formato "lapiz: 2.5 (25)".
# Agrega product_summary a product_summaries.
# Luego revisa el valor de product_summary en cada vuelta y product_summaries al final.
