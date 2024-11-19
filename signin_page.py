import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")

class SignInPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("370x675")
        self.title("Sign In")

        # Title Label
        title_label = ctk.CTkLabel(self, text="Welcome to ASU Fitness App", font=("Arial", 24))
        title_label.pack(pady=20)

        # Username Label and Entry
        username_label = ctk.CTkLabel(self, text="Enter your name", font=("Arial", 18))
        username_label.pack(pady=10)

        self.username_entry = ctk.CTkEntry(self, font=("Arial", 16), width=300)
        self.username_entry.pack(pady=10)

        # Email Label and Entry
        email_label = ctk.CTkLabel(self, text="Email", font=("Arial", 18))
        email_label.pack(pady=10)

        self.email_entry = ctk.CTkEntry(self, font=("Arial", 16), width=300)
        self.email_entry.pack(pady=10)

        # Password Label and Entry (Optional)
        password_label = ctk.CTkLabel(self, text="Password", font=("Arial", 18))
        password_label.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self, font=("Arial", 16), width=300, show="*")
        self.password_entry.pack(pady=10)

        # Sign-In Button
        sign_in_button = ctk.CTkButton(
            self, text="Sign In", command=self.sign_in, font=("Arial", 16), fg_color="gold", text_color="black"
        )
        sign_in_button.pack(pady=20)

    def sign_in(self):
        """Handle sign-in logic."""
        username = self.username_entry.get().strip()

        if not username:
            messagebox.showerror("Error", "Please enter your username!")
            return

        # Simulate successful login
        self.destroy()  # Close the SignInPage
        app = App(username)  # Pass the username to the main app
        app.mainloop()
