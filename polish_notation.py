'''
Polish-Notation-Calculator
  * support following mathematical operations: + - * /
  * operands can be both integers and floats,
  * the operations must be written in polish notation: + 2 3,
  * operators and the operands can be separated by arbitrary number of spaces,

Example:
    Expression: + 2 3
    Result: 5
'''

import os

abs_path =os.getcwd()

if ( not os.path.isdir(os.path.join(abs_path, 'log'))) :
   os.mkdir(os.path.join(abs_path, 'log'))

from operator import add,sub,mul,truediv
from datetime import datetime

operations ={'+' : add, 'add' : add,
            '-' : sub, 'sub' : sub,
            '*' : mul, 'mul' : mul,
            '/' : truediv, 'div' : truediv }


def validation_pass(expression_list: list):
    new_list = [1 if unit in operations or (''.join(unit.split('.', 1))).isdecimal() else 0 for unit in expression_list ]
    return all(new_list)



def get_infix(expression_list : list):
    stack = []
    for i in reversed(expression_list) :
        if (i in operations):
            if(check_expression(stack)):
                logging_to_file(0, expression_list, -1)
                return False
            else:
                operand_1 = stack.pop()
                operand_2 = stack.pop()        
                prefix_string = "( {} {} {} )".format(operand_1, i, operand_2)
                stack.append(prefix_string)
        else:
            stack.append(i)
    return stack.pop()



def check_expression(stack):
    if(len(stack)== 1):
        return True        



def logging_to_file(log_type, params, result):
    with open(os.path.join(abs_path, 'log', 'info.log'), 'a+') as f:
        if (log_type):
            if(result.is_integer()): result = int(result)
            f.write('{} :: INFO  :: {} :: {} \n'.format(datetime.now()," ".join(params),result))
        else:
            f.write('{} :: ERROR :: Invalid expression :: {} \n'.format(datetime.now()," ".join(params)))

        f.seek(0)
        error_cnt = 0
        info_cnt = 0
        one_line = f.readlines()
        
        for line in one_line :
            if 'ERROR' in line:
                error_cnt +=1
            if 'INFO' in line:  
                info_cnt +=1
        
    print_report(log_type,params,result,error_cnt,info_cnt)
    f.close()
    
    
def print_report(log_type,params,result,error_cnt,info_cnt):
    
    if(log_type):
        print(f'Expression : {" ".join(params)} \nResult: {result} \nReport: INFO-{info_cnt}, ERROR-{error_cnt}')
    else:
        print(f'Expression : {" ".join(params)} \nERROR: Invalid expression \nReport: INFO-{info_cnt}, ERROR-{error_cnt} ')


def calculator(): 
    expression = input('type your code : ').split() 
    if(validation_pass(expression)):
        if (get_infix(expression) is not False):
            result = eval(get_infix(expression))
            logging_to_file(1, expression, result)
    else:
        logging_to_file(0, expression, -1)

calculator()


