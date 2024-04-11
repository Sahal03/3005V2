import psycopg2
class Trainer:
    def __init__(self, fName, lName, number,salary,cur):
        self.availabilities = []

        self.cursor = cur
        self.cursor.execute("INSERT INTO trainers (first_name,last_name,phone_number,salary) VALUES (%s, %s, %s, %s);",(fName,lName,number,salary))
