import unittest
from models.heladeria import Heladeria
from models.ingredientes import Ingrediente

class TestRenovarInventario(unittest.TestCase):
    def test_renovar_inventario(self):
        heladeria = Heladeria(nombre="Test Heladería", ubicacion="Centro")
        ingrediente = Ingrediente(nombre="Leche", precio=200, calorias=20, stock=0, heladeria_id=1)
        heladeria.ingredientes.append(ingrediente)

        heladeria.renovar_inventario("Leche", 10)
        self.assertEqual(ingrediente.stock, 10)

if __name__ == "__main__":
    unittest.main()
