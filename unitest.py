import unittest
import complexcalculator as comp
import math

class unit_calculadora(unittest.TestCase):

    def test_sum(self):

        self.assertEqual(comp.sum_comps((5, 20), (15, -7)), (20, 13))

    def test_rest(self):

        self.assertEqual(comp.res_comp((5, 20), (15, -7)), (-10, 27))

    def test_mult(self):

        self.assertEqual(comp.mult_comp((5, 20), (15, -7)), (215, 265))

    def test_div(self):

        self.assertEqual(comp.div_comp((5, 20), (15, -7)), (-0.23722627737226276, 1.2226277372262773))

    def test_mod(self):

        self.assertEqual(comp.mod_comp((-4, 3)), 5)

    def test_conj(self):

        self.assertEqual(comp.conj_comp((-15, -10)), (15, 10))

    def test_polar_cart(self):

        self.assertEqual(comp.polar_cart((math.sqrt(2), (math.pi*3)/4)), (-1.0, 1.0))

    def test_cart_polar(self):

        self.assertEqual(comp.cart_polar((-1.0, 1.0)), (math.sqrt(2), 135.0))

    def test_fase(self):

        self.assertEqual(comp.c_fase((6, 15)), 68.19859051364818)

if __name__ == '__main__':
    unittest.main()