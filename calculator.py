from ast import Raise
from typing import List

Valid_operators = set(['+', '-', '*'])
Priority = {'+':1, '-':1, '*':2}

def convert_input_to_list(user_input: str) -> List:
    current_num = ''
    ouptut_list = []
    for char in user_input:
        if char.isnumeric():
            current_num += char
        elif char in Valid_operators:
            if current_num != '':
                ouptut_list.append(int(current_num))
                current_num = ''
            ouptut_list.append(char)
        elif char == ' ':
            pass
        else:
            raise TypeError("Error, invalid token in input string, please only enter integers, '*', '+', '-'.")
    
    if current_num != '':
        ouptut_list.append(int(current_num))
    
    return ouptut_list

def switch_expression_to_postfix(expression: List) -> List:
    stack = []
    output_list = []

    for elem in expression:
        if elem not in Valid_operators:
                output_list.append(elem)
        else: 
            while stack and Priority[elem]<=Priority[stack[-1]]:
                output_list.append(stack.pop())
            stack.append(elem)

    while stack:
        output_list+=stack.pop()

    return output_list


def evaluate_postfix_expression(postfix_list):
    stack = []     
    for digit in postfix_list:
        currentVal = None
        if isinstance(digit,int):
            stack.append(digit)
        elif not len(stack)==0:
            if digit == "-":
                currentVal = -stack.pop() + stack.pop()
            elif digit == "+":
                currentVal = stack.pop() + stack.pop()
            elif digit == "*":
                currentVal = stack.pop() * stack.pop()

            if currentVal is not None:
                stack.append(currentVal)
            else:
                raise Exception("Invalid input: %s"%digit)

    if not len(stack) == 0 :      
        return stack.pop()
    else:
        return

    

if __name__ == "__main__":
    user_input = input("Please enter the expression you would like to caluclate: ") 
    infix_expression = convert_input_to_list(user_input)
    print(f'Infix: {infix_expression}')
    postfix_expression = switch_expression_to_postfix(infix_expression)
    print(f'Postfix: {postfix_expression}')
    answer = evaluate_postfix_expression(postfix_expression)
    print(f'Final answer: {answer}')
    

    
