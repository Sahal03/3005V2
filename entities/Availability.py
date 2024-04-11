import psycopg2

class Availability:
    def __init__(self,id,day,start,end,cur):
        self.trainer_id = id
        self.day = day
        self.start = start
        self.end = end
        self.cursor = cur
        self.cursor.execute("INSERT INTO availabilities (trainer_id, day, start_time,end_time) VALUES (%s, %s, %s, %s);", (id,day,start,end))

    def isAvailable(self,day,start,end):
        if day!=self.day:
            return False
        if start>=self.start and end<=self.end:
            return True
        return False