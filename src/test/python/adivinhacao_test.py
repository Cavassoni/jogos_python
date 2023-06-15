import unittest
from forca import desenha_forca

class TestStringMethods(unittest.TestCase):
    def test_desenha_forca_vazia(self):
        desenha_forca(0)

    def test_desenha_forca_cabeca(self):
        desenha_forca(1)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
