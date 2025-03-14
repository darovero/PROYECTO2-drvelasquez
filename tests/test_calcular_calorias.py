import unittest
from models.producto import Producto
from models.ingredientes import Ingrediente

class TestCalcularCalorias(unittest.TestCase):
    def test_calcular_calorias(self):
        producto = Producto(nombre="Copa Fresa", precio=7500, tipo="Copa", heladeria_id=1)
        producto.ingredientes.append(Ingrediente(nombre="Fresa", precio=500, calorias=30, stock=10, heladeria_id=1))
        producto.ingredientes.append(Ingrediente(nombre="Leche", precio=200, calorias=20, stock=10, heladeria_id=1))

        self.assertEqual(producto.calcular_calorias(), 50)

if __name__ == "__main__":
    unittest.main()
