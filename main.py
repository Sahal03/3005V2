import psycopg2 as ps
from entities.Trainer import Trainer
#Needed Credentials to access the db
DB_NAME = "V2"
DB_USER = "postgres"
DB_PASS = "admin"
DB_HOST = "localhost"
DB_PORT = 5432

conn = ps.connect(database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT)
conn.autocommit = True
cursor = conn.cursor()

# create table
# cursor.execute(open("scripts/initializer.sql","r").read())

# populate sample data
# cursor.execute(open("scripts/populateDummy.sql","r").read())
# connection.commit()

t1 = Trainer("Sahal","Aidid","911","25000",cursor)
cursor.close()
conn.close()