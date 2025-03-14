import unittest
from models.ingredientes import Ingrediente

class TestAbastecerIngrediente(unittest.TestCase):
    def test_abastecer(self):
        ingrediente = Ingrediente(nombre="Vainilla", precio=600, calorias=40, stock=5, heladeria_id=1)
        ingrediente.abastecer(10)
        self.assertEqual(ingrediente.stock, 15)

if __name__ == "__main__":
    unittest.main()
