import customtkinter as ctk
from timer import start_timer, update_timer 

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(app):
        super().__init__()

        app.geometry("400x675")
        app.title("ASU Fitness App")

        # Create a container frame to stack the pages 
        container = ctk.CTkFrame(app)
        container.pack(fill="both", expand=True)

        # Create the navigation bar at the bottom
        app.nav_bar = ctk.CTkFrame(app, height=55, corner_radius=0, fg_color="#800000")
        app.nav_bar.pack(fill="x", side="bottom")

        # Dictionary to hold the pages
        app.pages = {}

        # Initialize the pages and store them in the dictionary
        for Page in (HomePage, LeadboardPage, HistoryPage):
            page = Page(container, app)
            app.pages[Page] = page
            page.grid(row=0, column=0, sticky="nsew")

        # Show the initial page
        app.show_frame(HomePage)

        # Add navigation buttons to the nav bar
        app.create_nav_buttons()

    def create_nav_buttons(self):
        """Create navigation buttons for the bottom navigation bar."""
        home_button = ctk.CTkButton(self.nav_bar, text="History", height=55, fg_color="#800000", hover_color="#990000",
                                    command=lambda: self.show_frame(HistoryPage))
        home_button.pack(side="left", fill="both", expand=True)

        settings_button = ctk.CTkButton(self.nav_bar, text="Add New New Workout", height=55, fg_color="#800000", hover_color="#990000",
                                        command=lambda: self.show_frame(HomePage))
        settings_button.pack(side="left", fill="both", expand=True)

        profile_button = ctk.CTkButton(self.nav_bar, text="Leaderboards", height=55, fg_color="#800000", hover_color="#990000",
                                       command=lambda: self.show_frame(LeadboardPage))
        profile_button.pack(side="left", fill="both", expand=True)

    def show_frame(self, page_class):
        """Raise the frame to the top for the specified page."""
        frame = self.pages[page_class]
        frame.tkraise()


# ===================================================================================
class HomePage(ctk.CTkFrame):
    def __init__(app, parent, controller):
        super().__init__(parent)

        # Add widgets for the Home Page
        label = ctk.CTkLabel(app, text=" Workout", font=("Arial", 24) )
        label.pack(pady=20)

        # Timer variables
        app.timer_running = False
        app.time_elapsed = 0

        app.timer_label = ctk.CTkLabel(app, text="0:00", font=("Arial", 24))
        app.timer_label.pack(pady=20)

        # Button to start the timer
        app.start_button = ctk.CTkButton(app, text="Start a New Workout", command=lambda: start_timer(app), fg_color="gold", text_color="black")
        app.start_button.pack(pady=10)

        app.stop_button = ctk.CTkButton(app, text="Finish Workout", fg_color="maroon")
        app.stop_button.pack(pady=10)

    def update_timer(app):
        update_timer(app)  # Call the imported update_timer function
    

        
# =====================================================================================
class LeadboardPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Add widgets for the Settings Page
        label = ctk.CTkLabel(self, text="Settings Page", font=("Arial", 24), justify=ctk.CENTER)
        label.pack(pady=20)        

# =====================================================================================
class HistoryPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Add widgets for the Settings Page
        label = ctk.CTkLabel(self, text="Settings Page", font=("Arial", 24))
        label.pack(pady=20)

# Run the application
if __name__ == "__main__":
    app = App()
    app.mainloop()