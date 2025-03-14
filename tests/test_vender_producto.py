import unittest
from models.heladeria import Heladeria
from models.producto import Producto
from models.ingredientes import Ingrediente

class TestVenderProducto(unittest.TestCase):
    def test_vender_producto_exitoso(self):
        heladeria = Heladeria(nombre="Test Heladería", ubicacion="Centro")
        producto = Producto(nombre="Copa Fresa", precio=7500, tipo="Copa", heladeria_id=1)
        ingrediente = Ingrediente(nombre="Fresa", precio=500, calorias=30, stock=5, heladeria_id=1)

        producto.ingredientes.append(ingrediente)
        heladeria.productos.append(producto)

        resultado = heladeria.vender(producto)
        self.assertEqual(resultado, "¡Vendido!")
        self.assertEqual(ingrediente.stock, 4)

    def test_vender_producto_fallido(self):
        heladeria = Heladeria(nombre="Test Heladería", ubicacion="Centro")
        producto = Producto(nombre="Copa Fresa", precio=7500, tipo="Copa", heladeria_id=1)
        ingrediente = Ingrediente(nombre="Fresa", precio=500, calorias=30, stock=0, heladeria_id=1)

        producto.ingredientes.append(ingrediente)
        heladeria.productos.append(producto)

        with self.assertRaises(ValueError) as context:
            heladeria.vender(producto)

        self.assertEqual(str(context.exception), "Fresa")

if __name__ == "__main__":
    unittest.main()
