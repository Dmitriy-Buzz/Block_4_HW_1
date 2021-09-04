from app.people import get_employees
from app.salary import get_salary
import datetime

def main():
    print(f"Добрый день пользователь, текущая сессия: {datetime.datetime.now()}")
    command = input('Введите команду: ')
    if command == 'l':
        get_employees()
    if command == 's':
        get_salary()

if __name__ == '__main__':
    main()