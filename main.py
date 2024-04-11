import psycopg2

connection = psycopg2.connect(host='localhost', dbname="postgres", user="postgres",password="admin",port=5432)
cursor = connection.cursor()

# create table
cursor.execute(open("scripts/initializer.sql","r").read())
connection.commit()

# populate sample data
# cursor.execute(open("scripts/populateDummy.sql","r").read())
# connection.commit()

cursor.close()
connection.close()