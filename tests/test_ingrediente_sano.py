import unittest
from models.ingredientes import Ingrediente

class TestIngredienteSano(unittest.TestCase):
    def test_ingrediente_sano(self):
        ingrediente = Ingrediente(nombre="Fresa", precio=500, calorias=30, stock=10, heladeria_id=1)
        self.assertTrue(ingrediente.es_sano())

    def test_ingrediente_no_sano(self):
        ingrediente = Ingrediente(nombre="Chocolate", precio=700, calorias=80, stock=10, heladeria_id=1)
        self.assertFalse(ingrediente.es_sano())

if __name__ == "__main__":
    unittest.main()
