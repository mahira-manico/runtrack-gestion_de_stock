from database.connection import Data

class Category:
    def __init__(self):
        self.connection=Data()
        self.cursor=self.connection.cursor()

    
    def get_name(self):
       
       try:
        
        self.cursor.execute("SELECT name FROM category")
        return [row["name"] for row in self.cursor.fetchall()]

       except Exception as e:
        print(f"Error {e}")
        return []
    
   
      


