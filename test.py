import unittest
from calculator import convert_input_to_list, switch_expression_to_postfix


class TestCalculatorMethods(unittest.TestCase):
    def test_convert_input_to_list(self):
        self.assertEqual(convert_input_to_list("123+3234+512+64"), [123, '+', 3234, '+', 512, '+', 64])
        self.assertEqual(convert_input_to_list("828-832-759-64"), [828, '-', 832, '-', 759, '-', 64]) 
        self.assertEqual(convert_input_to_list("345*34*435*2"), [345, '*', 34, '*', 435, '*', 2]) 
        self.assertEqual(convert_input_to_list("12+34-52*6"), [12, '+', 34, '-', 52, '*', 6])
        self.assertEqual(convert_input_to_list("+-**-+"), ['+', '-', '*', '*', '-', '+']) 
        self.assertEqual(convert_input_to_list(""), [])  
        with self.assertRaises(TypeError):
            convert_input_to_list("2g/6*45gdsf")

    def test_switch_expression_to_postfix(self):
        self.assertEqual(switch_expression_to_postfix([123, '+', 3234, '+', 512, '+', 64]), [123, 3234, '+', 512, '+', 64, '+'])
        self.assertEqual(switch_expression_to_postfix([828, '-', 832, '-', 759, '-', 64]), [828, 832, '-', 759, '-', 64, '-'])
        self.assertEqual(switch_expression_to_postfix([345, '*', 34, '*', 435, '*', 2]), [345, 34, '*', 435, '*', 2, '*'])
        self.assertEqual(switch_expression_to_postfix([12, '+', 34, '-', 52, '*', 6]), [12, 34, '+', 52, 6, '*', '-'])
        self.assertEqual(switch_expression_to_postfix(['+', '-', '*', '*', '-', '+']), ['+', '*', '*', '-', '-', '+'])
        self.assertEqual(switch_expression_to_postfix([]), [])  

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")