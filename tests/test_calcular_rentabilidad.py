import unittest
from models.producto import Producto
from models.ingredientes import Ingrediente

class TestCalcularRentabilidad(unittest.TestCase):
    def test_calcular_rentabilidad(self):
        producto = Producto(nombre="Copa Vainilla", precio=7200, tipo="Copa", heladeria_id=1)
        producto.ingredientes.append(Ingrediente(nombre="Vainilla", precio=600, calorias=40, stock=10, heladeria_id=1))
        producto.ingredientes.append(Ingrediente(nombre="Leche", precio=200, calorias=20, stock=10, heladeria_id=1))

        self.assertEqual(producto.calcular_rentabilidad(), 6400)

if __name__ == "__main__":
    unittest.main()
