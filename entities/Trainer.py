import psycopg2
from entities.Availability import Availability

class Trainer:
    def __init__(self, id, fName, lName,email,salary,cur):
        self.availabilities = []
        self.cursor = cur
        
        if id == None:
            self.cursor.execute("INSERT INTO trainers (first_name,last_name,email,salary) VALUES (%s, %s, %s, %s);",(fName,lName,email,salary))
            self.id = self.cursor.execute("SELECT trainer_id FROM trainers ORDER BY trainer_id DESC LIMIT 1;")
        else:
            self.id = id
        self.fName = fName
        self.lName = lName
        self.email = email
        self.salary = salary

    def profile(self):
        print("")
        print("\nWelcome Trainer!")
        print("1: Manage your Availabilities")
        print("2: Search for Members")
        print("Press Any Key to Return to Main Menu")
        choice = input("Select choice: ")

        if choice == '1':
            self.manageAvail()
        elif choice == '2':
            self.searchMember()
        
    def manageAvail(self):
        # view availabilities
        self.viewAvailabilities()
        # add availability
        print("")
        print("1: Add New Availability")
        print("2: Return to Profile")
        choice = input("Select choice: ")
        if choice == '1':
            self.addAvailability()
        else:
            self.profile()
    
    def viewAvailabilities(self):
        self.cursor.execute("SELECT * FROM availabilities WHERE trainer_id=%s",(self.id,))
        result = self.cursor.fetchall()
        for avail in result:
            print(avail[1]," from ", avail[2], " to ",avail[3])
        print("")
    
    def addAvailability(self):
        print("")
        date = input("Enter the Date (YYYY-MM--DD): ")
        start = input("Enter the start time (HH:MM:SS): ")
        end = input("Enter the end time (HH:MM:SS): ")
        self.availabilities.append(Availability(self.id,date,start,end,self.cursor))
        self.manageAvail()
        
    def searchMember(self):
        # prompt user for name 
        print("")
        fName = input("Search by first name: ")
        fName = "%" + fName + "%"
        # execute query
        self.cursor.execute("SELECT * FROM members WHERE first_name LIKE %s",(fName,))
        result = self.cursor.fetchall()

        #print result
        for member in result:
            for attribute in member:
                print(attribute, end=" ")
            print("")
        
        self.profile()

