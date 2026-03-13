import customtkinter as ctk
from src.Product import Product
from src.Category import Category
from src.constant import *
import csv

class GlitterApp(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        
        ctk.set_appearance_mode("dark")
        self.configure(fg_color=BG_DARK)

        self.products=Product()
        self.categories=Category()
        
        self.title("GlitterGestion App")
        self.geometry("1200x800")
        self.minsize(800,600)

        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(1, weight=1)

        self.sidebar=Sidebar(master=self)
        self.sidebar.grid(row=0, column=0, sticky="ns", padx=(10,0), pady=10)
        
        self.dashboard_frame=Dashboard(master=self)
        self.dashboard_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.dashboard_frame.grid_columnconfigure(0, weight=1)

        
        self.sidebar.set_dashboard(self.dashboard_frame)


class Dashboard(ctk.CTkFrame):

    def __init__(self,master):
        super().__init__(master)
    
        self.products=master.products
        self.categories=master.categories

        self.grid_rowconfigure(2, weight=1)  
        self.grid_columnconfigure(0, weight=1)

        self.action_bar=ctk.CTkFrame(self, fg_color="transparent")
        self.action_bar.grid(row=1, column=0, sticky="ew", pady=10)

        self.search_entry=ctk.CTkEntry(self.action_bar, placeholder_text="🔍 Search a product (Dior, Fenty...)", width=250, height=38, fg_color=BG_CARD, border_color=PINK, text_color=TEXT)
        self.search_entry.pack(side="left", padx=10)

        self.entry_button=ctk.CTkButton(self.action_bar, text="Search", fg_color=BG_CARD, border_color=PINK, text_color=TEXT, command=self.search)
        self.entry_button.pack(side="left", padx=10)

        self.scrollable_list = ctk.CTkScrollableFrame(self, label_text="✨ Inventory", label_font=ctk.CTkFont(family="Georgia", size=14, weight="bold"), label_text_color=GOLD, fg_color=BG_CARD, scrollbar_button_color=PINK)
        self.scrollable_list.grid(row=2, column=0, sticky="nsew", padx=20, pady=20)

        categories=["ALL"] + self.categories.get_name()
        self.category_menu=ctk.CTkOptionMenu(self.action_bar,  fg_color=BG_CARD, button_color=PINK, button_hover_color=PINK_DARK, text_color=TEXT, values=categories, command=self.filter_by_categories)
        self.category_menu.pack(side="left", padx=10)

        self.refresh_products()

    def filter_by_categories(self,choice):
        if choice=="ALL":
            self.refresh_products()
        
        else:
            result=self.products.get_category(choice)
            self.refresh_products(products=result)

    
    def search(self):
        letter=self.search_entry.get()
        result=self.products.get_product(letter)
        
        if not letter:
            self.refresh_products(products=None)
            return
        
        if result is not None:
            self.refresh_products(products=result)
    
    def export(self):
        products=self.products.get_all()

        if not products:
            return
        
        with open("products.csv","w",newline="",encoding="utf-8") as f:
            writer=csv.DictWriter(f,fieldnames=products[0].keys())
            writer.writeheader()
            writer.writerows(products)
        
    
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
             row=ctk.CTkFrame(self.scrollable_list, fg_color=BG_DARK, corner_radius=10, border_width=1, border_color="#2A2A4A") 
             row.pack(fill="x", expand=True, pady=4, padx=10)
 
             ctk.CTkLabel(row, text=f"#{i['id']}", width=60, text_color=GOLD, font=ctk.CTkFont(weight="bold")).pack(side="left", pady=15, padx=10)
             ctk.CTkLabel(row, text=i["name"], width=200, text_color=TEXT, font=ctk.CTkFont(size=13, weight="bold")).pack(side="left")
             ctk.CTkLabel(row, text=i["description"], width=200, text_color=TEXT_MUTED).pack(side="left")
             ctk.CTkLabel(row, text=f"{i['price']}$", width=80, text_color=PINK, font=ctk.CTkFont(weight="bold")).pack(side="right", padx=10)
             ctk.CTkLabel(row, text=f"Stock: {i['quantity']}", width=100, text_color=TEXT_MUTED).pack(side="right")

class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, width=180, fg_color=BG_SIDEBAR, corner_radius=5)

        self.grid_propagate(False) 
        self.dashboard = None 

        ctk.CTkLabel(self, text="✨ GlitterApp", font=ctk.CTkFont(family="Georgia", size=24, weight="bold"),
    text_color=GOLD).pack(pady=(30, 5))

        self.add_btn = ctk.CTkButton(self, text="✦ Add Product", fg_color=PINK, hover_color=PINK_DARK, font=ctk.CTkFont(weight="bold"), corner_radius=8, height=40, command=self.add)       
        self.add_btn.pack(pady=10, padx=15)

        self.delete_btn = ctk.CTkButton(self, text="✦ Delete Product",  fg_color=PINK, hover_color=PINK_DARK, font=ctk.CTkFont(weight="bold"), corner_radius=8, height=40, command=self.delete)
        self.delete_btn.pack(pady=10, padx=15)

        self.update_btn = ctk.CTkButton(self, text="✦ Update Product",  fg_color=PINK, hover_color=PINK_DARK, font=ctk.CTkFont(weight="bold"), corner_radius=8, height=40, command=self.update)
        self.update_btn.pack(pady=10, padx=15)

        self.export_btn = ctk.CTkButton(self, text="⬇ Export CSV",  fg_color=PINK, hover_color=PINK_DARK, font=ctk.CTkFont(weight="bold"), corner_radius=8, height=40, command=self.export)
        self.export_btn.pack(pady=10, padx=15)

    def set_dashboard(self, dashboard):
        self.dashboard=dashboard

    def add(self):
        if self.dashboard:
            self.dashboard.add_window()

    def delete(self):
        if self.dashboard:
            self.dashboard.delete_window()

    def update(self):
        if self.dashboard:
            self.dashboard.update_pr()

    def export(self):
        if self.dashboard:
            self.dashboard.export()

class UpdateProduct(ctk.CTkToplevel):
    def __init__(self, master, refresh_product):
        super().__init__(master)
        self.configure(fg_color=BG_DARK)
        self.lift()
        self.focus_force()
        self.title("Update a Product Here!")
        self.update_idletasks() 
        width=400
        height=500
        x=(self.winfo_screenwidth()//2)-(width//2)
        y=(self.winfo_screenheight()//2)-(height//2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.refresh=refresh_product
        self.products=master.products
        
        ctk.CTkLabel(self, text="✨ Update Product", font=ctk.CTkFont(family="Georgia", size=20, weight="bold"), text_color=GOLD).pack(pady=(30, 5))
        ctk.CTkLabel(self, text="Choose a column", font=ctk.CTkFont(family="Georgia", size=12, weight="bold"),text_color=GOLD).pack(pady=(20, 5))

        self.column_entry=ctk.CTkOptionMenu(self, values=["name","description","price","quantity"], fg_color=BG_CARD, button_color=PINK, button_hover_color=PINK_DARK,text_color=TEXT, width=280, height=38)
        self.column_entry.pack(pady=(0, 15))
        
        self.id_entry=ctk.CTkEntry(self, placeholder_text="Take the ID of the product to modify", fg_color=BG_CARD, border_color=PINK, text_color=TEXT, width=280, height=38)
        self.id_entry.pack(pady=(0, 15))

        self.change_entry=ctk.CTkEntry(self, placeholder_text="Type your entry", fg_color=BG_CARD, border_color=PINK, text_color=TEXT, width=280, height=38)
        self.change_entry.pack(pady=(0, 15))

        self.save_button=ctk.CTkButton(self, text="Save", fg_color=PINK, hover_color=PINK_DARK, font=ctk.CTkFont(weight="bold"), corner_radius=8, command=self.update_product, width=280, height=44)
        self.save_button.pack(pady=(25, 0))

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
        self.configure(fg_color=BG_DARK)
        self.lift()
        self.focus_force()
        self.title("Delete a Product Here!")
        self.update_idletasks()  
        width=400
        height=300
        x=(self.winfo_screenwidth()//2)-(width//2)
        y=(self.winfo_screenheight()//2)-(height//2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.refresh=refresh_product
        self.products=master.products

        ctk.CTkLabel(self, text="🗑 Delete a Product", font=ctk.CTkFont(family="Georgia", size=20, weight="bold"), text_color=GOLD).pack(pady=(30, 20))

        self.id_entry=ctk.CTkEntry(self, placeholder_text="Enter Product ID", fg_color=BG_CARD, border_color=PINK, text_color=TEXT, width=280, height=38)
        self.id_entry.pack(pady=(0, 15))

        self.id_entry.pack(pady=10)

        self.save_button=ctk.CTkButton(self, text="Delete from Database", fg_color=PINK, hover_color=PINK_DARK, font=ctk.CTkFont(weight="bold"), corner_radius=8, width=280, height=44, command=self.delete_product)
        self.save_button.pack(pady=(25, 0))
        
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
            self.configure(fg_color=BG_DARK)
            self.lift()
            self.focus_force()
            self.title("Add new Products to GlitterApp!")
            self.update_idletasks() 
            width=400
            height=500
            x=(self.winfo_screenwidth()//2)-(width//2)
            y=(self.winfo_screenheight()//2)-(height//2)
            self.geometry(f"{width}x{height}+{x}+{y}")
            self.refresh=refresh_product
            self.products=master.products
        
            ctk.CTkLabel(self,text="✦ Add a new product", font=ctk.CTkFont(family="Georgia", size=20, weight="bold"), text_color=GOLD).pack(pady=(30, 20))

            self.name_entry=ctk.CTkEntry(self,placeholder_text="Enter a name", fg_color=BG_CARD, border_color=PINK, text_color=TEXT, width=280, height=38)
            self.name_entry.pack(pady=(0, 15))

            self.name_entry.pack(pady=10)

            self.description_entry=ctk.CTkEntry(self,placeholder_text="Enter a description", fg_color=BG_CARD, border_color=PINK, text_color=TEXT, width=280, height=38)
            self.description_entry.pack(pady=(0, 15)) 
            
            self.price_entry=ctk.CTkEntry(self, placeholder_text="Enter a price", fg_color=BG_CARD, border_color=PINK, text_color=TEXT, width=280, height=38)
            self.price_entry.pack(pady=(0, 15))
        
            self.quantity_entry=ctk.CTkEntry(self, placeholder_text="Enter a quantity", fg_color=BG_CARD, border_color=PINK, text_color=TEXT, width=280, height=38)
            self.quantity_entry.pack(pady=(0, 15))
   
            self.category_entry=ctk.CTkEntry(self, placeholder_text="Enter an ID category", fg_color=BG_CARD, border_color=PINK, text_color=TEXT, width=280, height=38)
            self.category_entry.pack(pady=(0, 15))
     
            self.save_button=ctk.CTkButton(self, text="Save to Database", fg_color=PINK, hover_color=PINK_DARK, font=ctk.CTkFont(weight="bold"), corner_radius=8, width=280, height=44, command=self.sumbit_data)
            self.save_button.pack(pady=(25, 0))

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
                ctk.CTkLabel(self, text=f"{name} added to inventory!", text_color="green").pack()
                self.refresh()
                self.destroy()
            
            else:
                ctk.CTkLabel(self, text="Synthax Error or Error", text_color="red").pack()

    
