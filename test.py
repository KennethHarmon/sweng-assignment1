from calculator.py import evaluate_postfix_expression

def initial_test():
    assert "loud noises".upper() == "LOUD NOISES"
    
def test_postfixevaluation():
    assert evaluate_postfix_expression([2, 2, '+']) == 4

