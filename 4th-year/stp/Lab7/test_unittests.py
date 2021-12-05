import unittest
from tpnumber import TPNumber


class UnitTests(unittest.TestCase):
    def test_create_tpnumber_num(self):
        tpnumber = TPNumber(1, 2, 3)

        expected = (1, 2, 3)
        actual = (tpnumber.n, tpnumber.b, tpnumber.c)

        self.assertEqual(expected, actual)
        self.assertIsInstance(tpnumber.n, float)
        self.assertIsInstance(tpnumber.b, int)
        self.assertIsInstance(tpnumber.c, int)

    def test_create_tpnumber_str(self):
        tpnumber = TPNumber("1", "2", "3")

        expected = (1, 2, 3)
        actual = (tpnumber.n, tpnumber.b, tpnumber.c)

        self.assertEqual(expected, actual)
        self.assertIsInstance(tpnumber.n, float)
        self.assertIsInstance(tpnumber.b, int)
        self.assertIsInstance(tpnumber.c, int)

    def test_create_tpnumber_raise_b_less_2(self):
        self.assertRaises(ValueError, TPNumber, 1, 1, 3)

    def test_create_tpnumber_raise_b_more_16(self):
        self.assertRaises(ValueError, TPNumber, 1, 17, 3)

    def test_create_tpnumber_raise_c_less_0(self):
        self.assertRaises(ValueError, TPNumber, 1, 2, -1)

    def test_copy(self):
        tpnumber = TPNumber(1, 2, 3)
        tpnumber_copy = tpnumber.copy()

        expected = (1, 2, 3)
        actual = (tpnumber_copy.n, tpnumber_copy.b, tpnumber_copy.c)

        self.assertEqual(expected, actual)
        self.assertIsInstance(tpnumber_copy.n, float)
        self.assertIsInstance(tpnumber_copy.b, int)
        self.assertIsInstance(tpnumber_copy.c, int)

    def test_add(self):
        tpnumber_1 = TPNumber(1, 2, 3)
        tpnumber_2 = TPNumber(16, 2, 3)
        tpnumber_result = tpnumber_1 + tpnumber_2

        expected = (17, 2, 3)
        actual = (tpnumber_result.n, tpnumber_result.b, tpnumber_result.c)

        self.assertEqual(expected, actual)
        self.assertIsInstance(tpnumber_result.n, float)
        self.assertIsInstance(tpnumber_result.b, int)
        self.assertIsInstance(tpnumber_result.c, int)

    def test_add_raise_b_not_eqals(self):
        tpnumber_1 = TPNumber(1, 5, 3)
        tpnumber_2 = TPNumber(1, 8, 3)

        self.assertRaises(ValueError, lambda: tpnumber_1 + tpnumber_2)

    def test_add_raise_c_not_eqals(self):
        tpnumber_1 = TPNumber(1, 2, 11)
        tpnumber_2 = TPNumber(1, 2, 6)

        self.assertRaises(ValueError, lambda: tpnumber_1 + tpnumber_2)

    def test_mul(self):
        tpnumber_1 = TPNumber(6, 2, 3)
        tpnumber_2 = TPNumber(8, 2, 3)
        tpnumber_result = tpnumber_1 * tpnumber_2

        expected = (48, 2, 3)
        actual = (tpnumber_result.n, tpnumber_result.b, tpnumber_result.c)

        self.assertEqual(expected, actual)
        self.assertIsInstance(tpnumber_result.n, float)
        self.assertIsInstance(tpnumber_result.b, int)
        self.assertIsInstance(tpnumber_result.c, int)

    def test_mul_raise_b_not_eqals(self):
        tpnumber_1 = TPNumber(1, 5, 3)
        tpnumber_2 = TPNumber(1, 8, 3)

        self.assertRaises(ValueError, lambda: tpnumber_1 * tpnumber_2)

    def test_mul_raise_c_not_eqals(self):
        tpnumber_1 = TPNumber(1, 2, 11)
        tpnumber_2 = TPNumber(1, 2, 6)

        self.assertRaises(ValueError, lambda: tpnumber_1 * tpnumber_2)

    def test_sub(self):
        tpnumber_1 = TPNumber(49, 2, 3)
        tpnumber_2 = TPNumber(27, 2, 3)
        tpnumber_result = tpnumber_1 - tpnumber_2

        expected = (22, 2, 3)
        actual = (tpnumber_result.n, tpnumber_result.b, tpnumber_result.c)

        self.assertEqual(expected, actual)
        self.assertIsInstance(tpnumber_result.n, float)
        self.assertIsInstance(tpnumber_result.b, int)
        self.assertIsInstance(tpnumber_result.c, int)

    def test_sub_raise_b_not_eqals(self):
        tpnumber_1 = TPNumber(1, 5, 3)
        tpnumber_2 = TPNumber(1, 8, 3)

        self.assertRaises(ValueError, lambda: tpnumber_1 - tpnumber_2)

    def test_sub_raise_c_not_eqals(self):
        tpnumber_1 = TPNumber(1, 2, 11)
        tpnumber_2 = TPNumber(1, 2, 6)

        self.assertRaises(ValueError, lambda: tpnumber_1 - tpnumber_2)

    def test_truediv(self):
        tpnumber_1 = TPNumber(36, 2, 3)
        tpnumber_2 = TPNumber(6, 2, 3)
        tpnumber_result = tpnumber_1 / tpnumber_2

        expected = (6, 2, 3)
        actual = (tpnumber_result.n, tpnumber_result.b, tpnumber_result.c)

        self.assertEqual(expected, actual)
        self.assertIsInstance(tpnumber_result.n, float)
        self.assertIsInstance(tpnumber_result.b, int)
        self.assertIsInstance(tpnumber_result.c, int)

    def test_truediv_raise_b_not_eqals(self):
        tpnumber_1 = TPNumber(1, 5, 3)
        tpnumber_2 = TPNumber(1, 8, 3)

        self.assertRaises(ValueError, lambda: tpnumber_1 / tpnumber_2)

    def test_truediv_raise_c_not_eqals(self):
        tpnumber_1 = TPNumber(1, 2, 11)
        tpnumber_2 = TPNumber(1, 2, 6)

        self.assertRaises(ValueError, lambda: tpnumber_1 / tpnumber_2)

    def test_reverse(self):
        tpnumber = TPNumber(5, 2, 3)
        tpnumber = tpnumber.reverse()

        expected = (1/5, 2, 3)
        actual = (tpnumber.n, tpnumber.b, tpnumber.c)

        self.assertEqual(expected, actual)

    def test_rise_n_is_0(self):
        tpnumber = TPNumber(0, 2, 3)

        self.assertRaises(ZeroDivisionError, tpnumber.reverse)

    def test_sq(self):
        tpnumber = TPNumber(-7, 2, 3)
        tpnumber = tpnumber.sq()

        expected = (49, 2, 3)
        actual = (tpnumber.n, tpnumber.b, tpnumber.c)

        self.assertEqual(expected, actual)

    def test_getPNum(self):
        tpnumber = TPNumber(5, 2, 3)

        expected = tpnumber.getPNum()
        actual = 5

        self.assertEqual(expected, actual)

    def test_getPNum(self):
        tpnumber = TPNumber(5, 2, 3)

        expected = tpnumber.getPStr()
        actual = "5"

        self.assertEqual(expected, actual)

    def test_getBaseNum(self):
        tpnumber = TPNumber(5, 2, 3)

        expected = tpnumber.getBaseNum()
        actual = 2

        self.assertEqual(expected, actual)

    def test_getBaseStr(self):
        tpnumber = TPNumber(5, 2, 3)

        expected = tpnumber.getBaseStr()
        actual = "2"

        self.assertEqual(expected, actual)

    def test_getCommaNum(self):
        tpnumber = TPNumber(5, 2, 3)

        expected = tpnumber.getCommaNum()
        actual = 3

        self.assertEqual(expected, actual)

    def test_getCommaStr(self):
        tpnumber = TPNumber(5, 2, 3)

        expected = tpnumber.getCommaStr()
        actual = "3"

        self.assertEqual(expected, actual)

    def test_setBase_num(self):
        tpnumber = TPNumber(5, 2, 3)
        tpnumber.setBase(7)

        expected = (5, 7, 3)
        actual = (tpnumber.n, tpnumber.b, tpnumber.c)

        self.assertEqual(expected, actual)

    def test_setBase_str(self):
        tpnumber = TPNumber(5, 2, 3)
        tpnumber.setBase("7")

        expected = (5, 7, 3)
        actual = (tpnumber.n, tpnumber.b, tpnumber.c)

        self.assertEqual(expected, actual)

    def test_setBase_rise_b_less_2(self):
        tpnumber = TPNumber(5, 2, 3)

        self.assertRaises(ValueError, tpnumber.setBase, 0)

    def test_setBase_rise_b_more_16(self):
        tpnumber = TPNumber(5, 2, 3)

        self.assertRaises(ValueError, tpnumber.setBase, 17)

    def test_setBase_num(self):
        tpnumber = TPNumber(5, 2, 3)
        tpnumber.setComma(24)

        expected = (5, 2, 24)
        actual = (tpnumber.n, tpnumber.b, tpnumber.c)

        self.assertEqual(expected, actual)

    def test_setBase_str(self):
        tpnumber = TPNumber(5, 2, 3)
        tpnumber.setComma("24")

        expected = (5, 2, 24)
        actual = (tpnumber.n, tpnumber.b, tpnumber.c)

        self.assertEqual(expected, actual)

    def test_setBase_rise_c_less_0(self):
        tpnumber = TPNumber(5, 2, 3)

        self.assertRaises(ValueError, tpnumber.setComma, -1)
