from database import Data

class Category:
    def __init__(self):
        self.connection=Data()
        self.cursor=self.connection.cursor()

    
    def get_all(self):
       
       try:
        
        self.cursor.execute("SELECT * FROM category")
        result=self.cursor.fetchall()

       except Exception as e:
        print(f"Error {e}")
        return False
       
       finally:
        self.connection.disconnect_cursor()
        return result
    
    def add(self, name):

        try:
         request="INSERT INTO category (name) VALUES=(%s)"
         value=(name,)
         self.cursor.execute(request,value)
         self.connection.commit()
         return True
        
        except Exception as e:
         print(f"Error: {e}")
         return False
        
        finally:
         self.connection.disconnect_cursor()
    
    def update(self, column,id, new_value):

        try:
         if column not in ["name"]:
            return False
         
         request=f"UPDATE category SET {column}=%s WHERE id=%s"
         values=new_value,id
         self.cursor.execute(request,values)
         self.connection.commit()
         return True
        
        except Exception as e:
         print(f"Error: {e}")
         return False
        
        finally:
         self.connection.disconnect_cursor()
    
    def delete(self,id):
       
       try:
        request="DELETE FROM category WHERE id=%s"
        value=(id,)
        self.cursor.execute(request,value)
        self.connection.commit()
        return True

       except Exception as e:
        print(f"Error {e}")
        return False
       
       finally:
        self.connection.disconnect_cursor()




        

      


