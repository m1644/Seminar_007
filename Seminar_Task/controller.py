# Модуль вычисления

import calk_complex
import calk_float
import user_interface
import logger

def run():
    temp = user_interface.initial()
    if 'j' in temp[0] and 'j' in temp[1]:
        result = calk_complex.calc(temp[0], temp[1], temp[2])
    else:
        result = calk_float.calc(temp[0], temp[1], temp[2])
    print(f'Результат = {result}')
    logger.log_to_file(temp, result)
    return result
