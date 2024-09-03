
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ATM:
    def __init__(self, root):
        self.pin = ""
        self.balance = 0

        # Main window setup
        self.root = root
        self.root.title("ATM")
        self.root.geometry("700x600")
        self.root.resizable(False,False)
        self.root.config(bg="#f0f0f0")  # Light gray background color for the main window

        # Load images with error handling
        try:
            self.pin_image = ImageTk.PhotoImage(Image.open("key.png").resize((50, 50)))
            self.change_pin_image = ImageTk.PhotoImage(Image.open("key.png").resize((50, 50)))
            self.balance_image = ImageTk.PhotoImage(Image.open("money.png").resize((50, 50)))
            self.withdraw_image = ImageTk.PhotoImage(Image.open("withdrow.png").resize((50, 50)))
            self.exit_image = ImageTk.PhotoImage(Image.open("exit.png").resize((50, 50)))
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"Image file not found: {e}")
            self.root.destroy()  # Close the application if images are not found
            return

        # Menu frame setup
        self.menu_frame = tk.Frame(root, bg="#f0f0f0")  # Match the background color
        self.menu_frame.pack(pady=20)

        # Menu buttons with images
        tk.Button(self.menu_frame, text="1: Generate PIN", image=self.pin_image, compound="left", command=self.pin_generator, bg="#ffffff", fg="#333333").pack(pady=5)
        tk.Button(self.menu_frame, text="2: Change PIN", image=self.change_pin_image, compound="left", command=self.pin_changer, bg="#ffffff", fg="#333333").pack(pady=5)
        tk.Button(self.menu_frame, text="3: Balance Inquiry", image=self.balance_image, compound="left", command=self.balance_inquiry, bg="#ffffff", fg="#333333").pack(pady=5)
        tk.Button(self.menu_frame, text="4: Withdraw", image=self.withdraw_image, compound="left", command=self.withdraw, bg="#ffffff", fg="#333333").pack(pady=5)
        tk.Button(self.menu_frame, text="5: Exit", image=self.exit_image, compound="left", command=root.quit, bg="#ffffff", fg="#333333").pack(pady=5)

    def pin_generator(self):
        # Window for generating a new PIN
        new_window = tk.Toplevel(self.root)
        new_window.title("Generate PIN")
        new_window.geometry("400x300")
        new_window.resizable(False,False)
        new_window.config(bg="#f0f0f0")

        # Input fields and labels
        tk.Label(new_window, text="Enter new PIN:", bg="#f0f0f0").pack(pady=5)
        new_pin_entry = tk.Entry(new_window, show="*")
        new_pin_entry.pack(pady=5)

        tk.Label(new_window, text="Enter initial deposit:", bg="#f0f0f0").pack(pady=5)
        balance_entry = tk.Entry(new_window)
        balance_entry.pack(pady=5)

        def submit():
            # Handling PIN generation and balance setup
            try:
                self.pin = new_pin_entry.get()
                self.balance = int(balance_entry.get())
                messagebox.showinfo("Success", "PIN generated and balance set.")
                new_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for the balance.")

        tk.Button(new_window, text="Submit", command=submit, bg="#4CAF50", fg="#ffffff").pack(pady=5)

    def pin_changer(self):
        # Window for changing the PIN
        new_window = tk.Toplevel(self.root)
        new_window.title("Change PIN")
        new_window.geometry("400x300")
        new_window.resizable(False,False)

        new_window.config(bg="#f0f0f0")

        # Input fields and labels
        tk.Label(new_window, text="Enter old PIN:", bg="#f0f0f0").pack(pady=5)
        old_pin_entry = tk.Entry(new_window, show="*")
        old_pin_entry.pack(pady=5)

        tk.Label(new_window, text="Enter new PIN:", bg="#f0f0f0").pack(pady=5)
        new_pin_entry = tk.Entry(new_window, show="*")
        new_pin_entry.pack(pady=5)

        def submit():
            # Handling PIN change
            if old_pin_entry.get() == self.pin:
                self.pin = new_pin_entry.get()
                messagebox.showinfo("Success", "PIN successfully changed.")
                new_window.destroy()
            else:
                messagebox.showerror("Error", "Incorrect old PIN.")

        tk.Button(new_window, text="Submit", command=submit, bg="#2196F3", fg="#ffffff").pack(pady=5)

    def balance_inquiry(self):
        # Displaying the balance
        messagebox.showinfo("Balance Inquiry", f"Your bank balance is: {self.balance}")

    def withdraw(self):
        # Window for withdrawing money
        new_window = tk.Toplevel(self.root)
        new_window.title("Withdraw")
        new_window.geometry("400x300")
        new_window.resizable(False,False)
        new_window.config(bg="#f0f0f0")

        # Input fields and labels
        tk.Label(new_window, text="Enter PIN:", bg="#f0f0f0").pack(pady=5)
        pin_entry = tk.Entry(new_window, show="*")
        pin_entry.pack(pady=5)

        tk.Label(new_window, text="Enter amount to withdraw:", bg="#f0f0f0").pack(pady=5)
        amount_entry = tk.Entry(new_window)
        amount_entry.pack(pady=5)

        def submit():
            # Handling the withdrawal process
            try:
                if pin_entry.get() == self.pin:
                    withdrawal_amount = int(amount_entry.get())
                    if withdrawal_amount <= self.balance:
                        self.balance -= withdrawal_amount
                        messagebox.showinfo("Success", f"Withdrawal successful. New balance: {self.balance}")
                        new_window.destroy()
                    else:
                        messagebox.showerror("Error", "Insufficient balance.")
                else:
                    messagebox.showerror("Error", "Incorrect PIN.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for the withdrawal amount.")

        tk.Button(new_window, text="Submit", command=submit, bg="#f44336", fg="#ffffff").pack(pady=5)

# Create the main window
root = tk.Tk()
atm = ATM(root)
root.mainloop()
