import tkinter as tk
from tkinter import ttk,messagebox
class ordermanagement:
    def __init__(self,root):
        self.root=root
        self.root.title("restaurant order app")
        self.menuitems={
            "MASALA DOSA":2,
            "MYSORE PAK":2,
            "CHOLE BATURE":4,
            "LASSI":3
        }
        self.exchangerate=95
        self.setup_background(root)
        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        tk.label(frame,text="hotel management",font=("Arial",20,"bold")).grid(row=0,columnspan=3,padx=10,pady=10)
        self.menu_label={}
        self.menu_quantities={}
        for i,(item,price)in enumerate(self.menu_items.items(),start=1):
            label=ttk.Label(frame,text=f"{item},(${price})")
            label.grid(row=i,column=0,padx=5,pady=5)
            

# 11) Create a currency selection section:
#     a) Create a `StringVar` called `self.currency_var`.
#     b) Add a "Currency:" label.
#     c) Add a dropdown (`ttk.Combobox`) with options "USD" and "INR".
#     d) Set default selection to "USD".
#     e) Attach a trace to `self.currency_var` so when currency changes,
#        it automatically calls `self.update_menu_prices`.

# 12) Add a "Place Order" button:
#     a) When clicked, it runs `self.place_order()`.

# 13) Define `setup_background(self, root)`:
#     a) Create a Canvas of size 800x600.
#     b) Load the background image file `background.png` using `tk.PhotoImage`.
#     c) Resize it approximately using `.subsample(...)`.
#     d) Place the image on the canvas using `create_image(...)`.
#     e) Store the image reference (`canvas.image`) to prevent garbage collection.

# 14) Define `update_menu_prices(self, *args)`:
#     a) Read the selected currency from `self.currency_var`.
#     b) Set currency symbol:
#        - INR -> "₹"
#        - USD -> "$"
#     c) Set conversion rate:
#        - INR -> exchange rate
#        - USD -> 1
#     d) Update every menu label text to show the converted price.

# 15) Define `place_order(self)`:
#     a) Initialize `total_cost = 0` and `order_summary` message text.
#     b) Determine currency symbol and conversion rate (same as above).
#     c) Loop through each menu item entry:
#        i) Read quantity using `entry.get()`.
#        ii) If quantity is a digit, convert it to int.
#        iii) Compute price (converted), item cost, and add to total.
#        iv) If quantity > 0, add line details to `order_summary`.
#     d) If `total_cost > 0`, show the order summary in a messagebox.
#     e) Else, show an error message asking the user to order at least one item.

# 16) In the main block (`if __name__ == "__main__":`):
#     a) Create the main window using `root = tk.Tk()`.
#     b) Create the app object `app = RestaurantOrderManagement(root)`.
#     c) Set the window size to 800x600.
#     d) Start the GUI loop using `root.mainloop()`.