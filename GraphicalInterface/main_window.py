import customtkinter as ctk
from src.Product import Product

class GlitterApp(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.products=Product()
        
        self.title("GlitterGestion App")
        self.geometry("1200x800")
        self.minsize(800,600)

        self.grid_rowconfigure(2, weight=1)  
        self.grid_columnconfigure(0, weight=1)
        
        self.dashboard_frame=Dashboard(master=self)
        self.dashboard_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=20)
        self.dashboard_frame.grid_columnconfigure(0, weight=1)
        
        self.stats_frame=Stats(master=self)
        self.stats_frame.grid(row=0, column=0, sticky="ew", padx=20,pady=20)

class Stats(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)


class Dashboard(ctk.CTkFrame):

    def __init__(self,master):
        super().__init__(master)
    
        self.products=master.products
        self.action_bar=ctk.CTkFrame(self, fg_color="transparent")
        self.action_bar.grid(row=1, column=0, sticky="ew", pady=10)

        self.search_entry=ctk.CTkEntry(self.action_bar, placeholder_text="Search a product (Dior, Fenty...)", width=400)
        self.search_entry.pack(side="left", padx=10)
        self.entry_button=ctk.CTkButton(self.action_bar, text="Search",command=self.search)
        self.entry_button.pack(side="left")

        self.add_button = ctk.CTkButton(self.action_bar, text="+ Add Product", fg_color="#E91E63", command=self.add_window)
        self.add_button.pack(side="right", padx=10)

        self.scrollable_list = ctk.CTkScrollableFrame(self, label_text="Live Inventory")
        self.scrollable_list.grid(row=2, column=0, sticky="nsew", padx=20, pady=20)

        self.delete_button=ctk.CTkButton(self.action_bar, text="- Delete a Product", command=self.delete_window)
        self.delete_button.pack(side="right",padx=20)

        self.update_button=ctk.CTkButton(self.action_bar, text="Update", command=self.update_pr)
        self.update_button.pack(side="right",padx=20)

        self.refresh_products()

    def search(self):
        letter=self.search_entry.get()
        result=self.products.get_product(letter)
        
        if not letter:
            return
        
        if result is not None:
            self.refresh_products(products=result)
    
    def update_pr(self):
        UpdateProduct(master=self, refresh_product=self.refresh_products)

    def add_window(self):
        AddProduct(master=self, refresh_product=self.refresh_products)

    def delete_window(self):
        DeleteProduct(master=self, refresh_product=self.refresh_products)

    def refresh_products(self,products=None):

        for infos in self.scrollable_list.winfo_children():
         infos.destroy()
        
        if products is None:
         products=self.products.get_all()
         
        if products:
         for i in products:
             row=ctk.CTkFrame(self.scrollable_list)
             row.pack(fill="x", expand=True,pady=5,padx=10)
 
             ctk.CTkLabel(row, text=i["id"],width=200).pack(side="left",pady=20)
             ctk.CTkLabel(row, text=i["name"],width=200).pack(side="left",pady=20)
             ctk.CTkLabel(row,text=i["description"],width=100).pack(side="left")
             ctk.CTkLabel(row,text=f"{i['price']}$",width=100).pack(side="right")
             ctk.CTkLabel(row,text=f"Stock: {i['quantity']}",width=100).pack(side="left")

class UpdateProduct(ctk.CTkToplevel):
    def __init__(self, master, refresh_product):
        super().__init__(master)
        self.title("Update a Product Here!")
        self.geometry("400x500")
        self.refresh=refresh_product
        self.products=master.products

        ctk.CTkLabel(self, text="Choose a column to modify: ").pack(pady=(20,5))
        self.column_entry=ctk.CTkOptionMenu(self, values=["name","description","price","quantity"])
        self.column_entry.pack()
        
        self.id_entry=ctk.CTkEntry(self, placeholder_text="Take the ID of the product to modify",width=200)
        self.id_entry.pack(pady=10)

        self.change_entry=ctk.CTkEntry(self, placeholder_text="Type your entry")
        self.change_entry.pack(pady=20)

        self.save_button=ctk.CTkButton(self, text="Save", command=self.update_product)
        self.save_button.pack(pady=20)

    def update_product(self):
        column=self.column_entry.get()
        new_value=self.change_entry.get()
        id=int(self.id_entry.get())

        if not column or not new_value or not id:
            return 
        
        result=self.products.update(column,new_value,id)

        if result:
            print(result)
            self.refresh()
            self.destroy()
        
        else:
            ctk.CTkLabel(self, text="ID not Found or Error",text_color="red").pack()

class DeleteProduct(ctk.CTkToplevel):
    def __init__(self, master, refresh_product):
        super().__init__(master)
        self.title("Delete a Product Here!")
        self.geometry("400x300")
        self.refresh=refresh_product
        self.products=master.products

        ctk.CTkLabel(self, text="Delete a Product").pack(pady=20)

        self.id_entry=ctk.CTkEntry(self, placeholder_text="Enter Product ID",width=300)
        self.id_entry.pack(pady=10)

        self.save_button=ctk.CTkButton(self, text="Save to Database", command=self.delete_product)
        self.save_button.pack(pady=20)
        
    def delete_product(self):

        id=self.id_entry.get()

        if not id:
            return

        entry=self.products.delete(int(id))

        if entry:
            ctk.CTkLabel(self,text="Product succesfully deleted!",text_color="green").pack()
            self.refresh()
            self.destroy()
        
        else:
            ctk.CTkLabel(self, text="ID not found or Error",text_color="red").pack()

class AddProduct(ctk.CTkToplevel):
        def __init__(self, master,refresh_product):
            super().__init__(master)
            self.title("Add new Products to GlitterApp!")
            self.geometry("400x500")
            self.refresh=refresh_product
            self.products=master.products
        
            ctk.CTkLabel(self,text="Add a new product").pack(pady=20)

            self.name_entry=ctk.CTkEntry(self,placeholder_text="Enter a name", width=300)
            self.name_entry.pack(pady=10)

            self.description_entry=ctk.CTkEntry(self,placeholder_text="Enter a description",width=300)  
            self.description_entry.pack(pady=10)
            
            self.price_entry=ctk.CTkEntry(self, placeholder_text="Enter a price", width=300)
            self.price_entry.pack(pady=10)

            self.quantity_entry=ctk.CTkEntry(self, placeholder_text="Enter a quantity", width=300)
            self.quantity_entry.pack(pady=10)

            self.category_entry=ctk.CTkEntry(self, placeholder_text="Enter an ID category", width=300)
            self.category_entry.pack(pady=10)

            self.save_button=ctk.CTkButton(self, text="Save to Database", command=self.sumbit_data)
            self.save_button.pack(pady=30)

        def sumbit_data(self):
            name=self.name_entry.get()
            description=self.description_entry.get()
            price=self.price_entry.get()
            quantity=self.quantity_entry.get()
            category=self.category_entry.get()

            if not name or not description or not price or not quantity or not category:
                return
            
            entries=self.products.add(name, description, int(price),int(quantity), int(category))

            if entries:
                ctk.CTkLabel(self, text=f"{name} added to inventory!", text_color="green").pack
                self.refresh()
                self.destroy()
            
            else:
                ctk.CTkLabel(self, text="Synthax Error or Error", text_color="red").pack()

    
