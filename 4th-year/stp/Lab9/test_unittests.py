import unittest
from tfrac import TFrac
from tfraceditor import TFracEditor

class UnitTests(unittest.TestCase):
    def test_is_zero_false(self):
        tfrac = TFrac(24, 4)
        tfraceditor = TFracEditor(tfrac)

        self.assertFalse(tfraceditor.isZero())

    def test_is_zero_true(self):
        tfrac = TFrac(0, 5)
        tfraceditor = TFracEditor(tfrac)

        self.assertTrue(tfraceditor.isZero())

    def test_change_sign_minus(self):
        tfrac = TFrac(4, 3)
        tfraceditor = TFracEditor(tfrac)
        tfraceditor.changeSign()

        expected = tfraceditor.getTFracStr()
        actual = '-4/3'

        self.assertEqual(expected, actual)

    def test_change_sign_plus(self):
        tfrac = TFrac(-3, 8)
        tfraceditor = TFracEditor(tfrac)
        tfraceditor.changeSign()

        expected = tfraceditor.getTFracStr()
        actual = '3/8'

        self.assertEqual(expected, actual)

    def test_add_number(self):
        tfrac = TFrac(5, 3)
        tfraceditor = TFracEditor(tfrac)
        tfraceditor.addNumber(7)

        expected = tfraceditor.getTFracStr()
        actual = '26/3'

        self.assertEqual(expected, actual)

    def test_add_zero(self):
        tfrac = TFrac(7, 6)
        tfraceditor = TFracEditor(tfrac)
        tfraceditor.addZero()

        expected = tfraceditor.getTFracStr()
        actual = '7/60'

        self.assertEqual(expected, actual)

    def test_remove_char(self):
        tfrac = TFrac(3, 100)
        tfraceditor = TFracEditor(tfrac)
        tfraceditor.removeChar()

        expected = tfraceditor.getTFracStr()
        actual = '3/10'

        self.assertEqual(expected, actual)

    def test_clear(self):
        tfrac = TFrac(14, 23)
        tfraceditor = TFracEditor(tfrac)
        tfraceditor.clear()

        expected = tfraceditor.getTFracStr()
        actual = '0/1'

        self.assertEqual(expected, actual)

    def test_set_tfrac_str(self):
        tfrac = TFrac(14, 23)
        tfraceditor = TFracEditor(tfrac)
        tfraceditor.setTFracStr('15/31')

        expected = tfraceditor.getTFracStr()
        actual = '15/31'

        self.assertEqual(expected, actual)

    def test_get_tfrac_str(self):
        tfrac = TFrac(7, 3)
        tfraceditor = TFracEditor(tfrac)
        
        expected = tfraceditor.getTFracStr()
        actual = '7/3'

        self.assertEqual(expected, actual)