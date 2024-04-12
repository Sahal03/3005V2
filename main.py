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
cursor.execute(open("scripts/initializer.sql","r").read())

# populate sample data
cursor.execute(open("scripts/populateDummy.sql","r").read())

def mainMenu():
    # initial prompt user
    print("1. Member")
    print("2. Trainer")
    print("3. Admin")
    print("4. Press 4 or any key to exit.")
    choice = input("Select Your Type of User: ")

    if choice == '1':
        memberPrompt()
    elif choice == '2':
        trainerPrompt()
    elif choice == '3':
        adminPrompt()
    else:
        print("Have a good day")

def memberPrompt():
    return

def trainerPrompt():
    email = input("Please enter your email to sign in: ")
    trainer = None
    cursor.execute("SELECT * FROM trainers WHERE email=%s",(email,))

    trainerResult = cursor.fetchone()

    if trainerResult is None:
        print("Trainer not found")
        choice = input("Press 1 to try again or anykey to return to main menu.")
        if choice == '1':
            trainerPrompt()
        else:
            mainMenu()
    else:
        trainer = Trainer(trainerResult[0],trainerResult[1],trainerResult[2],trainerResult[3],trainerResult[4],cursor)
        trainer.profile()
        mainMenu()

def adminPrompt():
    return

mainMenu()
cursor.close()
conn.close()