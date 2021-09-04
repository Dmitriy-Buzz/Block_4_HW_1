import db

def get_employees():
    for people in db.employees:
        print(people['name'])


get_employees()