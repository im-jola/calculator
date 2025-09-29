# GUI Calculator
from tkinter import *
import math
from simpleeval import simple_eval
from tkinter import ttk


class Calculator:
    def __init__(self):
        self.memory = 0
        self.buttons = []
        self.window = Tk()
        self.window.title("Calculator")
        self.window.minsize(width=220, height=370)

        for c in range(5): self.window.grid_columnconfigure(c, weight=1)
        for r in range(12): self.window.grid_rowconfigure(r, weight=1)


        self.window.bind('<Key>', self.key_pressed)

        self.theme_choice = StringVar(self.window)
        self.theme_choice.set('Light')

        self.theme_menu = OptionMenu(self.window, self.theme_choice, "Light", "Dark", "Dark blue", command=self.theme)
        self.buttons.append(self.theme_menu)
        self.theme_menu.grid(columnspan=4, row=0, column=2, pady=3, padx=3, sticky='nsew')

        self.entry = Entry(self.window, width=31)
        self.entry.grid(row=1, column=0, columnspan=5, pady=3, padx=3, sticky='nsew')

        # Buttons

        self.memory_c = Button(text='MC', width=4, command=self.memory_clear)
        self.buttons.append(self.memory_c)
        self.memory_c.grid(column=0, row=2, pady=3, padx=3, sticky='nsew')

        self.memory_r = Button(text='MR', width=4, command=self.memory_recall)
        self.buttons.append(self.memory_r)
        self.memory_r.grid(column=1, row=2, pady=3, padx=3, sticky='nsew')

        self.memory_minus = Button(text='M-', width=4, command=self.memory_subtract)
        self.buttons.append(self.memory_minus)
        self.memory_minus.grid(column=2, row=2, pady=3, padx=3, sticky='nsew')

        self.memory_plus = Button(text='M+', width=4, command=self.memory_add)
        self.buttons.append(self.memory_plus)
        self.memory_plus.grid(column=3, row=2, pady=3, padx=3, sticky='nsew')

        self.divide = Button(text='/', width=4, command=lambda: self.entry.insert(END, '/'))
        self.buttons.append(self.divide)
        self.divide.grid(column=4, row=2, pady=3, padx=3, sticky='nsew')

        self.sqrt = Button(text='√', width=4, command=self.square_root)
        self.buttons.append(self.sqrt)
        self.sqrt.grid(column=0, row=3, pady=3, padx=3, sticky='nsew')

        self.seven = Button(text='7', width=4, command=lambda: self.entry.insert(END, '7'))
        self.buttons.append(self.seven)
        self.seven.grid(column=1, row=3, pady=3, padx=3, sticky='nsew')

        self.eight = Button(text='8', width=4, command=lambda: self.entry.insert(END, '8'))
        self.buttons.append(self.eight)
        self.eight.grid(column=2, row=3, pady=3, padx=3, sticky='nsew')

        self.nine = Button(text='9', width=4, command=lambda: self.entry.insert(END, '9'))
        self.buttons.append(self.nine)
        self.nine.grid(column=3, row=3, pady=3, padx=3, sticky='nsew')

        self.multiply = Button(text='*', width=4, command=lambda: self.entry.insert(END, '*'))
        self.buttons.append(self.multiply)
        self.multiply.grid(column=4, row=3, pady=3, padx=3, sticky='nsew')

        self.neg_number = Button(text='+/-', width=4, command=self.negative_num)
        self.buttons.append(self.neg_number)
        self.neg_number.grid(column=0, row=4, pady=3, padx=3, sticky='nsew')

        self.four = Button(text='4', width=4, command=lambda: self.entry.insert(END, '4'))
        self.buttons.append(self.four)
        self.four.grid(column=1, row=4, pady=3, padx=3, sticky='nsew')

        self.five = Button(text='5', width=4, command=lambda: self.entry.insert(END, '5'))
        self.buttons.append(self.five)
        self.five.grid(column=2, row=4, pady=3, padx=3, sticky='nsew')

        self.six = Button(text='6', width=4, command=lambda: self.entry.insert(END, '6'))
        self.buttons.append(self.six)
        self.six.grid(column=3, row=4, pady=3, padx=3, sticky='nsew')

        self.subtract = Button(text='-', width=4, command=lambda: self.entry.insert(END, '-'))
        self.buttons.append(self.subtract)
        self.subtract.grid(column=4, row=4, pady=3, padx=3, sticky='nsew')

        self.delete_last = Button(text='DEL', width=4, command=self.delete_last_char)
        self.buttons.append(self.delete_last)
        self.delete_last.grid(column=0, row=5, pady=3, padx=3, sticky='nsew')

        self.one = Button(text='1', width=4, command=lambda: self.entry.insert(END, '1'))
        self.buttons.append(self.one)
        self.one.grid(column=1, row=5, pady=3, padx=3, sticky='nsew')

        self.two = Button(text='2', width=4, command=lambda: self.entry.insert(END, '2'))
        self.buttons.append(self.two)
        self.two.grid(column=2, row=5, pady=3, padx=3, sticky='nsew')

        self.three = Button(text='3', width=4, command=lambda: self.entry.insert(END, '3'))
        self.buttons.append(self.three)
        self.three.grid(column=3, row=5, pady=3, padx=3, sticky='nsew')

        self.plus = Button(text='+', width=4, command=lambda: self.entry.insert(END, '+'))
        self.buttons.append(self.plus)
        self.plus.grid(column=4, row=5, pady=3, padx=3, sticky='nsew')

        self.ac = Button(text='AC', width=4, command=self.delete_everything)
        self.buttons.append(self.ac)
        self.ac.grid(column=0, row=6, pady=3, padx=3, sticky='nsew')

        self.zero = Button(text='0', width=4, command=lambda: self.entry.insert(END, '0'))
        self.buttons.append(self.zero)
        self.zero.grid(column=1, row=6, pady=3, padx=3, sticky='nsew')

        self.decimal = Button(text='.', width=4, command=lambda: self.entry.insert(END, '.'))
        self.buttons.append(self.decimal)
        self.decimal.grid(column=2, row=6, pady=3, padx=3, sticky='nsew')

        self.equal = Button(text='=', width=4, command=self.calculate)
        self.buttons.append(self.equal)
        self.equal.grid(column=3, row=6, pady=3, padx=3, sticky='nsew')

        self.percent = Button(text='%', width=4, command=self.percentage)
        self.buttons.append(self.percent)
        self.percent.grid(column=4, row=6, pady=3, padx=3, sticky='nsew')

        self.sep = ttk.Separator(self.window, orient='horizontal')
        self.sep.grid(row=7, column=0, columnspan=5, sticky="ew", pady=5)

        self.x2 = Button(text='x²', width=4, command=lambda: self.power(2))
        self.buttons.append(self.x2)
        self.x2.grid(column=0, row=8, pady=3, padx=3, sticky='nsew')

        self.x3 = Button(text='x³', width=4, command=lambda: self.power(3))
        self.buttons.append(self.x3)
        self.x3.grid(column=1, row=8, pady=3, padx=3, sticky='nsew')

        self.xy = Button(text='xʸ', width=4, command=lambda: self.power())
        self.buttons.append(self.xy)
        self.xy.grid(column=2, row=8, pady=3, padx=3, sticky='nsew')

        self.sqrt_3 = Button(text='³√x', width=4, command=self.cube_root)
        self.buttons.append(self.sqrt_3)
        self.sqrt_3.grid(column=3, row=8, pady=3, padx=3, sticky='nsew')

        self.factorial = Button(text='n!', width=4, command=self.factor)
        self.buttons.append(self.factorial)
        self.factorial.grid(column=4, row=8, pady=3, padx=3, sticky='nsew')

        self.sinus = Button(text='sin', width=4, command=self.sin)
        self.buttons.append(self.sinus)
        self.sinus.grid(column=0, row=9, pady=3, padx=3, sticky='nsew')

        self.cosinus = Button(text='cos', width=4, command=self.cos)
        self.buttons.append(self.cosinus)
        self.cosinus.grid(column=1, row=9, pady=3, padx=3, sticky='nsew')

        self.tangens = Button(text='tan', width=4, command=self.tan)
        self.buttons.append(self.tangens)
        self.tangens.grid(column=2, row=9, pady=3, padx=3, sticky='nsew')

        self.l_parenthesis = Button(text='(', width=4, command=lambda: self.entry.insert(END, '('))
        self.buttons.append(self.l_parenthesis)
        self.l_parenthesis.grid(column=3, row=9, pady=3, padx=3, sticky='nsew')

        self.r_parenthesis = Button(text=')', width=4, command=lambda: self.entry.insert(END, ')'))
        self.buttons.append(self.r_parenthesis)
        self.r_parenthesis.grid(column=4, row=9, pady=3, padx=3, sticky='nsew')

        self.asinus = Button(text='sin⁻¹', width=4, command=self.asin)
        self.buttons.append(self.asinus)
        self.asinus.grid(column=0, row=10, pady=3, padx=3, sticky='nsew')

        self.acosinus = Button(text='cos⁻¹', width=4, command=self.acos)
        self.buttons.append(self.acosinus)
        self.acosinus.grid(column=1, row=10, pady=3, padx=3, sticky='nsew')

        self.atangens = Button(text='tan⁻¹', width=4, command=self.atan)
        self.buttons.append(self.atangens)
        self.atangens.grid(column=2, row=10, pady=3, padx=3, sticky='nsew')

        self.logarithm = Button(text='log', width=4, command=self.log)
        self.buttons.append(self.logarithm)
        self.logarithm.grid(column=3, row=10, pady=3, padx=3, sticky='nsew')

        self.natural_log = Button(text='ln', width=4, command=self.ln)
        self.buttons.append(self.natural_log)
        self.natural_log.grid(column=4, row=10, pady=3, padx=3, sticky='nsew')

        self.root_custom = Button(text='ⁿ√x', width=4, command=self.custom_root)
        self.buttons.append(self.root_custom)
        self.root_custom.grid(column=0, row=11, pady=3, padx=3, sticky='nsew')

        self.exp = Button(text="𝑒ˣ", width=4, command=self.exponential)
        self.buttons.append(self.exp)
        self.exp.grid(column=1, row=11, pady=3, padx=3, sticky='nsew')

        self.custom_log = Button(text='logb​(x)', width=4, command=self.custom_logarithm)
        self.buttons.append(self.custom_log)
        self.custom_log.grid(column=2, row=11, pady=3, padx=3, sticky='nsew')

        self.pi = Button(text='π', width=4, command=lambda: self.entry.insert(END, 'π'))
        self.buttons.append(self.pi)
        self.pi.grid(column=3, row=11, pady=3, padx=3, sticky='nsew')

        self.exit = Button(text='EXIT', width=4, bg='red', command=lambda: self.window.quit())
        self.exit.grid(column=4, row=11, pady=3, padx=3, sticky='nsew')

    def key_pressed(self, event):
        if event.char.isdigit():  # If the pressed key is number
            self.entry.insert(END, event.char)
        elif event.char in '+-/*().':
            self.entry.insert(END, event.char)
        elif event.keysym == 'Return':  # If enter is pressed
            self.calculate()
        elif event.keysym == 'Backspace':  # If backspace
            self.entry.delete(len(self.entry.get())-1, END)

    def get_entry_value(self):
        try:
            names = {'π': math.pi, 'e': math.e}
            value = simple_eval(self.entry.get(), names=names)
            return float(value)
        except Exception:
            raise ValueError

    def calculate(self):
        try:
            names = {'π': math.pi, 'e': math.e}

            result = simple_eval(self.entry.get(), names=names)
            formatted = f"{result:.10f}".rstrip('0').rstrip('.')
            self.entry.delete(0, END)
            self.entry.insert(END, str(formatted))
        except Exception:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')

    # Memory functions
    def memory_add(self):
        try:
            value = self.get_entry_value()
            self.memory += value
        except ValueError:
            pass

    def memory_subtract(self):
        try:
            value = self.get_entry_value()
            self.memory -= value
        except ValueError:
            pass

    def memory_recall(self):
        self.entry.insert(END, str(self.memory))

    def memory_clear(self):
        self.memory = 0

    # Scientific methods
    def square_root(self):
        try:
            value = self.get_entry_value()
            result = math.sqrt(value)
            formatted = f"{result:.10f}".rstrip('0').rstrip('.')
            self.entry.delete(0, END)
            self.entry.insert(END, str(formatted))
        except ValueError:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')

    def negative_num(self):
        try:
            value = self.get_entry_value()
            neg_value = -value
            self.entry.delete(0, END)
            self.entry.insert(END, str(neg_value))
        except ValueError:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')

    def delete_last_char(self):
        current_text = self.entry.get()
        if current_text:
            self.entry.delete(len(current_text) - 1)

    def delete_everything(self):
        self.entry.delete(0, END)

    def percentage(self):
        expression = self.entry.get()
        try:
            idx = max(expression.rfind(op) for op in '+-*/')
            if idx != -1:

                left = float(expression[:idx])
                right = float(expression[idx+1:].replace('%', ''))
                op = expression[idx]

                if op == '+':
                    result = left + (left * right / 100)
                elif op == '-':
                    result = left - (left * right / 100)
                elif op == '*':
                    result = left * (right / 100)
                elif op == '/':
                    result = left / (right / 100)

                self.entry.delete(0, END)
                self.entry.insert(END, str(result))
                return

            result = float(expression.replace('%', '')) / 100
            self.entry.delete(0, END)
            self.entry.insert(END, str(result))

        except Exception:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')

    def power(self, exp=None):
        try:
            base = self.get_entry_value()
            if exp is None:
                from tkinter import simpledialog
                exp = simpledialog.askfloat('Exponentation', 'Enter the exponent')

            if exp is not None:
                res = pow(base, exp)
                formatted = f"{res:.10f}".rstrip('0').rstrip('.')
                self.entry.delete(0, END)
                self.entry.insert(END, str(formatted))
        except ValueError:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Invalid expression')

    def cube_root(self):
        try:
            base = self.get_entry_value()
            res = -((-base) ** (1/3)) if base < 0 else base ** (1/3)
            formatted = f"{res:.10f}".rstrip('0').rstrip('.')
            self.entry.delete(0, END)
            self.entry.insert(END, str(formatted))
        except ValueError:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')

    def factor(self):
        try:
            value = self.entry.get()
            res = math.factorial(int(value))
            self.entry.delete(0, END)
            self.entry.insert(END, str(res))
        except ValueError:
            self.entry.delete(0, END)
            self.entry.insert(END, "Invalid (only whole numbers ≥ 0)")

    def sin(self):
        try:
            value = self.get_entry_value()
            radians = math.radians(value)  # convert degrees → radians
            result = math.sin(radians)
            formatted = f"{result:.10f}".rstrip('0').rstrip('.')
            self.entry.delete(0, END)
            self.entry.insert(END, str(formatted))
        except Exception:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')

    def cos(self):
        try:
            value = self.get_entry_value()
            radians = math.radians(value)
            res = math.cos(radians)
            formatted = f"{res:.10f}".rstrip('0').rstrip('.')
            self.entry.delete(0, END)
            self.entry.insert(END, str(formatted))
        except Exception:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')

    def tan(self):
        try:
            value = self.get_entry_value()
            radians = math.radians(value)
            res = math.tan(radians)
            formatted = f"{res:.10f}".rstrip('0').rstrip('.')
            self.entry.delete(0, END)
            self.entry.insert(END, str(formatted))
        except Exception:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')

    def asin(self):
        try:
            value = self.get_entry_value()
            res = math.degrees(math.asin(value))  # radians → degrees
            formatted = f"{res:.10f}".rstrip('0').rstrip('.')
            self.entry.delete(0, END)
            self.entry.insert(END, formatted)
        except Exception:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')

    def acos(self):
        try:
            value = self.get_entry_value()
            res = math.degrees(math.acos(value))  # radians → degrees
            formatted = f"{res:.10f}".rstrip('0').rstrip('.')
            self.entry.delete(0, END)
            self.entry.insert(END, formatted)
        except Exception:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')

    def atan(self):
        try:
            value = self.get_entry_value()
            res = math.degrees(math.atan(value))  # radians → degrees
            formatted = f"{res:.10f}".rstrip('0').rstrip('.')
            self.entry.delete(0, END)
            self.entry.insert(END, formatted)
        except Exception:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')

    def log(self):
        try:
            value = self.get_entry_value()
            res = math.log10(value)
            formatted = f"{res:.10f}".rstrip('0').rstrip('.')
            self.entry.delete(0, END)
            self.entry.insert(END, formatted)

        except Exception:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')

    def ln(self):
        try:
            value = self.get_entry_value()
            res = math.log(value)
            formatted = f"{res:.10f}".rstrip('0').rstrip('.')
            self.entry.delete(0, END)
            self.entry.insert(END, formatted)

        except Exception:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')

    def custom_root(self, degree=None):
        try:
            base = self.get_entry_value()
            if degree is None:
                from tkinter import simpledialog
                degree = simpledialog.askfloat('Degree', 'Enter the degree: ')
            if degree is not None:
                res = base ** (1/degree)
                formatted = f"{res:.10f}".rstrip('0').rstrip('.')
                self.entry.delete(0, END)
                self.entry.insert(END, str(formatted))
        except Exception:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')

    def exponential(self, degree=None):
        try:
            if degree is None:
                from tkinter import simpledialog
                degree = simpledialog.askfloat('Degree', 'Enter the degree: ')
            res = math.exp(degree)
            formatted = f"{res:.10f}".rstrip('0').rstrip('.')
            self.entry.delete(0, END)
            self.entry.insert(END, str(formatted))
        except Exception:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')

    def custom_logarithm(self, base=None, argument=None):
        try:
            if base is None and argument is None:
                from tkinter import simpledialog
                base = simpledialog.askfloat('Base', 'Enter the base number: ')
                argument = simpledialog.askfloat('Argument', 'Enter the number you are taking the log of: ')
            res = math.log(argument, base)
            formatted = f"{res:.10f}".rstrip('0').rstrip('.')
            self.entry.delete(0, END)
            self.entry.insert(END, str(formatted))
        except Exception:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')

    def theme(self, *args):
        choice = self.theme_choice.get()
        if choice == 'Light':
            self.theme_choice.set('Light')
            self.window.configure(bg='#F0F0F0')  # Darker white color
            self.entry.configure(bg='white', fg='black')
            for button in self.buttons:
                button.configure(bg='#F0F0F0', fg='black')
        elif choice == 'Dark':
            self.theme_choice.set('Dark')
            self.window.configure(bg='black')
            self.entry.configure(bg='black', fg='white')
            for button in self.buttons:
                button.configure(bg='black', fg='white')
        elif choice == 'Dark blue':
            self.theme_choice.set('Dark blue')
            self.window.configure(bg="#0A1D37")  # Dark blue color
            self.entry.configure(bg="#0A1D37", fg='white')
            for button in self.buttons:
                button.configure(bg="#0A1D37", fg='white')


calc = Calculator()
calc.window.mainloop()



