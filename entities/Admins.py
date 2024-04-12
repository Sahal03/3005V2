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
        print("Welcome Admin() " + self.First_Name + ":")
        command = input("Please enter I for INFO: ")
        if command is "I" or "INFO":
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
            self.cur.execute("""UPDATE Admin SET email = %s """, (new_email))
            print("Email successfully updated to " + new_email)  
        
        except Exception:
            print("Failed to update email!") 
    
    def update_salary(self,new_salary):
        try: 
            self.cur.execute("""UPDATE Admin SET salary = %s """, (new_salary))
            print("Salary successfully updated to " + new_salary)

        except Exception: 
            print("Failed to update salary!")  

    def update_position(self,new_position):
        try:
            self.cur.execute("""UPDATE Admin SET position = %s """, (new_position))
            print("Position successfully updated to " + new_position)

        except Exception: 
            print("Failed to update position")  



    def roombook(self, roomnumber):
        if self.cur.execute("""SELECT status FROM rooms WHERE room_number = %s""", (roomnumber)) is not None : 
            print("Room booked")
        else:
            try:
                self.cur.execute("""
                    UPDATE rooms 
                    SET status = %s
                    WHERE room_number = %s 
                    """, ('True',roomnumber))
                
                self.cur.execute("""
                    UPDATE rooms
                    SET admin_id = %s
                    WHERE room_number = %s
                    """,(self.ID,roomnumber))
                print("Room " + roomnumber + "has been succesfully booked!") 

            except Exception:
                print("Failed to book room!")
    
    def equipment_check(self,equipment_id):
        if self.cur.execute("""SELECT status FROM Equipment WHERE equipment_id = %s""", (equipment_id)) is not None : 
            print("Equipment functional")
        else:
            print("Equipment under maintenance")
            
    # def class_update():
            



        

        
                       