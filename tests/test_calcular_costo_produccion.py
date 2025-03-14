import unittest
from models.producto import Producto
from models.ingredientes import Ingrediente

class TestCalcularCostoProduccion(unittest.TestCase):
    def test_costo_produccion(self):
        producto = Producto(nombre="Malteada Vainilla", precio=8300, tipo="Malteada", heladeria_id=1)
        producto.ingredientes.append(Ingrediente(nombre="Vainilla", precio=600, calorias=40, stock=10, heladeria_id=1))
        producto.ingredientes.append(Ingrediente(nombre="Leche", precio=200, calorias=20, stock=10, heladeria_id=1))

        self.assertEqual(producto.calcular_costo_produccion(), 800)

if __name__ == "__main__":
    unittest.main()
