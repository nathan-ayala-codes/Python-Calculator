import tkinter as tk
import re


class Calculator:
    def __init__(self) -> None:
        self.num1 = None
        self.num2 = None
        self.output = None

    def addition(self) -> None:
        self.output = self.num1 + self.num2

    def subtraction(self) -> None:
        self.output = self.num1 - self.num2

    def multiplication(self) -> None:
        self.output = self.num1 * self.num2

    def division(self) -> None:
        if self.num2 == 0:
            raise ZeroDivisionError
        self.output = self.num1 / self.num2


class CalculatorApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Nathan's Calculator")
        self.root.resizable(False, False)
        self.root.configure(bg="#0f1b2d")

        self.C1 = Calculator()
        self.expression = tk.StringVar()

        self._build_ui()

    def _build_ui(self):
        # --- Display ---
        display_frame = tk.Frame(self.root, bg="#0f1b2d", padx=10, pady=10)
        display_frame.pack(fill="x")

        self.display = tk.Entry(
            display_frame,
            textvariable=self.expression,
            font=("Courier New", 24),
            bg="#1a2e45",
            fg="#e8f4fd",
            insertbackground="#7eb8e8",
            relief="flat",
            justify="right",
            bd=8,
        )
        self.display.pack(fill="x")
        self.display.bind("<Return>", lambda e: self.evaluate())
        self.display.focus()

        # --- Buttons ---
        button_frame = tk.Frame(self.root, bg="#0f1b2d", padx=10, pady=5)
        button_frame.pack()

        # Layout: each tuple is (label, row, col, style)
        buttons = [
            ("C",  0, 0, "clear"),   ("ANS", 0, 1, "special"), ("%",  0, 2, "op"), ("/", 0, 3, "op"),
            ("7",  1, 0, "num"),     ("8",   1, 1, "num"),      ("9",  1, 2, "num"), ("*", 1, 3, "op"),
            ("4",  2, 0, "num"),     ("5",   2, 1, "num"),      ("6",  2, 2, "num"), ("-", 2, 3, "op"),
            ("1",  3, 0, "num"),     ("2",   3, 1, "num"),      ("3",  3, 2, "num"), ("+", 3, 3, "op"),
            ("0",  4, 0, "num"),     (".",   4, 1, "num"),      ("⌫", 4, 2, "special"), ("=", 4, 3, "eq"),
        ]

        styles = {
            "num":     {"bg": "#1e3a5f", "fg": "#e8f4fd", "activebackground": "#2a4f7f"},
            "op":      {"bg": "#2e6da4", "fg": "#ffffff", "activebackground": "#3a85c4"},
            "eq":      {"bg": "#1a6bbd", "fg": "#ffffff", "activebackground": "#2280d8"},
            "clear":   {"bg": "#8b1a1a", "fg": "#ffcccc", "activebackground": "#b02020"},
            "special": {"bg": "#1a3550", "fg": "#a0c8e8", "activebackground": "#254a6e"},
        }

        for (label, row, col, style) in buttons:
            s = styles[style]
            btn = tk.Label(
                button_frame,
                text=label,
                font=("Courier New", 18, "bold"),
                width=4,
                height=2,
                relief="flat",
                cursor="hand2",
                bg=s["bg"],
                fg=s["fg"],
            )
            btn.grid(row=row, column=col, padx=4, pady=4)

            # Bind click and hover manually since Labels have no command
            btn.bind("<Button-1>", lambda e, l=label: self._on_button(l))
            btn.bind("<Enter>", lambda e, b=btn, s=s: b.config(bg=s["activebackground"]))
            btn.bind("<Leave>", lambda e, b=btn, s=s: b.config(bg=s["bg"]))

        # --- Status label ---
        self.status = tk.Label(
            self.root,
            text="Type an expression or use buttons",
            font=("Courier New", 10),
            bg="#0f1b2d",
            fg="#5a8ab0",
        )
        self.status.pack(pady=(0, 8))

    def _on_button(self, label: str):
        if label == "=":
            self.evaluate()
        elif label == "C":
            self.expression.set("")
            self.status.config(text="Cleared", fg="#5a8ab0")
        elif label == "⌫":
            current = self.expression.get()
            self.expression.set(current[:-1])
        elif label == "ANS":
            if self.C1.output is not None:
                current = self.expression.get()
                ans = int(self.C1.output) if self.C1.output == int(self.C1.output) else self.C1.output
                self.expression.set(current + str(ans))
            else:
                self.status.config(text="No previous answer yet", fg="#e05555")
        else:
            current = self.expression.get()
            self.expression.set(current + label)

    def evaluate(self):
        expression = self.expression.get().strip()

        if not expression:
            return

        try:
            parts = [p.strip() for p in re.split(r'(\+|-|\*|/|%)', expression) if p.strip()]

            if len(parts) != 3:
                raise ValueError("Need exactly two numbers and one operator.")

            self.C1.num1 = float(parts[0])
            operator = parts[1]
            self.C1.num2 = float(parts[2])

            if operator == "+":
                self.C1.addition()
            elif operator == "-":
                self.C1.subtraction()
            elif operator == "*":
                self.C1.multiplication()
            elif operator == "/":
                self.C1.division()
            elif operator == "%":
                self.C1.output = self.C1.num1 % self.C1.num2
            else:
                raise ValueError(f"Unknown operator: {operator}")

            result = self.C1.output
            display_result = int(result) if result == int(result) else result

            self.expression.set(str(display_result))
            self.status.config(text=f"{parts[0]} {operator} {parts[2]} = {display_result}", fg="#4ec9f0")

        except ZeroDivisionError:
            self.status.config(text="Error: Cannot divide by zero", fg="#e05555")
            self.expression.set("")
        except ValueError:
            self.status.config(text="Invalid expression. Try: 3 + 4", fg="#e05555")
            self.expression.set("")
