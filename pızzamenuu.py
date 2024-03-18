import tkinter as tk
from tkinter import ttk

class PizzaMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Menüsü")

        self.size_prices = {'Küçük': 10, 'Orta': 12, 'Büyük': 14}
        self.topping_prices = {'Salam': 2, 'Mantar': 1, 'Zeytin': 1, 'Ananas': 2}

        self.size_label = ttk.Label(root, text="Pizza Boyutu:")
        self.size_label.grid(row=0, column=0, padx=10, pady=10)
        self.size_combo = ttk.Combobox(root, values=list(self.size_prices.keys()))
        self.size_combo.grid(row=0, column=1, padx=10, pady=10)
        self.size_combo.current(0)

        self.toppings_label = ttk.Label(root, text="Malzemeler:")
        self.toppings_label.grid(row=1, column=0, padx=10, pady=10)

        self.selected_toppings = []
        for i, (topping, price) in enumerate(self.topping_prices.items(), start=2):
            topping_check = ttk.Checkbutton(root, text=f"{topping} - ${price}", command=lambda t=topping: self.toggle_topping(t))
            topping_check.grid(row=i, column=0, columnspan=2, padx=10, pady=5)

        self.total_label = ttk.Label(root, text="Toplam Tutar: $0")
        self.total_label.grid(row=i+1, column=0, columnspan=2, padx=10, pady=10)

        self.order_button = ttk.Button(root, text="Sipariş Ver", command=self.place_order)
        self.order_button.grid(row=i+2, column=0, columnspan=2, padx=10, pady=10)

    def toggle_topping(self, topping):
        if topping in self.selected_toppings:
            self.selected_toppings.remove(topping)
        else:
            self.selected_toppings.append(topping)

    def place_order(self):
        size_price = self.size_prices[self.size_combo.get()]
        toppings_price = sum(self.topping_prices[topping] for topping in self.selected_toppings)
        total_price = size_price + toppings_price
        self.total_label.config(text=f"Toplam Tutar: ${total_price}")

def main():
    root = tk.Tk()
    app = PizzaMenuApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()