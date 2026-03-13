from database.connection import Data

class Product:
    def __init__(self):

        self.connection=Data()
        self.cursor=self.connection.cursor()

    def get_all(self):
        
        try:
            self.cursor.execute("SELECT * FROM product")
            result=self.cursor.fetchall()
            return result

        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def get_product(self,letter):

        try:
            request="SELECT * FROM product WHERE name LIKE %s"
            value=(f"%{letter}%",)
            self.cursor.execute(request, value)
            result=self.cursor.fetchall()
            return result
        
        except Exception as e:
            print(f"Error: {e}")
            return None
    
        
    def add(self, name, description, price, quantity, id_category):
        
        try:
            request="INSERT INTO product (name, description, price, quantity, id_category) VALUES=(%s,%s,%s,%s,%s)"
            values=(name, description, price, quantity, id_category)
            self.cursor.execute(request, values)
            self.connection.commit()
            return True
        
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    
    def update(self, column, new_value, id):
        
        try:    
            request=f"UPDATE product SET {column}=%s WHERE id=%s"
            values=(new_value, id)
            self.cursor.execute(request, values)
            self.connection.commit()
            return True
        
        except Exception as e:
            print(f"Error: {e}")
            return False
     
    def delete(self, id):
        
        try:
            request="DELETE FROM product WHERE id=%s"
            value=(id,)
            self.cursor.execute(request, value)
            self.connection.commit()
            return True
        
        except Exception as e:
            print(f"Error: {e}")
            return False
   



