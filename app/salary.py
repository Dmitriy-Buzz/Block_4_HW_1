from db import employees


def get_salary():
    for sm in employees:
        print(f"{sm['name']} - {sm['salary']} руб.")



get_salary()