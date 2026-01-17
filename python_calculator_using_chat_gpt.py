import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x420")
        self.root.resizable(False, False)

        self.expression = ""

        # Display
        self.display = tk.Entry(
            root,
            font=("Arial", 20),
            bd=10,
            relief=tk.RIDGE,
            justify="right"
        )
        self.display.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

        # Buttons frame
        button_frame = tk.Frame(root)
        button_frame.pack(expand=True, fill=tk.BOTH)

        # Button layout
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        # Create buttons
        for (text, row, col) in buttons:
            btn = tk.Button(
                button_frame,
                text=text,
                font=("Arial", 16),
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Clear button
        clear_btn = tk.Button(
            button_frame,
            text="C",
            font=("Arial", 16),
            bg="lightgray",
            command=self.clear
        )
        clear_btn.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Configure grid weights
        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += char
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
