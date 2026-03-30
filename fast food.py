import tkinter as tk
from tkinter import ttk, messagebox

# Menu data

menu = {
    "Pizza": {
        "Small": {"Cheese Pizza": 800, "Veg Pizza": 750},
        "Medium": {"Cheese Pizza": 1200, "Pepperoni Pizza": 1300},
        "Large": {"Fajita Pizza": 1600, "Tikka Pizza": 1700}
    },
    "Burger": {
        "Small": {"Zinger": 400},
        "Medium": {"Cheese Burger": 500},
        "Large": {"Double Patty": 600}
    },
    "Drinks": {
        "Small": {"Water": 50, "Coke": 50},
        "Medium": {"Cold Drink": 80, "Coke": 80},
        "Large": {"Fresh Juice": 150, "Coke": 100}
    },
    "Pasta": {
        "Small": {"White Sauce Pasta": 450},
        "Medium": {"White Sauce Pasta": 600},
        "Large": {"Chicken Pasta": 650, "White Sauce Pasta": 750}
    },
    "Shawarma": {
        "Small": {"Chicken Shawarma": 200, "Beef Shawarma": 250},
        "Medium": {"Chicken Shawarma": 300, "Beef Shawarma": 350},
        "Large": {"Chicken Shawarma": 400, "Beef Shawarma": 450}
    },
    "Karahi": {
        "Small": {"Chicken Karahi": 800, "Mutton Karahi": 1000},
        "Medium": {"Chicken Karahi": 1300, "Mutton Karahi": 1800},
        "Large": {"Chicken Karahi": 1800, "Mutton Karahi": 2500}
    },
    "Malai Boti": {
        "Small": {"Malai Boti": 500},
        "Medium": {"Malai Boti": 800},
        "Large": {"Malai Boti": 1100}
    },
    "Breads": {
        "Standard": {"Roti": 20, "Naan": 30}
    },
    "Desserts": {
        "Standard": {"Chocolate Cake": 300, "Ice Cream": 200, "Cupcake": 120, "Donut": 100}
    },
    "Snacks": {
        "Standard": {"Nuggets": 250, "Wings": 300, "Samosa": 60, "Roll": 80}
    }
}
cart = []

def add_to_cart(item, price, qty_entry):
    try:
        qty = int(qty_entry.get())
        if qty <= 0:
            raise ValueError
        cart.append((item, qty, price * qty))
        update_bill()
    except ValueError:
        messagebox.showerror("Error", "Enter valid quantity.")

def update_bill():
    for row in bill_table.get_children():
        bill_table.delete(row)
    
    total = 0
    for item, qty, subtotal in cart:
        bill_table.insert("", "end", values=(item, qty, subtotal))
        total += subtotal
    
    tax = round(total * 0.05)
    grand_total = total + tax

    total_var.set(f"Rs. {total}")
    tax_var.set(f"Rs. {tax}")
    grand_var.set(f"Rs. {grand_total}")

# GUI setup
root = tk.Tk()
root.title("Fast Food Ordering System")
root.geometry("950x600")

menu_frame = tk.Frame(root)
menu_frame.pack(side="left", fill="y", padx=10, pady=10)

bill_frame = tk.Frame(root)
bill_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Tabs
tabs = ttk.Notebook(menu_frame)
tabs.pack(fill="both", expand=True)

for category, sizes in menu.items():
    tab = ttk.Frame(tabs)    #make new tab
    tabs.add(tab, text=category)

    row = 0   #grid row numbering start 
    for size, items in sizes.items():
        tk.Label(tab, text=f"{size} Size", font=("Arial", 10, "bold"), fg="blue").grid(row=row, column=0, sticky="w")  #hr siza ka naam  tab py show hona
        row += 1
        for item, price in items.items():
            tk.Label(tab, text=f"{item} - Rs.{price}").grid(row=row, column=0, sticky="w")
            qty_entry = tk.Entry(tab, width=5)
            qty_entry.grid(row=row, column=1)
            tk.Button(tab, text="Add", command=lambda i=item, p=price, q=qty_entry: add_to_cart(i, p, q)).grid(row=row, column=2)
            row += 1

# Bill Table(items added to cart    )
tk.Label(bill_frame, text="BILL", font=("Arial", 14, "bold")).pack()
columns = ("Item", "Quantity", "Price")
bill_table = ttk.Treeview(bill_frame, columns=columns, show="headings", height=15)
for col in columns:
    bill_table.heading(col, text=col)
    bill_table.column(col, anchor="center", width=120)
bill_table.pack(pady=10)

# Bill Totals
total_var = tk.StringVar()             #ye variables total values ko dynnamically update krty hai
tax_var = tk.StringVar()
grand_var = tk.StringVar()

tk.Label(bill_frame, text="Total:").pack()
tk.Label(bill_frame, textvariable=total_var).pack()

tk.Label(bill_frame, text="Tax (5%):").pack()
tk.Label(bill_frame, textvariable=tax_var).pack()

tk.Label(bill_frame, text="Grand Total:").pack()
tk.Label(bill_frame, textvariable=grand_var).pack()

# Feedback Box
tk.Label(bill_frame, text="Feedback:", font=("Arial", 12, "bold")).pack(pady=(15, 0))
feedback_entry = tk.Text(bill_frame, height=3, width=40)
feedback_entry.pack()

def show_feedback():
    feedback = feedback_entry.get("1.0", "end").strip()
    if feedback:
        messagebox.showinfo("Feedback Received", f"Thanks for your feedback:\n{feedback}")
    else:
        messagebox.showwarning("Empty", "Please write some feedback first.")

tk.Button(bill_frame, text="Submit Feedback", command=show_feedback).pack(pady=10)

root.mainloop()
                                     