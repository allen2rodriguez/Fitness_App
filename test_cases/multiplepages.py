import customtkinter as ctk

# Set the theme and appearance mode
ctk.set_appearance_mode("dark")  # "light" or "dark"
ctk.set_default_color_theme("blue")  # color theme


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure the main window
        self.title("CustomTkinter Multi-Page Example with Navigation")
        self.geometry("600x400")

        # Create a container frame to stack the pages
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        # Create the navigation bar at the bottom
        self.nav_bar = ctk.CTkFrame(self, height=50, corner_radius=0)
        self.nav_bar.pack(fill="x", side="bottom")

        # Dictionary to hold the pages
        self.pages = {}

        # Initialize the pages and store them in the dictionary
        for Page in (HomePage, SettingsPage, ProfilePage):
            page = Page(self.container, self)
            self.pages[Page] = page
            page.grid(row=0, column=0, sticky="nsew")

        # Show the initial page
        self.show_frame(HomePage)

        # Add navigation buttons to the nav bar
        self.create_nav_buttons()

    def create_nav_buttons(self):
        """Create navigation buttons for the bottom navigation bar."""
        home_button = ctk.CTkButton(self.nav_bar, text="Home",
                                    command=lambda: self.show_frame(HomePage))
        home_button.pack(side="left", fill="both", expand=True)

        settings_button = ctk.CTkButton(self.nav_bar, text="Settings",
                                        command=lambda: self.show_frame(SettingsPage))
        settings_button.pack(side="left", fill="both", expand=True)

        profile_button = ctk.CTkButton(self.nav_bar, text="Profile",
                                       command=lambda: self.show_frame(ProfilePage))
        profile_button.pack(side="left", fill="both", expand=True)

    def show_frame(self, page_class):
        """Raise the frame to the top for the specified page."""
        frame = self.pages[page_class]
        frame.tkraise()


# Define each page as a separate frame
class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Add widgets for the Home Page
        label = ctk.CTkLabel(self, text="Home Page", font=("Arial", 24))
        label.pack(pady=20)


class SettingsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Add widgets for the Settings Page
        label = ctk.CTkLabel(self, text="Settings Page", font=("Arial", 24))
        label.pack(pady=20)


class ProfilePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Add widgets for the Profile Page
        label = ctk.CTkLabel(self, text="Profile Page", font=("Arial", 24))
        label.pack(pady=20)


# Run the application
if __name__ == "__main__":
    app = App()
    app.mainloop()
