# Логирование в файл

from datetime import datetime

def log_to_file(temp, result):
    with open('Seminar_Task\log.csv', 'a') as file:
        file.write(f'{datetime.today()}; {temp[0]}; {temp[2]};{temp[1]};{result}; \n')
