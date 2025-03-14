import unittest
from models.heladeria import Heladeria
from models.producto import Producto

class TestProductoMasRentable(unittest.TestCase):
    def test_producto_mas_rentable(self):
        heladeria = Heladeria(nombre="Heladería Test", ubicacion="Centro")
        producto1 = Producto(nombre="Copa Fresa", precio=7500, tipo="Copa", heladeria_id=1)
        producto2 = Producto(nombre="Malteada Choco", precio=8500, tipo="Malteada", heladeria_id=1)

        heladeria.productos.extend([producto1, producto2])

        self.assertEqual(heladeria.encontrar_producto_mas_rentable(), producto2)

if __name__ == "__main__":
    unittest.main()
