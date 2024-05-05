# Import libraries
import math
import tkinter as tk


# Define the calculator class
class Calculator:
    """
    This class represents a simple scientific calculator with a graphical user interface.

    Attributes:
        last_answer (list): A list to store the last answer for the 'Ans' button.
        master (tk.Tk): The main tkinter window object.
    """
    def __init__(self, master):
        """
        Initialize the calculator object.

        Args:
            master (tk.Tk): The main tkinter window object.
        """

        self.last_answer = []
        self.master = master
        master.title("Calculator")

        # Define the dark theme colors for the calculator GUI
        dark_background = "#333333"
        light_text = "#FFFFFF"

        # Set the theme for the calculator application window
        master.configure(bg=dark_background)

        # Load an image for the calculator icon (optional)
        # Replace "img.png" with the actual path to your image file
        self.icon = tk.PhotoImage(file="img.png")
        master.iconphoto(True, self.icon)

        # Create the display entry widget to show calculation results
        self.display = tk.Entry(master, width=40, borderwidth=5, font=('Arial', 16), bg="#555555", fg=light_text)
        self.display.grid(row=0, column=0, columnspan=7, padx=10, pady=10)

        # Define button labels for calculator functions
        buttons = [
            'Rad', 'Deg', 'x!', '(', ')', '%', 'AC',
            'Inv', 'sin', 'ln', '7', '8', '9', '/',
            '\u03C0', 'cos', 'log', '4', '5', '6', '*',
            'e', 'tan', '\u221A', '1', '2', '3', '-',
            '^2', 'EXP', '^y', '0', '.', '=', '+'
        ]
        # Create buttons and arrange them in a grid layout on the calculator window
        row = 1
        col = 0
        # Make the grid cells expandable to fit content
        master.grid_columnconfigure(tuple(range(7)), weight=1)
        master.grid_rowconfigure(tuple(range(1, row + 1)), weight=1)

        for button in buttons:
            # Create buttons with appropriate functionality based on the label
            if button == '=':
                tk.Button(master, text=button, width=10, height=2, command=self.evaluate,
                          bg=dark_background).grid(row=row, column=col,
                                                   sticky="nsew",
                                                   padx=1, pady=1)

            # Add functionality for Radian/Degree mode toggle (not implemented here)
            elif button == 'Rad':
                tk.Button(master, text=button, width=10, height=2, command=self.radians, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1, pady=1)
            elif button == 'Deg':
                tk.Button(master, text=button, width=10, height=2, command=self.degree, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1, pady=1)

            elif button == 'x!':
                tk.Button(master, text=button, width=10, height=2, command=self.factorial, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1, pady=1)

            elif button == 'Inv':
                tk.Button(master, text=button, width=10, height=2, command=self.inverse, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1, pady=1)

            elif button == 'sin':
                tk.Button(master, text=button, width=10, height=2, command=self.sine, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1,
                    pady=1)

            elif button == 'ln':
                tk.Button(master, text=button, width=10, height=2, command=self.ln, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1,
                    pady=1)

            elif button == '\u03C0':
                tk.Button(master, text=button, width=10, height=2, command=self.pi, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1,
                    pady=1)
            elif button == 'cos':
                tk.Button(master, text=button, width=10, height=2, command=self.cosine, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1, pady=1)

            elif button == 'tan':
                tk.Button(master, text=button, width=10, height=2, command=self.tan, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1,
                    pady=1)

            elif button == 'Ans':
                tk.Button(master, text=button, width=10, height=2, command=self.ans, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1,
                    pady=1)

            elif button == 'x^2':
                tk.Button(master, text=button, width=10, height=2, command=self.power, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1,
                    pady=1)

            elif button == 'AC':
                tk.Button(master, text=button, width=10, height=2, command=self.clear, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1,
                    pady=1)

            elif button == '\u221A':
                tk.Button(master, text=button, width=10, height=2, command=self.square_root, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1, pady=1)
            elif button == 'log':
                tk.Button(master, text=button, width=10, height=2, command=self.logarithm, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1,
                    pady=1)

            elif button == 'EXP':
                tk.Button(master, text=button, width=10, height=2, command=self.exponent, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1, pady=1)

            elif button == 'mod':
                tk.Button(master, text=button, width=10, height=2, command=self.modulus, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1, pady=1)
            elif button == '%':
                tk.Button(master, text=button, width=10, height=2, command=self.percent, bg=dark_background).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=1, pady=1)
            else:
                tk.Button(master,
                          text=button,
                          width=10, height=2,
                          command=lambda x=button: self.add_to_display(x), bg=dark_background).grid(row=row,
                                                                                                    column=col,
                                                                                                    sticky="nsew",
                                                                                                    padx=1, pady=1)

            col += 1
            if col > 6:
                col = 0
                row += 1

    def add_to_display(self, value):
        self.display.insert(tk.END, value)

    def clear(self):
        self.display.delete(0, tk.END)

    def evaluate(self):
        try:
            result = str(eval(self.display.get()))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            print(f"Error: {e}")

    def square_root(self):
        try:
            value = float(self.display.get())
            result = math.sqrt(value)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except (ValueError, TypeError) as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            print(f"Error: {e}")

    def logarithm(self):
        try:
            value = float(self.display.get())
            result = math.log(value)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            print(f"Error: {e}")

    def exponent(self):
        try:
            value = float(self.display.get())
            result = math.exp(value)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            print(f"Error: {e}")

    def modulus(self):
        try:
            # Get the two values from the display field
            values = self.display.get().split(",")
            if len(values) != 2:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error: Provide two values separated by a comma")
                return

            value1 = float(values[0].strip())
            value2 = float(values[1].strip())

            result = value1 % value2
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            print(f"Error: {e}")

    def percent(self):
        try:
            value = float(self.display.get())
            result = value * 100
            self.display.delete(0, tk.END)
            self.display.insert(0, f"{result:.2f}")
        except (ValueError, ZeroDivisionError) as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            print(f"Error: {e}")

    def radians(self):
        try:
            value = float(self.display.get())
            result = math.radians(value)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            print(f"Error: {e}")

    def degree(self):
        try:
            value = float(self.display.get())
            result = math.degrees(value)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            print(f"Error: {e}")

    def factorial(self):
        try:
            value = int(self.display.get())
            result = math.factorial(value)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            print(f"Error: {e}")

    def inverse(self):
        pass

    def sine(self):
        try:
            value = float(self.display.get())
            result = math.sin(value)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            print(f"Error: {e}")

    def ln(self):
        try:
            value = float(self.display.get())
            result = math.log10(value)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            print(f"Error: {e}")

    def pi(self):
        try:
            value = float(self.display.get())
            result = math.pi * value
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            print(f"Error: {e}")

    def cosine(self):
        try:
            value = float(self.display.get())
            result = math.cos(value)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            print(f"Error: {e}")

    def tan(self):
        try:
            value = float(self.display.get())
            result = math.tan(value)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            print(f"Error: {e}")

    def ans(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.last_answer = result  # Store the last answer
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            print(f"Error: {e}")
        else:
            try:
                self.display.delete(0, tk.END)
                self.display.insert(0, str(self.last_answer))
            except AttributeError:
                self.display.delete(0, tk.END)
                self.display.insert(0, "No previous answer")

    def power(self):
        try:
            value = float(self.display.get())
            result = math.pow(value, 2)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            print(f"Error: {e}")


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
