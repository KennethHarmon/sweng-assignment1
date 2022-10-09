import unittest
from calculator import convert_input_to_list, switch_expression_to_postfix,  evaluate_postfix_expression


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

    def test_evaluate_postfix_expression(self):
        self.assertEqual(evaluate_postfix_expression([123, 3234, '+', 512, '+', 64, '+']), 3933)
        self.assertEqual(evaluate_postfix_expression([828, 832, '-', 759, '-', 64, '-']), -827)
        self.assertEqual(evaluate_postfix_expression([345, 34, '*', 435, '*', 2, '*']), 10205100)
        self.assertEqual(evaluate_postfix_expression([12, 34, '+', 52, 6, '*', '-']), -266)
        self.assertEqual(evaluate_postfix_expression(['+', '*', '*', '-', '-', '+']), None)
        self.assertEqual(evaluate_postfix_expression([]), None)
        

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
