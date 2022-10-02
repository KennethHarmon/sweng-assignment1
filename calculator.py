from typing import List


running = True

def convert_input_to_list(user_input: str) -> List:
    current_num = ''
    ouptut_list = []
    valid_operators = ['+', '-', '*']
    for char in user_input:
        if char.isnumeric():
            current_num += char
        elif char in valid_operators:
            if current_num != '':
                ouptut_list.append(int(current_num))
                current_num = ''
            ouptut_list.append(char)
        elif char == ' ':
            pass
        else:
            print("Error, invalid token in input string, please only enter integers, '*', '+', '-'.")
    
    if current_num != '':
        ouptut_list.append(int(current_num))
    
    return ouptut_list

while (running):
    user_input = input("Please enter the expression you would like to caluclate: ") 
    output_list = convert_input_to_list(user_input)
    print(output_list)

    