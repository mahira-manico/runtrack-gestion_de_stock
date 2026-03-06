import mysql.connector
from mysql.connector import Error


class Data:
    def __init__(self):

      try:
        self.mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Banane1001#",
            database="store"
        )
        if self.mydb.is_connected():           
         return True
      except Exception as e:
         print(f"Error while connecting: {e}")
         return False
    
    def cursor(self):
       if self.mydb and self.my.is_connected():
          return self.mydb.cursor(dictionnary=True)
       else:
          return None
        
    
    def commit(self):
     if self.mydb and self.mydb.is_connected():
       self.mydb.commit()
     else:
        return None
    
    def disconnect_cursor(self,cursor):
        if self.mydb and self.mydb.is_connected():
           if cursor:
            cursor.close()
    
    def disconnect(self):
        if self.mydb and self.mydb.is_connected():
         self.mydb.close()
 
    
    

