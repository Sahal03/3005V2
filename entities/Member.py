import psycopg2 as ps

class Member:
    def __init__(self, fName, lName, EMAIL, db, register):
        if register == False:
            db.execute("SELECT first_name FROM members WHERE email = %s", (EMAIL,))
            self.fName = db.fetchone()[0]
            db.execute("SELECT last_name FROM members WHERE email = %s;", (EMAIL,))
            self.lName = db.fetchone()[0]
            self.EMAIL = EMAIL
            self.db = db
            db.execute("SELECT member_id FROM members WHERE email = %s;", (EMAIL,))
            self.ID = db.fetchone()[0]
            db.execute("""SELECT g.weight
                                            FROM goals AS g
                                            INNER JOIN members AS m ON g.member_id = m.member_id
                                            WHERE m.member_id = %s;""", (self.ID,))
            self.goalWeight = db.fetchone()[0]
            db.execute("""SELECT g.time
                                            FROM goals AS g
                                            INNER JOIN members AS m ON g.member_id = m.member_id
                                            WHERE m.member_id = %s;""", (self.ID,))
            self.goalTime = db.fetchone()[0]
            db.execute("""SELECT g.streak
                                            FROM goals AS g
                                            INNER JOIN members AS m ON g.member_id = m.member_id
                                            WHERE m.member_id = %s;""", (self.ID,))
            self.goalStreak = db.fetchone()[0]
            
            db.execute("""SELECT h.average_bpm
                                            FROM health as h
                                            INNER JOIN members as m on h.member_id = m.member_id
                                            WHERE m.member_id = %s;""", (self.ID,))
            self.average_bpm = db.fetchone()[0]
            db.execute("""SELECT h.muscle_mass
                                        FROM health as h
                                        INNER JOIN members as m on h.member_id = m.member_id
                                        WHERE m.member_id = %s;""", (self.ID,))
            self.muscle = db.fetchone()[0]
            db.execute("""SELECT h.weight
                                        FROM health as h
                                        INNER JOIN members as m on h.member_id = m.member_id
                                        WHERE m.member_id = %s;""", (self.ID,))
            self.weight = db.fetchone()[0]
            db.execute("""SELECT h.bmi
                                    FROM health as h
                                    INNER JOIN members as m on h.member_id = m.member_id
                                    WHERE m.member_id = %s;""", (self.ID,))
            self.bmi = db.fetchone()[0]

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
            self.db = db

            db.execute("INSERT INTO members (fName, lName, email) VALUES (%s, %s, %s)", (fName, lName, EMAIL))
            self.ID = db.fetchone()[0]
            db.execute("INSERT INTO goals (member_id, weight, time, streak) VALUES (%s,%s,%s,%s)", (self.ID, self.goalWeight, self.goalTime, self.goalStreak))
            db.execute("INSERT INTO health (member_id, average_bpm, muscle_mass, weight, bmi) VALUES (%s,%s,%s,%s,%s)", (self.ID, self.average_bpm, self.muscle, self.weight, self.bmi))
            
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
        if command.upper() == "E":
            print("Please look at the following routines! \n")
            self.display_exercise()
        elif command.upper() == "F":
            print("Please look at what the different achievements! \n")
            self.display_fitness()
        elif command.upper() == "H":
            print("Please look at the following health statistics! \n")
            self.display_health()
        elif command.upper() == "M":
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
        if command.upper() == "U":
            print("Please Select what info you'd like to update from the following:")
            self.update_personal()
        elif command.upper() == "F":
            print("Please select what goals you'd like to update from the following:")
            self.update_goal()
        elif command.upper() == "H":
            print("Please select what health metrics you'd like to update from the following:")
            self.update_health()
        elif command.upper() == "M":
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
        if command.upper() == "T":
            print("Please select a suitable time: ")
            self.schedule_trainer()
        elif command.upper() == "G":
            print("Please select a group session")
            self.schedule_group()
        elif command.upper() == "M":
            self.ui()
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
        self.db.execute("""SELECT t.first_name, t.last_name, a.Day, a.start_time, a.end_time
                        FROM trainers AS t
                        JOIN availabilities AS a ON t.trainer_id = a.trainer_id;""")
        availabilities = self.db.fetchall()
        print(availabilities)
        trainer_name = input("Please select the trainer name that you want: ")
        self.db.execute("SELECT trainer_id FROM trainers WHERE first_name = %s", (trainer_name,))
        trainer_id = self.db.fetchone()
        trainer_day = input("Please input the day using the format YEAR-MONTH-DAY: ")
        trainer_time = input("Please input the starting hour using the format XX:XX:XX : ")
        self.db.execute("""SELECT available
                                    FROM availabilities
                                    WHERE trainer_id = %s""", (trainer_id,))
        available = self.db.fetchone()
        if available:
            self.db.execute("""UPDATE availabilities 
                                SET available = FALSE 
                                WHERE trainer_id = %s 
                                AND day = %s
                                AND start_time = %s""", (trainer_id, trainer_day, trainer_time))
            print("You've Scheduled the class!")
        else:
            print("Sorry not available please choose another day...")
            self.schedule_trainer()
        self.schedule_ui()   

    def schedule_group(self):
        self.db.execute("""SELECT class_name, instructor, quantity, isFull
                        FROM classes""")
        availabilities = self.db.fetchall()
        print(availabilities)
        class_name = input("Please select the class name that you want: ")
        self.db.execute("SELECT class_id FROM classes WHERE class_name = %s", (class_name,))
        class_id = self.db.fetchone()[0]
        self.db.execute("SELECT isFull FROM classes WHERE class_id = %s", (class_id,))
        isFull = self.db.fetchone()[0]
        self.db.execute("SELECT capacity FROM classes WHERE class_name = %s", (class_name,))
        class_capacity = int(self.db.fetchone()[0])
        self.db.execute("SELECT quantity FROM classes WHERE class_name = %s", (class_name,))
        class_quantity = int(self.db.fetchone()[0])
        if isFull == False:
            if class_quantity < class_capacity:
                self.db.execute("""UPDATE classes
                                    SET quantity = quantity + 1
                                    WHERE class_id = %s""", (class_id,))
                print("You've successfully joined the class!!!")
            elif class_capacity == class_quantity + 1:
                self.db.execute("""UPDATE classes
                                    SET quantity = quantity + 1
                                    WHERE class_id = %s""", (class_id,))
                self.db.execute("""UPDATE classes 
                                SET isFull = TRUE 
                                WHERE class_id = %s""", (class_id,))
                print("You've successfully joined the class and it is now full!") 
            else:
                print("Sorry not available please choose another class...")
                self.schedule_group() 
        else:
            print("Sorry not available please choose another class...")
            self.schedule_group() 
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
        if name.upper() == "A" or name.upper() == "AVERAGE" or name.upper() == "BPM":
            new_bpm = input("Please enter your new average bpm: ")
            self.change_health(new_bpm, 0)
        elif name.upper() == "M" or name.upper() == "MUSCLE" or name.upper() == "MUSCLE MASS":
            new_muscle = input("Please enter your new muscle mass: ")
            self.change_health(new_muscle, 1)
        elif name.upper() == "W" or name.upper() == "WEIGHT":
            new_weight = input("Please input new weight: ")
            self.change_health(new_weight, 2)
        elif name.upper() == "B" or name.upper() == "BMI":
            new_bmi = input("Please input new BMI: ")
            self.change_health(new_bmi, 3)
        else:
            print("Unknown command, please try again...")
            self.update_personal()
            self.profile_ui()


    def update_personal(self):
        name = input("(F)irst Name, (L)ast Name, (E)mail, (G)oals: ")
        if name.upper() == "F" or name.upper() == "FIRST NAME" or name.upper() == "FIRST":
            new_name = input("Please enter your new first name: ")
            self.change_name(new_name, 0)
        elif name.upper() == "L" or name.upper() == "LAST NAME" or name.upper() == "LAST":
            new_name = input("Please enter your new last name: ")
            self.change_name(new_name, 1)
        elif name.upper() == "E" or name.upper() == "EMAIL":
            new_email = input("Please input new email: ")
            self.change_name(new_email, 2)
        else:
            print("Unknown command, please try again...")
            self.update_personal()
        self.profile_ui()

    def update_goal(self):
        new_goals = input("Please select from the following goals, (W)eight, (T)ime, (S)treak: ")
        if new_goals.upper() == "W" or new_goals.upper() == "WEIGHT":
            new_goalWeight = input("Please select weight goal: ")
            self.change_goal(new_goalWeight, 0)
        elif new_goals.upper() == "T" or new_goals.upper() == "TIME":
            new_goalTime = input("Please select time goal: ")
            self.change_goal(new_goalTime, 1)
        elif new_goals.upper() == "S" or new_goals.upper() == "STREAK":
            new_goalStreak = input("Please input your new streak!: ")
            self.change_goal(new_goalStreak, 2)
        else:
            print("Unknown command, please try again...")
            self.update_goal()
        self.profile_ui()

    def change_health(self, new_health, option):
        if option == 0:
            self.db.execute("""UPDATE health as h
                                SET average_bpm = %s
                                FROM members as m
                                WHERE h.member_id = m.member_id AND m.member_id = %s""", (new_health, self.ID))
        elif option == 1:
            self.db.execute("""UPDATE health as h
                                SET muscle_mass = %s
                                FROM members as m
                                WHERE h.member_id = m.member_id AND m.member_id = %s""", (new_health, self.ID))
        elif option == 2:
            self.db.execute("""UPDATE health as h
                                SET weight = %s
                                FROM members as m
                                WHERE h.member_id = m.member_id AND m.member_id = %s""", (new_health, self.ID))       
        elif option == 3:
            self.db.execute("""UPDATE health as h
                                SET bmi = %s
                                FROM members as m
                                WHERE h.member_id = m.member_id AND m.member_id = %s""", (new_health, self.ID))

    def change_name(self, new_name, first_or_last_or_email):
        if first_or_last_or_email == 0:
            self.db.execute("UPDATE members SET first_name = %s WHERE EMAIL = %s", (new_name, self.EMAIL))
            self.fName = new_name
        elif first_or_last_or_email == 1:
            self.db.execute("UPDATE members SET last_name = %s WHERE EMAIL = %s", (new_name, self.EMAIL))
            self.lName = new_name
        else:
            self.db.execute("""
                            DELETE FROM members WHERE email = %s;
                            INSERT INTO members (first_name, last_name, email) VALUES (%s, %s, %s);
                            """, (self.EMAIL, self.fName, self.lName, new_name))
            self.EMAIL = new_name

    def change_goal(self, new_goal, weight_time_streak):
        if weight_time_streak == 0:
            self.db.execute("""UPDATE goals as g
                                SET weight = %s
                                FROM members as m
                                WHERE g.member_id = m.member_id AND m.member_id = %s""", (new_goal, self.ID))
        elif weight_time_streak == 1:
            self.db.execute("""UPDATE goals as g
                                SET time = %s
                                FROM members as m
                                WHERE g.member_id = m.member_id AND m.member_id = %s""", (new_goal, self.ID))
        elif weight_time_streak == 2:
            self.db.execute("""UPDATE goals as g
                                SET streak = %s
                                FROM members as m
                                WHERE g.member_id = m.member_id AND m.member_id = %s""", (new_goal, self.ID))