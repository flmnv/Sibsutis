import unittest
from unittest import result
from tfrac import TFrac


class UnitTests(unittest.TestCase):
    def test_create_fraction_devision_by_zero(self):
        a: int = 10
        b: int = 0

        self.assertRaises(ZeroDivisionError, TFrac, a, b)


    def test_create_fraction_standart(self):
        tfrac = TFrac(0, 3)

        expected = (0, 3)
        actual = (tfrac.a, tfrac.b)

        self.assertEqual(expected, actual)


    def test_create_fraction_short(self):
        tfrac = TFrac(180, 35)

        expected = (36, 7)
        actual = (tfrac.a, tfrac.b)

        self.assertEqual(expected, actual)


    def test_create_fraction_sign_b(self):
        tfrac = TFrac(5, -7)

        expected = (-5, 7)
        actual = (tfrac.a, tfrac.b)

        self.assertEqual(expected, actual)

    
    def test_create_fraction_sign_ab(self):
        tfrac = TFrac(-15, -4)

        expected = (15, 4)
        actual = (tfrac.a, tfrac.b)

        self.assertEqual(expected, actual)

    
    def test_create_fraction_string(self):
        tfrac = TFrac("18/48")

        expected = (3, 8)
        actual = (tfrac.a, tfrac.b)

        self.assertEqual(expected, actual)


    def test_copy(self):
        f = "27/-36"
        tfrac = TFrac(f)
        tfrac_copy: TFrac = TFrac(1, 3)
        tfrac_copy.copy(tfrac)

        expected = (-3, 4)
        actual = (tfrac_copy.a, tfrac_copy.b)

        self.assertEqual(expected, actual)


    def test_add(self):
        tfrac_1 = TFrac("1/2")
        tfrac_2 = TFrac(-3, 4)
        tfrac_3 = tfrac_1 + tfrac_2

        expected = (-1, 4)
        actual = (tfrac_3.a, tfrac_3.b)

        self.assertEqual(expected, actual)

    
    def test_addf(self):
        tfrac_1 = TFrac("1/2")
        tfrac_2 = TFrac(-3, 4)
        tfrac_3 = tfrac_1.add(tfrac_2)

        expected = (-1, 4)
        actual = (tfrac_3.a, tfrac_3.b)

        self.assertEqual(expected, actual)


    def test_mul(self):
        tfrac_1 = TFrac("5/-6")
        tfrac_2 = TFrac(-3, 2)
        tfrac_3 = tfrac_1 * tfrac_2

        expected = (5, 4)
        actual = (tfrac_3.a, tfrac_3.b)

        self.assertEqual(expected, actual)


    def test_sub(self):
        tfrac_1 = TFrac("1/2")
        tfrac_2 = TFrac(3, 7)
        tfrac_3 = tfrac_1 - tfrac_2

        expected = (1, 14)
        actual = (tfrac_3.a, tfrac_3.b)

        self.assertEqual(expected, actual)

    
    def test_subf(self):
        tfrac_1 = TFrac("1/2")
        tfrac_2 = TFrac(3, 7)
        tfrac_3 = tfrac_1.sub(tfrac_2)

        expected = (1, 14)
        actual = (tfrac_3.a, tfrac_3.b)

        self.assertEqual(expected, actual)


    def test_truediv(self):
        tfrac_1 = TFrac("1/2")
        tfrac_2 = TFrac(1, 4)
        tfrac_3 = tfrac_1 / tfrac_2

        expected = (2, 1)
        actual = (tfrac_3.a, tfrac_3.b)

        self.assertEqual(expected, actual)


    def test_pow(self):
        tfrac_1 = TFrac("2/4")
        tfrac_2 = tfrac_1 ** 2

        expected = (1, 4)
        actual = (tfrac_2.a, tfrac_2.b)

        self.assertEqual(expected, actual)


    def test_rtruediv(self):
        tfrac_1 = TFrac("1/2")
        tfrac_2 = 2 / tfrac_1

        expected = (4, 1)
        actual = (tfrac_2.a, tfrac_2.b)

        self.assertEqual(expected, actual)


    def test_equate(self):
        tfrac_1 = TFrac("1/4")
        tfrac_2 = TFrac(1, 4)

        self.assertTrue(tfrac_1 == tfrac_2)


    def test_great(self):
        tfrac_1 = TFrac(10, 5)
        tfrac_2 = TFrac("1/20")

        self.assertTrue(tfrac_1 > tfrac_2)

    
    def test_getNumeratorNum(self):
        tfrac_1 = TFrac(3, 5)

        expected = 3
        actual = tfrac_1.getNumeratorNum()

        self.assertEqual(expected, actual)

    
    def test_getDenominatorNum(self):
        tfrac_1 = TFrac(3, 5)

        expected = 5
        actual = tfrac_1.getDenomiratorNum()

        self.assertEqual(expected, actual)


    def test_getNumeratorStr(self):
        tfrac_1 = TFrac(3, 5)

        expected = "3"
        actual = tfrac_1.getNumeratorStr()

        self.assertEqual(expected, actual)


    def test_getDenominatorStr(self):
        tfrac_1 = TFrac(3, 5)

        expected = "5"
        actual = tfrac_1.getDenomiratorStr()

        self.assertEqual(expected, actual)


    def test_getStr(self):
        tfrac_1 = TFrac(3, 5)

        expected = "3/5"
        actual = tfrac_1.getStr()

        self.assertEqual(expected, actual)
