import psycopg2 as psy

class Admins:
    def __init__(self,ID,EMAIL,Salary,Position,last_Name,first_Name,Database):
        
        if ID == None:
            self.cur.execute("INSERT INTO admins (email, salary, position, last_Name, first_Name) VALUES (%s, %s, %s, %s, %s)", (EMAIL, Salary, Position, last_Name, first_Name))
            self.ID = self.cursor.execute("SELECT admin_id FROM admins ORDER BY admin_id DESC LIMIT 1;")
        else:
            self.ID=ID
            
        self.EMAIL = EMAIL
        self.Salary = Salary
        self.Position = Position
        self.Last_Name = last_Name
        self.First_Name = first_Name
        
        self.cur = Database
        
    def profile(self):
        while True:
            print("Welcome Admin() " + self.First_Name + ":")
            command = input("Please enter either (U)pdate, (R)ooms, (E)quipment, P(ayments), (V)iew, (C)lasses, (Q)uit: ")
            command = command.upper()
        
            if (command == 'U'):
                print("Please select what info you'd like to update from the following: ")
                name = input("(F)irst Name, (L)ast Name, (E)mail, (S)alary, (P)osition: ")
                if (name.upper() == "F"):
                    new_first = input("Please enter new First Name: ")
                    self.change_name(new_first,True)
                
                elif(name.upper() == "L"):
                    new_last = input("Please enter new Last Name: ")
                    self.change_name(new_last,False)

                elif(name.upper() == "E"):
                    new_email = input("Please enter a new email: ")
                    self.update_email(new_email)

                elif(name.upper() == "S"):
                    new_salary = input("Please enter a new salary: ")
                    self.update_salary(new_salary)
                
                elif(name.upper() == "P"):
                    new_pos = input("Please enter a new position: ")
                    self.update_position(new_pos) 
                    
            elif (command == 'R'):
                self.cur.execute("""SELECT * 
                             FROM rooms""")
            
                rooms_view = self.cur.fetchall()

                for rooms in rooms_view:
                    print(rooms)
            
                print("Please select what room you'd like to book: ")
                roomnum = input()
                self.roombook(roomnum)
            
            elif(command == 'E'):
                self.cur.execute("""
                        SELECT * FROM equipments
                        """)
                
                equipments = self.cur.fetchall()
                for e in equipments:
                    print("ID: " + str(e[0]) + ", Name: " + e[1])
                e_id = input("Please enter equipment ID to check funtionality: ")
                self.equipment_check(e_id)
                
            elif(command == 'P'):
                self.billing()
            
            elif(command == 'V'):
                self.view_info()
            
            elif(command == 'C'):
                self.class_schedules()
            
            elif(command == 'Q'):
                break
            
    
    def class_schedules(self):
        check = input("Would you like to (V)iew, (E)dit, (C)reate, (D)elete classes?: ")
        check = check.upper()
        if check == 'V':
            self.class_view()
        elif check == 'E':
            self.class_updater()
        elif check == 'C':
            name = input("Please enter instructor name: ")
            quantity = 0
            capacity = input("Please enter max capacity: ")
            class_name = input("Please enter class name: ")
            isFull = False
            try: 
                self.cur.execute("INSERT INTO classes (instructor, quantity, capacity, class_name, isFull) VALUES (%s, %s, %s, %s, %s)", (name, quantity, capacity, class_name, isFull))
                print("Class successfully created!")
            except Exception: 
                print("Error! Failed to create class!")
        
        elif check == 'D':
            class_id = input("Enter the class id that you'd like to delete: ")
            
            try:
                self.cur.execute("""DELETE FROM classes WHERE class_id = %s""",(class_id,))
                print("Class successfully deleted!")
            except Exception:
                print("Failed to delete class!")                

    def class_view(self):
        self.cur.execute("""SELECT * 
                            FROM classes""")
        
        classes_view = self.cur.fetchall()
        
        for classes in classes_view:
            print(classes)
        
    def class_updater(self):
        self.class_view()

        id = input("Enter the id of the class you wish to update: ")
        print("1. Change instructor")
        print("2. Update Class Quantity")
        print("3. Update Class Capacity")
        print("4. Update Class Name")
        selection = input("Edit Selection: ")

        if selection == '1':
            newInstructor = input("Input New Instructor: ")
            self.cur.execute("UPDATE classes SET instructor=%s WHERE class_id=%s",(newInstructor,int(id)))
        elif selection == '2':
            newQuantity = input("Input New Quantity: ")
            self.cur.execute("SELECT capacity FROM classes WHERE class_id=%s",(int(id),))
            capacity = self.cur.fetchone()[0]
            if int(newQuantity) > capacity or int(newQuantity) < 0:
                print("Invalid quantity entered... try again")
                self.class_updater()
            else:
                self.cur.execute("UPDATE classes SET quantity=%s WHERE class_id=%s",(int(newQuantity),int(id)))
                if(int(newQuantity) == capacity):
                    self.cur.execute("UPDATE classes SET isFull=TRUE WHERE class_id=%s",(int(id),))
                else:
                    self.cur.execute("SELECT isFull FROM classes WHERE class_id=%s",(int(id),))
                    isFull = self.cur.fetchone()[0]
                    if isFull == True:
                        self.cur.execute("UPDATE classes SET isFull=FALSE WHERE class_id=%s",(int(id),))
        elif selection == '3':
            newCapacity = input("Input New Capacity: ")
            self.cur.execute("SELECT quantity FROM classes WHERE class_id=%s",(int(id),))
            quantity = self.cur.fetchone()[0]

            if int(newCapacity) < quantity:
                print("Please enter new quantity and try again")
                self.class_updater()
            else:
               self.cur.execute("UPDATE classes SET capacity=%s WHERE class_id=%s",(int(newCapacity),int(id)))
               if int(newCapacity) == quantity:
                   self.cur.execute("UPDATE classes SET isFull=TRUE WHERE class_id=%s",(int(id),))
               else:
                    self.cur.execute("SELECT isFull FROM classes WHERE class_id=%s",(int(id),))
                    isFull = self.cur.fetchone()[0]
                    if isFull == True:
                        self.cur.execute("UPDATE classes SET isFull=FALSE WHERE class_id=%s",(int(id),))
        elif selection == '4':
            newName = input("Input New Class Name: ")
            self.cur.execute("UPDATE classes SET class_name=%s WHERE class_id=%s",(newName,int(id)))
        else:
            print("Invalid input. Please enter either 1,2,3 or 4 when shown edit menu.")
            self.class_updater()
        
        
        
    def view_info(self):
        print("What infomation would you like to view?")
        type = input("(M)ember, (T)rainer, (A)dmin: ")
        type = type.upper()
        
        if type == 'A':
            view = input("(F)irst Name, (L)ast Name, (E)mail, (S)alary, (P)osition, (A)ll: ")
            view = view.upper()
            
            if view == 'F':
                self.cur.execute("""
                            SELECT first_name FROM admins WHERE admin_id = %s
                            """, (self.ID,))
                status = self.cur.fetchone()
                print("First name: " + status[0])
        
            elif view == 'L':
                self.cur.execute("""
                            SELECT last_name FROM admins WHERE admin_id = %s
                            """, (self.ID,))
                status = self.cur.fetchone()
                print("Last name: " + status[0])
        
            elif view == 'E':
                self.cur.execute("""
                            SELECT email FROM admins WHERE admin_id = %s
                            """, (self.ID,))
                status = self.cur.fetchone()
                print("Email: " + status[0])
        
            elif view == 'S':
                self.cur.execute("""
                            SELECT salary FROM admins WHERE admin_id = %s
                            """, (self.ID,))
                status = self.cur.fetchone()
                print("Salary: " + str(status[0]))
        
            elif view == 'P':
                self.cur.execute("""
                            SELECT position FROM admins WHERE admin_id = %s
                            """, (self.ID,))
                status = self.cur.fetchone()
                print("Positon: " + status[0]) 
        
            elif view == 'A':
                self.cur.execute("""
                            SELECT * FROM admins WHERE admin_id = %s
                            """, (self.ID,))
                
                view = self.cur.fetchone()
                print(view[0])
                print(view[2])
                print("ID: " + str(view[0]) + ", Email: " + view[1] + ", Salary: " + str(view[2]) + ", Position: " + view[3] + ", Last name: " + view[4] + ", First name: " + view[5])
        
        elif type == 'M':
            self.cur.execute("""SELECT * FROM members""")
            status = self.cur.fetchall()
            
            for members in status:
                print("ID: " + str(members[0]) + ", First name: " + members[1] + ", Last name: " + members[2] + ", Email: " + members[3])
        
        elif type == 'T':
            self.cur.execute("""SELECT * FROM trainers""")
            status = self.cur.fetchall()
            
            for trainers in status:
                print("ID: " + (str(trainers[0])) + ", First name: " + trainers[1] + ", Last name: " + trainers[2] + ", Email: " + trainers[3] + ", Salary: " + str(trainers[4]))
            
            
        



    def change_name(self,new_name,F_or_L):
        if(F_or_L == True):
            try:
                self.cur.execute("""
                UPDATE admins SET first_name = %s
                WHERE admin_id = %s 
                """, (new_name,self.ID))
                self.First_Name = new_name
                print("First name successfully updated to " + new_name)            
            except Exception as e:
                print("Failed to update first name! : " + e)

        else:
            try:
                self.cur.execute("""
                UPDATE admins SET last_name = %s 
                WHERE admin_id = %s
                """, (new_name,self.ID))
                self.Last_Name = new_name
                print("Last name successfully updated to " + new_name)            
            except Exception:
                print("Failed to update last name!")
    

    def update_email(self,new_email):
        try:
            self.cur.execute("""UPDATE admins SET email = %s 
                             WHERE admin_id = %s
                                """,(new_email,self.ID))
            print("Email successfully updated to " + new_email)  
            self.EMAIL = new_email
            
        except Exception:
            print("Failed to update email!") 
    
    
    def update_salary(self,new_salary):
        try: 
            self.cur.execute("""UPDATE admins SET salary = %s 
                            WHERE admin_id = %s
                            """,(new_salary, self.ID))
            print("Salary successfully updated to " + new_salary)

            self.Salary = new_salary
        except Exception: 
            print("Failed to update salary!")  

    def update_position(self,new_position):
        try:
            self.cur.execute("""UPDATE admins SET position = %s 
                             WHERE admin_id = %s
                            """,(new_position,self.ID))
            
            self.Position = new_position
            print("Position successfully updated to " + new_position)

        except Exception: 
            print("Failed to update position")  


    def roombook(self, roomnumber):
        
        self.cur.execute("""
                        SELECT status FROM rooms WHERE room_number = %s
                        """, (roomnumber,))
        status = self.cur.fetchone()
                
        if (status != (False,)): 
            print("Room booked already. Please pick another room: ")
        else:
            try:
                self.cur.execute("""
                    UPDATE rooms 
                    SET status = %s
                    WHERE room_number = %s
                    """, (True, roomnumber))
      
                print("Room " + roomnumber + " has been succesfully booked!") 

            except Exception:
                print("Failed to book room!")
    
    
    def equipment_check(self,equipment_id):
        self.cur.execute("""SELECT status FROM equipments WHERE equipment_id = %s """, (equipment_id))
        status = self.cur.fetchone()
        if status != None:
            try:
                if status != (False,) : 
                    print("Equipment functional")
                else:
                    print("Equipment under maintenance")
            except:
                print(equipment_id + " does not exist")
        else:
                print(equipment_id + " does not exist")
            

    def billing(self):
        while True:
            print("Payment Processing")
            form = input("Please enter either (D)ebit or (C)redit: ")
            form = form.upper()
            if form == 'D':
                print("Debit selected. What plan would you like to choose")
                plan = input("Biweekly Payment(1), Monthly Payment(2), Yearly Payment(3): ")
                
                if plan == '1': 
                    print("Biweekly Selected")
                    print("Your biweekly payments will be: $25.99 | Tax included")
                    confirm = input("Confirm purchase(Y/N): ")
                    if confirm.upper() == 'Y':
                        self.reciept_print(plan)
                        break
                  
                    elif confirm.upper() == 'N': 
                        select = input("For different payment type 1, otherwise Q to quit: ")
                        if select == 1:
                            pass
                        elif select.upper() == 'Q':
                            break
                        
                elif plan == '2': 
                    print("Monthly Selected")
                    print("Your monthly payments will be: $45.99 | Tax included")
                    confirm = input("Confirm purchase(Y/N): ")
                    if confirm.upper() == 'Y':
                        self.reciept_print(plan)
                        break
                    
                    elif confirm.upper() == 'N': 
                        select = input("For different payment type 1, otherwise Q to quit: ")
                        if select == 1:
                            pass
                        elif select.upper() == 'Q':
                            break
                
                elif plan == '3':
                    print("Yearly Selected")
                    print("Your yearly payments will be: $250.99 | Tax included")
                    confirm = input("Confirm purchase(Y/N): ")
                    if confirm.upper() == 'Y':
                        self.reciept_print(plan)
                        break
                    
                    elif confirm.upper() == 'N': 
                        select = input("For different payment type 1, otherwise Q to quit: ")
                        if select == 1:
                            pass
                        elif select.upper() == 'Q':
                            break
        
            elif form == 'C':
                    print("Credit selected. What plan would you like to choose")
                    plan = input("Biweekly Payment(1), Monthly Payment(2), Yearly Payment(3): ")
                    
                    if plan == '1': 
                        print("Biweekly Selected")
                        print("Your biweekly payments will be: $25.99 | Tax included")
                        confirm = input("Confirm purchase(Y/N): ")
                        if confirm.upper() == 'Y':
                            self.reciept_print(plan)
                            break
                    
                        elif confirm.upper() == 'N': 
                            select = input("For different payment type 1, otherwise Q to quit: ")
                            if select == 1:
                                pass
                            elif select.upper() == 'Q':
                                break
                            
                    elif plan == '2': 
                        print("Monthly Selected")
                        print("Your monthly payments will be: $45.99 | Tax included")
                        confirm = input("Confirm purchase(Y/N): ")
                        if confirm.upper() == 'Y':
                            self.reciept_print(plan)
                            break
                        
                        elif confirm.upper() == 'N': 
                            select = input("For different payment type 1, otherwise Q to quit: ")
                            if select == 1:
                                pass
                            elif select.upper() == 'Q':
                                break
                    
                    elif plan == '3':
                        print("Yearly Selected")
                        print("Your yearly payments will be: $250.99 | Tax included")
                        confirm = input("Confirm purchase(Y/N): ")
                        if confirm.upper() == 'Y':
                            self.reciept_print(plan)
                            break
                        
                        elif confirm.upper() == 'N': 
                            select = input("For different payment type 1, otherwise Q to quit: ")
                            if select == 1:
                                pass
                            elif select.upper() == 'Q':
                                break
                
                
    def reciept_print(self,plan):
        
        print("")
        if plan == '1':
            print("For Admin " + self.First_Name + " " + self.Last_Name)
            print("Email: " + self.EMAIL)
            print("Your total will come out to be: $25.99")
            print("Your card will automatically be charged the same amount every two weeks.")
            print("Thank you for your purchase. Stay safe and healthy!")
            
        elif plan == '2':
            print("For Admin " + self.First_Name + " " + self.Last_Name)
            print("Email: " + self.EMAIL)
            print("Your total will come out to be: $45.99")
            print("Your card will automatically be charged the same amount in every month.")
            print("Thank you for your purchase. Stay safe and healthy!")
        
        elif plan == '3':
            print("For Admin " + self.First_Name + " " + self.Last_Name)
            print("Email: " + self.EMAIL)
            print("Your total will come out to be: $250.99")
            print("Your card will automatically be charged the same amount every year.")
            print("Thank you for your purchase. Stay safe and healthy!")
        
        print("")
        

        

        
                       