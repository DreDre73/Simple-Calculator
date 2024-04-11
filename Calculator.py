import tkinter as tk


class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("350x400")

        # Entry widget for calculations
        self.entry = tk.Entry(self.window, font=('Arial', 20))
        self.entry.pack(padx=50, pady=20)

        self.entry.bind("<Return>", lambda event: self.calculate())

        # Columns and frame for buttons
        button_frame = tk.Frame(self.window)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)

        # Clear Button
        btn_clear = tk.Button(button_frame, text="C", font=('Arial', 18), command=self.clear_field)
        btn_clear.grid(row=0, column=0, sticky=tk.W + tk.E)

        # Divide Button
        btn_div = tk.Button(button_frame, text="/", font=('Arial', 18), command=lambda: self.update_field("/"))
        btn_div.grid(row=0, column=1, sticky=tk.W + tk.E)

        # Decimal Button
        btn_dec = tk.Button(button_frame, text=".", font=('Arial', 18), command=lambda: self.update_field("."))
        btn_dec.grid(row=0, column=2, sticky=tk.W + tk.E)

        # Multiply Button
        btn_multiply = tk.Button(button_frame, text="*", font=('Arial', 18), command=lambda: self.update_field("*"))
        btn_multiply.grid(row=0, column=3, sticky=tk.W + tk.E)

        # 7 Button
        btn_7 = tk.Button(button_frame, text="7", font=('Arial', 18), command=lambda: self.update_field("7"))
        btn_7.grid(row=1, column=0, sticky=tk.W + tk.E)

        # 8 Button
        btn_8 = tk.Button(button_frame, text="8", font=('Arial', 18), command=lambda: self.update_field("8"))
        btn_8.grid(row=1, column=1, sticky=tk.W + tk.E)

        # 9 Button
        btn_9 = tk.Button(button_frame, text="9", font=('Arial', 18), command=lambda: self.update_field("9"))
        btn_9.grid(row=1, column=2, sticky=tk.W + tk.E)

        # Subtract Button
        btn_sub = tk.Button(button_frame, text="-", font=('Arial', 18), command=lambda: self.update_field("-"))
        btn_sub.grid(row=1, column=3, sticky=tk.W + tk.E)

        # 4 Button
        btn_4 = tk.Button(button_frame, text="4", font=('Arial', 18), command=lambda: self.update_field("4"))
        btn_4.grid(row=2, column=0, sticky=tk.W + tk.E)

        # 5 Button
        btn_5 = tk.Button(button_frame, text="5", font=('Arial', 18), command=lambda: self.update_field("5"))
        btn_5.grid(row=2, column=1, sticky=tk.W + tk.E)

        # 6 Button
        btn_6 = tk.Button(button_frame, text="6", font=('Arial', 18), command=lambda: self.update_field("6"))
        btn_6.grid(row=2, column=2, sticky=tk.W + tk.E)

        # Addition Button
        btn_add = tk.Button(button_frame, text="+", font=('Arial', 18), command=lambda: self.update_field("+"))
        btn_add.grid(row=2, column=3, sticky=tk.W + tk.E)

        # 1 Button
        btn_1 = tk.Button(button_frame, text="1", font=('Arial', 18), command=lambda: self.update_field("1"))
        btn_1.grid(row=3, column=0, sticky=tk.W + tk.E)

        # 2 Button
        btn_2 = tk.Button(button_frame, text="2", font=('Arial', 18), command=lambda: self.update_field("2"))
        btn_2.grid(row=3, column=1, sticky=tk.W + tk.E)

        # 3 Button
        btn_3 = tk.Button(button_frame, text="3", font=('Arial', 18), command=lambda: self.update_field("3"))
        btn_3.grid(row=3, column=2, sticky=tk.W + tk.E)

        # Square Root Button
        btn_square_root = tk.Button(button_frame, text="√", font=('Arial', 18),
                                    command=lambda: self.update_field("math.sqrt("))
        btn_square_root.grid(row=3, column=3, sticky=tk.W + tk.E)

        # Left Parenthesis Button
        btn_left_par = tk.Button(button_frame, text="(", font=('Arial', 18), command=lambda: self.update_field("("))
        btn_left_par.grid(row=4, column=0, sticky=tk.W + tk.E)

        # 0 Button
        btn_0 = tk.Button(button_frame, text="0", font=('Arial', 18), command=lambda: self.update_field("0"))
        btn_0.grid(row=4, column=1, sticky=tk.W + tk.E)

        # Right Parenthesis Button
        btn_right_par = tk.Button(button_frame, text=")", font=('Arial', 18), command=lambda: self.update_field(")"))
        btn_right_par.grid(row=4, column=2, sticky=tk.W + tk.E)

        # Equal Button
        btn_equal = tk.Button(button_frame, text="=", font=('Arial', 18), command=self.calculate)
        btn_equal.grid(row=4, column=3, sticky=tk.W + tk.E)

        # Displays the buttons on the screen Button
        button_frame.pack(fill='x', padx=10, pady=10)

        self.window.config(background='firebrick4')  # Background Color
        self.window.mainloop()

    # Clears the input field
    def clear_field(self):
        self.entry.delete(0, tk.END)

    # Updates field after buttons are pressed
    def update_field(self, value):
        current_text = self.entry.get().strip()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current_text + value)

    # Calculates values from input field and updates them back to input field
    def calculate(self):
        try:
            expression = self.entry.get().strip()
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")


Calculator()
