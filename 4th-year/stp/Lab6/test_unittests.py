import unittest
from tcomplex import TComplex


class UnitTests(unittest.TestCase):
    def test_create_tcomplex_one(self):
        tcomplex = TComplex(1)

        expected = (1, 0)
        actual = (tcomplex.a, tcomplex.b)

        self.assertEqual(expected, actual)
        self.assertIsInstance(tcomplex.a, float)
        self.assertIsInstance(tcomplex.b, float)


    def test_create_tcomplex_two(self):
        tcomplex = TComplex(2, 3)

        expected = (2, 3)
        actual = (tcomplex.a, tcomplex.b)

        self.assertEqual(expected, actual)
        self.assertIsInstance(tcomplex.a, float)
        self.assertIsInstance(tcomplex.b, float)


    def test_create_tcomplex_str(self):
        tcomplex = TComplex("6+i*3")

        expected = (6, 3)
        actual = (tcomplex.a, tcomplex.b)

        self.assertEqual(expected, actual)
        self.assertIsInstance(tcomplex.a, float)
        self.assertIsInstance(tcomplex.b, float)


    def test_create_tcomplex_str_num(self):
        self.assertRaises(ValueError, TComplex, "0+i*3", 6)


    def test_copy(self):
        tcomplex = TComplex(2, 3)
        tcomplex_copy = tcomplex.copy()

        expected = (2, 3)
        actual = (tcomplex.a, tcomplex.b)

        self.assertEqual(expected, actual)
        self.assertIsNot(tcomplex, tcomplex_copy)


    def test_add_function(self):
        tcomplex_1 = TComplex(2, 1)
        tcomplex_2 = TComplex(3, 4)
        tcomplex_add = tcomplex_1.add(tcomplex_2)

        expected = (5, 5)
        actual = (tcomplex_add.a, tcomplex_add.b)

        self.assertEqual(expected, actual)


    def test_multiply(self):
        tcomplex_1 = TComplex(1, 2)
        tcomplex_2 = TComplex(4, 3)
        tcomplex_mul = tcomplex_1 * tcomplex_2

        expected = (-2, 11)
        actual = (tcomplex_mul.a, tcomplex_mul.b)

        self.assertEqual(expected, actual)


    def test_squaring(self):
        tcomplex_1 = TComplex(2, 4)
        tcomplex_sq = tcomplex_1.sq()

        expected = (-12, 16)
        actual = (tcomplex_sq.a, tcomplex_sq.b)

        self.assertEqual(expected, actual)


    def test_inverse(self):
        tcomplex_1 = TComplex(4, 1)
        tcomplex_inv = tcomplex_1.inverse()

        expected = (0.235294117647, -0.058823529412)
        actual = (round(tcomplex_inv.a, 12), round(tcomplex_inv.b, 12))

        self.assertEqual(expected, actual)


    def test_subtraction_function(self):
        tcomplex_1 = TComplex(4, 1)
        tcomplex_2 = TComplex(2, 3)
        tcomplex_sub = tcomplex_1.sub(tcomplex_2)

        expected = (2, -2)
        actual = (tcomplex_sub.a, tcomplex_sub.b)

        self.assertEqual(expected, actual)


    def test_subtraction(self):
        tcomplex_1 = TComplex(4, 1)
        tcomplex_2 = TComplex(2, 3)
        tcomplex_sub = tcomplex_1 - tcomplex_2

        expected = (2, -2)
        actual = (tcomplex_sub.a, tcomplex_sub.b)

        self.assertEqual(expected, actual)


    def test_truediv(self):
        tcomplex_1 = TComplex(3, -1)
        tcomplex_2 = TComplex(-5, 2)
        tcomplex_div = tcomplex_1 / tcomplex_2

        expected = (-0.586206896552, -0.034482758621)
        actual = (round(tcomplex_div.a, 12), round(tcomplex_div.b, 12))

        self.assertEqual(expected, actual)


    def test_module(self):
        tcomplex = TComplex(-5, 15)

        expected = 15.811388300841896
        actual = tcomplex.module()

        self.assertEqual(expected, actual)

    
    def test_radian(self):
        tcomplex = TComplex(3, 6)

        expected = 1.10714871779
        actual = round(tcomplex.radian(), 11)
        
        self.assertEqual(expected, actual)


    def test_degrees(self):
        tcomplex = TComplex(6, 2)

        expected = 18.4349488
        actual = round(tcomplex.degrees(), 7)
        
        self.assertEqual(expected, actual)


    def test_pow(self):
        tcomplex_1 = TComplex(4, 9)
        tcomplex_pow = tcomplex_1.pow(3)

        expected = (-908, -297)
        actual = (round(tcomplex_pow.a), round(tcomplex_pow.b))

        self.assertEqual(expected, actual)


    def test_root(self):
        tcomplex_1 = TComplex(5, 2)
        tcomplex_root = tcomplex_1.root(5)

        expected = (1.39630726, 0.10646637)
        actual = (round(tcomplex_root.a, 8), round(tcomplex_root.b, 8))

        self.assertEqual(expected, actual)


    def test_equal(self):
        tcomplex_1 = TComplex(5, 9)
        tcomplex_2 = TComplex("5+i*9")

        self.assertTrue(tcomplex_1 == tcomplex_2)

    
    def test_not_equal(self):
        tcomplex_1 = TComplex(3, 6)
        tcomplex_2 = TComplex("0+i*4")

        self.assertTrue(tcomplex_1 != tcomplex_2)


    def test_get_real_num(self):
        tcomplex = TComplex(7, 21)

        expected = 7
        actual = tcomplex.getRealNum()

        self.assertEqual(expected, actual)
        self.assertIsInstance(actual, float)

    
    def test_get_imaginary_num(self):
        tcomplex = TComplex(7, 21)

        expected = 21
        actual = tcomplex.getImNum()

        self.assertEqual(expected, actual)
        self.assertIsInstance(actual, float)

    
    def test_get_real_num(self):
        tcomplex = TComplex(12, 8)

        expected = "12.0"
        actual = tcomplex.getRealStr()

        self.assertEqual(expected, actual)
        self.assertIsInstance(actual, str)

    
    def test_get_imaginary_str(self):
        tcomplex = TComplex(12, 8)

        expected = "8.0"
        actual = tcomplex.getImStr()

        self.assertEqual(expected, actual)
        self.assertIsInstance(actual, str)

    
    def test_get_complex_str(self):
        tcomplex = TComplex(5, -11)

        expected = "5.0-i*11.0"
        actual = tcomplex.getComplexStr()

        self.assertEqual(expected, actual)
