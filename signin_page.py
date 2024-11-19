import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")

class SignInPage(ctk.CTk):
    def __init__(app):
        super().__init__()

        app.geometry("370x670")
        app.title("Sign In")

        # Title Label
        title_label = ctk.CTkLabel(app, text="Welcome to ASU Fitness App", font=("Arial", 24))
        title_label.pack(pady=20)

        # Username Label and Entry
        username_label = ctk.CTkLabel(app, text="Enter your name", font=("Arial", 18))
        username_label.pack(pady=10)

        app.username_entry = ctk.CTkEntry(app, font=("Arial", 16), width=300)
        app.username_entry.pack(pady=10)

        # Email Label and Entry
        email_label = ctk.CTkLabel(app, text="Email", font=("Arial", 18))
        email_label.pack(pady=10)

        app.email_entry = ctk.CTkEntry(app, font=("Arial", 16), width=300)
        app.email_entry.pack(pady=10)

        # Password Label and Entry (Optional)
        password_label = ctk.CTkLabel(app, text="Password", font=("Arial", 18))
        password_label.pack(pady=10)

        app.password_entry = ctk.CTkEntry(app, font=("Arial", 16), width=300, show="*")
        app.password_entry.pack(pady=10)

        # Sign-In Button
        sign_in_button = ctk.CTkButton(
            app, text="Sign In", command=app.sign_in, font=("Arial", 16), fg_color="gold", text_color="black"
        )
        sign_in_button.pack(pady=20)

    def sign_in(app):
        """Handle sign-in logic."""
        username = app.username_entry.get().strip()

        if not username:
            messagebox.showerror("Error", "Please enter your username!")
            return

        # Simulate successful login
        app.destroy()  # Close the SignInPage

app = SignInPage()
app.mainloop()
