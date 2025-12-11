import tkinter as tk
from tkinter import ttk
import math

class MultiModeCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi Mode Calculator")
        self.geometry("600x350")

        # Notebook for multiple modes
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        # Add all modes
        self.create_calculator_tab()
        self.create_currency_tab()
        self.create_length_tab()
        self.create_rates_tab()
        self.create_temperature_tab()

    # Calculator Tab
    def create_calculator_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Calculator")

        self.calc_display = tk.Entry(tab, font=("Consolas", 18), justify='right')
        self.calc_display.pack(fill='x', padx=10, pady=10)

        buttons = [
            ["C", "AC","⌫","%", "+", "sin", "cos", "tan", "π"],
            ["7", "8", "9", "-", "sinh", "cosh", "tanh", "2π"],
            ["4", "5", "6", "*", "√", "∛", "x!", "rad"],
            ["1", "2", "3", "/", "x²", "x³", "ln", "deg"],
            ["0", ".", "e", "="]
        ]

        grid = tk.Frame(tab)
        grid.pack()

        for r, row in enumerate(buttons):
            for c, label in enumerate(row):
                btn = tk.Button(grid, text=label, width=6, height=2,
                                command=lambda l=label: self.on_calc_click(l))
                btn.grid(row=r, column=c, padx=2, pady=2)

    def on_calc_click(self, label):
        expr = self.calc_display.get()
        try:
            if label=="⌫": # Backspace
                self.calc_display.delete(len(expr)-1,tk.END)
            elif label == "C":
                self.calc_display.delete(0, tk.END)
            elif label == "AC":
                self.calc_display.delete(0, tk.END)
            elif label == "=":
                result = eval(expr.replace("π", str(math.pi)).replace("e", str(math.e)))
                self.calc_display.delete(0, tk.END)
                self.calc_display.insert(tk.END, str(result))
            elif label == "√":
                self.calc_display.insert(tk.END, "math.sqrt(")
            elif label == "∛":
                self.calc_display.insert(tk.END, "**(1/3)")
            elif label == "x²":
                self.calc_display.insert(tk.END, "**2")
            elif label == "x³":
                self.calc_display.insert(tk.END, "**3")
            elif label == "x!":
                self.calc_display.insert(tk.END, "math.factorial(")
            elif label in ["sin", "cos", "tan", "sinh", "cosh", "tanh", "ln"]:
                self.calc_display.insert(tk.END, f"math.{label}(")
            elif label == "rad":
                self.calc_display.insert(tk.END, "math.radians(")
            elif label == "deg":
                self.calc_display.insert(tk.END, "math.degrees(")
            else:
                self.calc_display.insert(tk.END, label)
        except Exception:
            self.calc_display.delete(0, tk.END)
            self.calc_display.insert(tk.END, "Error")

    def toggle_theme(self):
        style=ttk.Style(self)
        current=style.theme_use()
        new_theme="calm" if current=="default" else "default"
        style.theme_use(new_theme)

        ttk.Button(self,text="Toggle Theme",command=self.toggle_theme).pack(pady=5)

    # Currency Converter Tab
    def create_currency_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Currency")

        ttk.Label(tab, text="Amount:").pack()
        self.curr_amount = tk.Entry(tab)
        self.curr_amount.pack()

        ttk.Label(tab, text="Rate (e.g. USD to INR):").pack()
        self.curr_rate = tk.Entry(tab)
        self.curr_rate.pack()

        self.curr_result = tk.Label(tab, text="", font=("Arial", 14))
        self.curr_result.pack()

        ttk.Button(tab, text="Convert", command=self.convert_currency).pack()

    def convert_currency(self):
        try:
            amt = float(self.curr_amount.get())
            rate = float(self.curr_rate.get())
            self.curr_result.config(text=f"Converted: {amt * rate:.2f}")
        except:
            self.curr_result.config(text="Invalid input")

    # Length Converter Tab
    def create_length_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Length")

        ttk.Label(tab, text="Meters:").pack()
        self.len_meters = tk.Entry(tab)
        self.len_meters.pack()

        self.len_result = tk.Label(tab, text="", font=("Arial", 14))
        self.len_result.pack()

        ttk.Button(tab, text="To Feet", command=self.convert_length).pack()

    def convert_length(self):
        try:
            meters = float(self.len_meters.get())
            feet = meters * 3.28084
            self.len_result.config(text=f"{feet:.2f} ft")
        except:
            self.len_result.config(text="Invalid input")

    # Rates Tab
    def create_rates_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Rates")

        ttk.Label(tab, text="Principal:").pack()
        self.rate_principal = tk.Entry(tab)
        self.rate_principal.pack()

        ttk.Label(tab, text="Rate (%):").pack()
        self.rate_percent = tk.Entry(tab)
        self.rate_percent.pack()

        ttk.Label(tab, text="Time (years):").pack()
        self.rate_time = tk.Entry(tab)
        self.rate_time.pack()

        self.rate_result = tk.Label(tab, text="", font=("Arial", 14))
        self.rate_result.pack()

        ttk.Button(tab, text="Calculate Simple Interest", command=self.calculate_interest).pack()

    def calculate_interest(self):
        try:
            p = float(self.rate_principal.get())
            r = float(self.rate_percent.get())
            t = float(self.rate_time.get())
            si = (p * r * t) / 100
            self.rate_result.config(text=f"Interest: {si:.2f}")
        except:
            self.rate_result.config(text="Invalid input")

    # Temperature Converter Tab
    def create_temperature_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Temperature")

        ttk.Label(tab, text="Celsius:").pack()
        self.temp_celsius = tk.Entry(tab)
        self.temp_celsius.pack()

        self.temp_result = tk.Label(tab, text="", font=("Arial", 14))
        self.temp_result.pack()

        ttk.Button(tab, text="To Fahrenheit", command=self.convert_temperature).pack()

    def convert_temperature(self):
        try:
            c = float(self.temp_celsius.get())
            f = (c * 9/5) + 32
            self.temp_result.config(text=f"{f:.2f} °F")
        except:
            self.temp_result.config(text="Invalid input")

# Entry point
if __name__ == "__main__":
    app = MultiModeCalculator()
    app.mainloop()