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
            command = input("Please enter either (I)nfo, (R)ooms, (E)quipment, P(ayments), (Q)uit: ")
            command = command.upper()
        
            if (command == 'I'):
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
                    self.update_email(self,new_email)

                elif(name.upper() == "S"):
                    new_salary = input("Please enter a new salary: ")
                    self.update_salary(self,new_salary)
                
                elif(name.upper() == "P"):
                    new_pos = input("Please enter a new position: ")
                    self.update_position(self,new_pos) 
                    
            elif (command == 'R'):
                print("Please select what room you'd like to book: ")
                roomnum = input()
                self.roombook(roomnum)
            
            elif(command == 'E'):
                e_id = input("Please enter equipment ID: ")
                self.equipment_check(e_id)
                
            elif(command == 'P'):
                self.billing()
            
            elif(command == 'Q'):
                break

        
    def change_name(self,new_name,F_or_L):
        if(F_or_L == True):
            try:
                self.cur.execute("""
                UPDATE admins SET first_name = %s
                WHERE admin_id = %s 
                """, (new_name,self.ID))
                print("First name successfully updated to " + new_name)            
            except Exception as e:
                print("Failed to update first name! : " + e)

        else:
            try:
                self.cur.execute("""
                UPDATE admins SET last_name = %s 
                WHERE admin_id = %s
                """, (new_name,self.ID))
                print("Last name successfully updated to " + new_name)            
            except Exception:
                print("Failed to update last name!")
    

    def update_email(self,new_email):
        try:
            self.cur.execute("""UPDATE admins SET email = %s 
                             WHERE admin_id = %s
                                """,(new_email,self.ID))
            print("Email successfully updated to " + new_email)  
        
        except Exception:
            print("Failed to update email!") 
    
    def update_salary(self,new_salary):
        try: 
            self.cur.execute("""UPDATE Admin SET salary = %s 
                            WHERE admin_id = %s
                            """,(new_salary, self.ID))
            print("Salary successfully updated to " + new_salary)

        except Exception: 
            print("Failed to update salary!")  

    def update_position(self,new_position):
        try:
            self.cur.execute("""UPDATE admins SET position = %s 
                             WHERE admin_id = %s
                            """,(new_position,self.ID))
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
                                
                # self.cur.execute("""
                #     UPDATE rooms
                #     SET admin_id = %s
                #     WHERE room_number = %s
                #     """,(self.ID,roomnumber))
                
                
                print("Room " + roomnumber + " has been succesfully booked!") 

            except Exception:
                print("Failed to book room!")
    
    def equipment_check(self,equipment_id):
        self.cur.execute("""SELECT status FROM Equipment WHERE equipment_id = %s """, (equipment_id))
        status = self.cur.fetchone()

        if status != (False,) : 
            print("Equipment functional")
        else:
            print("Equipment under maintenance")
            

    def billing(self):
        while True:
            print("Payment Processing")
            form = input("Please enter either (D)ebit or (C)redit: ")
            
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
        

        

        
                       