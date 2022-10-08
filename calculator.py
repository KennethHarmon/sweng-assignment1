from typing import List
running = True

Valid_operators = set(['+', '-', '*'])
Priority = {'+':1, '-':1, '*':2}

def peek(some_list):
    return some_list[-1]

def convert_input_to_list(user_input: str) -> List:
    output_list = user_input.split(' ')
    i = -1
    for elem in output_list:
        i += 1
        if elem not in Valid_operators:
            output_list[i] = int(elem)
    return output_list

def switch_expression_to_postfix(expression: List) -> List:
    stack = []
    output_list = []

    for elem in expression:
        if elem not in Valid_operators:
                output_list.append(elem)
        else: 
            print(f'Is operator {elem}')
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
            stack.insert(0,digit)
        elif not len(stack)==0:
            if digit == "-":
                currentVal = stack.pop() - stack.pop()
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

    

while (running):
    user_input = input("Please enter the expression you would like to caluclate: ") 
    infix_expression = convert_input_to_list(user_input)
    print(f'Infix: {infix_expression}')
    postfix_expression = switch_expression_to_postfix(infix_expression)
    print(f'Postfix: {postfix_expression}')
    answer = evaluate_postfix_expression(postfix_expression)
    print(f'Final answer: {answer}')
    

    
