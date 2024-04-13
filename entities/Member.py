
import psycopg2 as ps


#Needed Credentials to access the db
DB_NAME = "V2"
DB_USER = "postgres"
DB_PASS = "069359"
DB_HOST = "localhost"
DB_PORT = 5432

class Member:
    def __init__(self, fName, lName, EMAIL, db):
        exist = db.cursor().execute(f"""SELECT EXISTS (
        SELECT 1
        FROM members
        WHERE email = {EMAIL}
        );""")
        
        if exist:
            self.fName = db.cursor().execute(f"SELECT first_name FROM members WHERE email = {EMAIL};")
            self.lName = db.cursor().execute(f"SELECT last_name FROM members WHERE email = {EMAIL};")
            self.EMAIL = EMAIL
            self.db = db.cursor()
            self.ID = db.cursor().execute(f"SELECT member_id FROM members WHERE email = {EMAIL};")
            self.goalWeight = db.cursor().execute(f"""SELECT g.weight
                                                    FROM goals AS g
                                                    INNER JOIN members AS m ON g.member_id = m.member_id
                                                    WHERE m.member_id = {self.ID};""")
            self.goalTime = db.cursor().execute(f"""SELECT g.time
                                                    FROM goals AS g
                                                    INNER JOIN members AS m ON g.member_id = m.member_id
                                                    WHERE m.member_id = {self.ID};""")
            self.goalStreak = db.cursor().execute(f"""SELECT g.streak
                                                    FROM goals AS g
                                                    INNER JOIN members AS m ON g.member_id = m.member_id
                                                    WHERE m.member_id = {self.ID};""")
            
            self.average_bpm = db.cursor().execute(f"""
                                                    SELECT h.average_bpm
                                                   FROM health as h
                                                   INNER JOIN members as m on h.member_id = m.member_id
                                                   WHERE m.member_id = {self.ID}
                                                    """)
            self.muscle = db.cursor.execute(f"""
                                                SELECT h.muscle_mass
                                                FROM health as h
                                                INNER JOIN members as m on h.member_id = m.member_id
                                                WHERE m.member_id = {self.ID}
                                                    """)
            self.weight = db.cursor.execute(f"""
                                                SELECT h.weight
                                                FROM health as h
                                                INNER JOIN members as m on h.member_id = m.member_id
                                                WHERE m.member_id = {self.ID}
                                                    """)
            self.bmi = db.cursor.execute(f"""
                                                SELECT h.bmi
                                                FROM health as h
                                                INNER JOIN members as m on h.member_id = m.member_id
                                                WHERE m.member_id = {self.ID}
                                                    """)                                          
                                            

        else:

            self.fName = fName
            self.lName = lName
            self.EMAIL = EMAIL
            self.goalWeight = "Not set"
            self.goalTime = "Not set"
            self.goalStreak = "Not set"
            self.average_bpm = "Not set"
            self.muscle = "Not set"
            self.weight = "Not set"
            self.bmi = "Not set"
            self.db = db.cursor()

            db.execute("INSERT INTO members (fName, lName, email) VALUES (%s, %s, %s)", fName, lName, EMAIL)
            self.ID = db.cursor().fetchone()[0]
            print(self.ID)
            db.execute(f"INSERT INTO goals (member_id, weight, time, streak) VALUES ({self.ID},{self.goalWeight},{self.goalTime},{self.goalStreak})")
            db.execute(f"INSERT INTO health (member_id, average_bpm, muscle_mass, weight, bmi) VALUES ({self.ID},{self.average_bpm},{self.muscle},{self.weight}, {self.bmi})")

    def ui(self):
        print("\nWelcome ", self.fName, "!")
        print("1: Profile Management")
        print("2: Dashboard Display")
        print("3: Schedule Management")
        print("Press Any Key to Return to Main Menu")
        choice = input("Select choice: ")

        if choice == '1':
            self.profile_ui()
        elif choice == '2':
            self.dashboard_ui()
        elif choice == '3':
            self.schedule_ui()

    def dashboard(self, command):
        if command == "E" or "EXERCISE" or "EXERCISE ROUTINES":
            print("Please look at the following routines! \n")
            self.display_exercise(self)
        elif command == "F" or "FITNESS" or "FITNESS ACHIEVEMENTS":
            print("Please look at what the different achievements! \n")
            self.display_fitness(self)
        elif command == "H" or "HEALTH" or "STATISTICS":
            print("Please look at the following health statistics! \n")
            self.display_health(self)
        elif command == "M" or "MAIN" or "MENU":
            self.ui()
        else:
            print("Unknown command, please try again...")
            self.dashboard_ui()

    def dashboard_ui(self):
            print("E or EXERCISE or EXERCISE ROUTINES, for exercise routines")
            print("F or FITNESS or FITNESS ACHIEVEMENTS, for your fitness achievements")
            print("H or HEALTH or STATISTICS, for your Health Statistics")
            print("M or MAIN or MENU, to return to Main Menu")
            param = input("Enter your selection: ")
            self.dashboard(param)
    
    def profile(self, command):
        if command == "U" or "UPDATE" or "UPDATE PERSONAL INFORMATION":
            print("Please Select what info you'd like to update from the following:")
            self.update_personal(self)
        elif command == "F" or "FITNESS" or "GOALS" or "FITNESS GOALS":
            print("Please select what goals you'd like to update from the following:")
            self.update_goal(self)
        elif command == "H" or "HEALTH" or "HEALTH METRICS":
            print("Please select what health metrics you'd like to update from the following:")
            self.update_health(self)
        elif command == "M" or "MAIN" or "MENU":
            self.ui()
        else:
            print("Unknown command, please try again...")
            self.profile_ui()
    
    def profile_ui(self):
        print("U or UPDATE or UPDATE PERSONAL INFORMATION, to update your personal information")
        print("F or FITNESS or GOALS or FITNESS GOALS, for your fitness goals")
        print("H or HEALTH or HEALTH METRICS, for your health metrics ")
        print("M or MAIN or MENU, to return to Main Menu")
        param = input("Enter your selection: ")
        self.profile(param)
    
    def schedule(self, command):
        if command == "T" or "TRAINER":
            print("Please select a suitable time: ")
            self.schedule_trainer(self)
        elif command == "G" or "GROUP":
            print("Please select a group session")
            self.schedule_group(self)
        else:
            print("Unknown command, please try again...")
            self.schedule_ui()
             
    def schedule_ui(self):
        print("T or TRAINER, to get a trainer")
        print("G or GROUP, to select a group session")
        print("M or MAIN or MENU, to return to Main Menu")
        param = input("Enter your selection: ")
        self.schedule(param)
    
    def schedule_trainer(self):
        availabilities =self.db.execute("""SELECT t.first_name, t.last_name, a.Day, a.start_time, a.end_time
                        FROM trainers AS t
                        JOIN availabilities AS a ON t.trainer_id = a.trainer_id;""")
        print(availabilities)
        trainer_name = input("Please select the trainer name that you want: ")
        trainer_id = self.db.execute(f"""SELECT trainer_id FROM trainers WHERE first_name = {trainer_name}""")
        trainer_day = input("Please input the day using the format YEAR-MONTH-DAY: ")
        trainer_time = input("Please input the starting hour using the format XX:XX:XX : ")
        available = self.db.execute(f"""SELECT available
                                    FROM availabilities
                                    WHERE trainer_id = {trainer_id}""")
        if(available):
            self.db.execute(f""" UPDATE availabilities 
                                 SET available = FALSE 
                                 WHERE trainer_id = {trainer_id} 
                                 AND day = {trainer_day}
                                 AND start_time = {trainer_time} """)
        else:
            print("Sorry not available please choose another day...")
            self.schedule_trainer(self)
        self.schedule_ui()   
    
    def schedule_group(self):
        availabilities =self.db.execute("""SELECT c.class_name, c.instructor, c.quantity, c.isFull, a.Day, a.start_time, a.end_time
                        FROM classes AS c
                        JOIN availabilities AS a ON c.class_id = a.trainer_id;""")
        print(availabilities)
        class_name = input("Please select the class name that you want: ")
        class_id = self.db.execute(f"""SELECT class_id FROM classes WHERE class_name = {class_name}""")
        available = self.db.execute(f"""SELECT isFull
                                    FROM classes
                                    WHERE class_id = {class_id}""")
        class_capacity = self.db.execute(f"SELECT capacity FROM classes WHERE class_name = {class_name}")
        class_quantity = self.db.execute(f"SELECT quantity FROM classes WHERE class_name = {class_name}")
        if(available):
                if(class_capacity < class_quantity):
                    print("You've successfully joined the class!")
                    self.db.execute(f""" UPDATE classes
                                         SET quantity = quantity + 1
                                         WHERE class_id = {class_id};
                                         """)  
                elif(class_capacity == class_quantity + 1):
                        self.db.execute(f""" UPDATE classes
                                         SET quantity = quantity + 1
                                         WHERE class_id = {class_id};
                                         """)                      
                        self.db.execute(f""" UPDATE classes 
                                        SET isFull = TRUE 
                                        WHERE class_id = {class_id}
                                        AND """)
                        print("You've successfully joined the class and it is now full!") 
        else:
            print("Sorry not available please choose another class...")
            self.schedule_group(self) 
        self.schedule_ui() 
          

    def display_exercise(self):
        self.db.execute("SELECT * FROM exercise_routines;")
        result = self.db.fetchall()

        print("EXERCISE ROUTINES ------- ")
        #print exercises
        for exercise in result:
            for attribute in exercise:
                print(attribute, end=" ")
            print("")
        print("Returning to Main Menu")
        print("")
        self.dashboard_ui()

    def display_fitness(self):
        self.db.execute("SELECT * FROM fitness_achievement;")
        result = self.db.fetchall()

        #print fitness achievements
        print("FITNESS ACHIEVEMENTS ------- ")
        for achievement in result:
            for attribute in achievement:
                print(attribute, end=" ")
            print("")
        print("Returning to Main Menu")
        print("")
        self.dashboard_ui()
        
        
    
    def display_health(self):
        self.db.execute("SELECT * FROM health_statistics;")
        result = self.db.fetchall()

        #print health statistics
        print("HEALTH STATISTICS ------- ")
        for stat in result:
            for attribute in stat:
                print(attribute, end=" ")
            print("")
        print("Returning to Main Menu")
        print("")
        self.dashboard_ui()
        

    def update_health(self):
        name = input("(A)verage BPM, (M)uscle mass, (W)eight, (B)MI: ")          
        if name.upper() == "A" or "AVERAGE" or "BPM":
            new_bpm = input("Please enter your new average bpm: ")
            self.change_health(self, new_bpm, 0)
        elif name.upper() == "M" or "MUSCLE" or "MUSCLE MASS":
            new_muscle = input("Please enter your new muscle mass: ")
            self.change_health(self, new_muscle, 1)
        elif name.upper() == "W" or "WEIGHT":
            new_weight = input("Please input new weight: ")
            self.change_health(self, new_weight, 2)
        elif name.upper() == "B" or "BMI":
            new_bmi = input("Please input new BMI: ")
            self.change_health(self, new_bmi, 3)
        else:
            print("Unknown command, please try again...")
            self.update_personal(self)
        self.profile_ui()


    def update_personal(self):
        name = input("(F)irst Name, (L)ast Name, (E)mail, (G)oals: ")
        if name.upper() == "F" or "FIRST NAME" or "FIRST":
            new_name = input("Please enter your new first name: ")
            self.change_name(self, new_name, 0)
        elif name.upper() == "L" or "LAST NAME" or "LAST":
            new_name = input("Please enter your new last name: ")
            self.change_name(self, new_name, 1)
        elif name.upper() == "E" or "EMAIL":
            new_email = input("Please input new email: ")
            self.change_name(self, new_email, 2)
        else:
            print("Unknown command, please try again...")
            self.update_personal(self)
        self.profile_ui()
            
            

    def update_goal(self):
        new_goals = input("Please select from the following goals, (W)eight, (T)ime, (S)treak: ")
        if new_goals.upper == "W" or "WEIGHT":
            new_goalWeight = input("Please select weight goal: ")
            self.change_goal(self, new_goalWeight, 0)
        elif new_goals.upper == "T" or "TIME":
            new_goalTime = input("Please select time goal: ")
            self.change_goal(self, new_goalTime, 1)
        elif new_goals.upper == "S" or "STREAK":
            new_goalStreak = input("Please input your new streak!: ")
            self.change_goal(self, new_goalStreak, 2)
        else:
            print("Unknown command, please try again...")
            self.update_goal(self)
        self.profile_ui()
            

    def change_health(self, new_health, option):
        if option == 0:
            self.db.execute(f"""UPDATE health as h
                                SET average_bpm = {new_health}
                                FROM members as m
                                WHERE h.member_id = m.member_id AND m.member_id = {self.ID}""")
        elif option == 1:
            self.db.execute(f"""UPDATE health as h
                                SET muscle_mass = {new_health}
                                FROM members as m
                                WHERE h.member_id = m.member_id AND m.member_id = {self.ID}""")
        elif option == 2:
            self.db.execute(f"""UPDATE health as h
                                SET weight = {new_health}
                                FROM members as m
                                WHERE h.member_id = m.member_id AND m.member_id = {self.ID}""")       
        elif option == 3:
            self.db.execute(f"""UPDATE health as h
                                SET bmi = {new_health}
                                FROM members as m
                                WHERE h.member_id = m.member_id AND m.member_id = {self.ID}""")

    def change_name(self, new_name, first_or_last_or_email):
        if first_or_last_or_email == 0:
            self.db.execute(f"UPDATE members SET fName = {new_name} WHERE EMAIL = {self.EMAIL}")
            self.fName = new_name
        elif first_or_last_or_email == 1:
            self.db.execute(f"UPDATE members SET lName = {new_name} WHERE EMAIL = {self.EMAIL}")
            self.lName = new_name
        else:
            self.db.execute(f"""
                            DELETE FROM members WHERE email = {self.EMAIL};
                            INSERT INTO members ({self.fName}, {self.lName}, {self.EMAIL});
                            """)
            self.EMAIL = new_name
    
    def change_goal(self, new_goal, weight_time_streak):
        if weight_time_streak == 0:
            self.db.execute(f"""UPDATE goals as g
                                SET weight = {new_goal}
                                FROM members as m
                                WHERE g.member_id = m.member_id AND m.member_id = {self.ID}""")
        elif weight_time_streak == 1:
            self.db.execute(f"""UPDATE goals as g
                                SET time = {new_goal}
                                FROM members as m
                                WHERE g.member_id = m.member_id AND m.member_id = {self.ID}""")
        elif weight_time_streak == 2:
            self.db.execute(f"""UPDATE goals as g
                                SET streak = {new_goal}
                                FROM members as m
                                WHERE g.member_id = m.member_id AND m.member_id = {self.ID}""")