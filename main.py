import customtkinter as ctk
from tkinter import messagebox
from timer import start_timer, update_timer, stop_timer
from leaderboard import save_workout
from signin_page import SignInPage

ctk.set_appearance_mode("dark")

name = "Joe Schmo"

class App(ctk.CTk):
    def __init__(app):
        super().__init__()

        app.geometry("370x670")
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
        home_button = ctk.CTkButton(
            self.nav_bar,
            text="History",
            height=55,
            fg_color="#800000",
            hover_color="#990000",
            command=lambda: self.show_frame(HistoryPage),
        )
        home_button.pack(side="left", fill="both", expand=True)

        settings_button = ctk.CTkButton(
            self.nav_bar,
            text="New Workout",
            height=55,
            fg_color="#800000",
            hover_color="#990000",
            command=lambda: self.show_frame(HomePage),
        )
        settings_button.pack(side="left", fill="both", expand=True)

        profile_button = ctk.CTkButton(
            self.nav_bar,
            text="Leaderboards",
            height=55,
            fg_color="#800000",
            hover_color="#990000",
            command=lambda: self.show_frame(LeadboardPage),
        )
        profile_button.pack(side="left", fill="both", expand=True)

    def show_frame(self, page_class):
        """Raise the frame to the top for the specified page."""
        frame = self.pages[page_class]
        frame.tkraise()


class HomePage(ctk.CTkFrame):
    def __init__(app, parent, controller):
        super().__init__(parent)

        # Add widgets for the Home Page
        label = ctk.CTkLabel(app, text=f" Good Afternoon {name}", font=("Arial", 24))
        label.pack(pady=20)

        # Timer variables
        app.timer_running = False
        app.time_elapsed = 0

        app.timer_label = ctk.CTkLabel(app, text="0:00:00:00", font=("Arial", 24))
        app.timer_label.pack(pady=20)

        # Button to start the timer
        app.start_button = ctk.CTkButton(
            app,
            text="Start a New Workout",
            command=lambda: start_timer(app),
            fg_color="gold",
            text_color="black",
        )
        app.start_button.pack(pady=10)

        # Pass the controller to finish_workout
        app.stop_button = ctk.CTkButton(
            app,
            text="Finish Workout",
            fg_color="maroon",
            command=lambda: finish_workout(app, controller),
        )
        app.stop_button.pack(pady=10)

        label1 = ctk.CTkLabel(app, text="My Templates", font=("Arial", 24), pady=50)
        label1.pack(pady=5, padx=10)

        text_2 = ctk.CTkTextbox(app, width=350, height=125, font=("Arial", 18))
        text_2.pack(pady=10, padx=10)
        text_2.insert("end", "Strong A 5x5:  \n\n")
        text_2.insert("end", "Squat              5x5\nBench Press   5x5\nBarbell Row    5x5")

        text_3 = ctk.CTkTextbox(app, width=350, height=150, font=("Arial", 18))
        text_3.pack(pady=10, padx=10)
        text_3.insert("end", "Leg Day:  \n\n")
        text_3.insert("end", "Power Clean        3x2\nSquat                   3x5\nFront Squat          3x8\nRDLs                    3x12")

    def update_timer(app):
        update_timer(app)  # Call the imported update_timer function


def show_congratulations():
    messagebox.showinfo("Workout Finished", "Congratulations🎉!\n")


def finish_workout(app, controller):
    """Stop the timer, show the congratulations message, and refresh the leaderboards."""
    stop_timer(app)
    show_congratulations()
    save_workout(name, app)

    # Refresh the LeaderboardsPage
    controller.pages[LeadboardPage].refresh()


class LeadboardPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = ctk.CTkLabel(self, text="Current Leaders", font=("Arial", 24), pady=50)
        label.pack(pady=10, padx=10)

        self.text_1 = ctk.CTkTextbox(self, width=350, height=200, font=("Arial", 18))
        self.text_1.pack(pady=10, padx=10)
        self.text_1.insert("0.0", "Total Hours:  \n\n")

        self.text_1.insert("end", "1. Hugh Mongus      Time: 4:52:12\n")
        self.text_1.insert("end", "2. Bozo                    Time: 2:12:02\n")
        self.text_1.insert("end", "3. Joe King              Time: 1:12:25\n")
        self.text_1.insert("end", "4. Bhris Da Jit          Time: 2:01:07\n")
        self.text_1.insert("end", "5. Chris P. Bacon    Time: 1:58:25\n")

        text_4 = ctk.CTkTextbox(self, width=350, height=75, font=("Arial", 18))
        text_4.pack(pady=10, padx=10)
        text_4.insert("0.0", "Total Calories:")

        text_5 = ctk.CTkTextbox(self, width=350, height=75, font=("Arial", 18))
        text_5.pack(pady=10, padx=10)
        text_5.insert("0.0", "Classes Attended:")

        text_6 = ctk.CTkTextbox(self, width=350, height=75, font=("Arial", 18))
        text_6.pack(pady=10, padx=10)
        text_6.insert("0.0", "Stairs Climbed:")

        self.refresh()

    def refresh(self):
        """Refresh the leaderboard by reading the updated workout log."""
        self.text_1.delete("1.0", "end")  # Clear previous text
        self.text_1.insert("0.0", "Total Hours:  \n\n")

        # Read the workout log file and insert its content into the textbox
        try:
            with open("workout_log.txt", "r") as file:
                log_contents = file.read()

            if log_contents.strip():
                self.text_1.insert("end", log_contents)  # Add workout log at the end
            else:
                self.text_1.insert("end", "No workout records found.")
        except FileNotFoundError:
            self.text_1.insert("end", "Workout log file not found.")

class HistoryPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ctk.CTkLabel(self, text="History", font=("Arial", 24))
        label.pack(pady=20)

        label1 = ctk.CTkLabel(self, text="No Previous Workouts\n Start a new workout to show up", font=("Arial", 16))
        label1.pack(pady=10, padx=10)

# Run the application
if __name__ == "__main__":
    sign_in_page = SignInPage()
    app = App()
    app.mainloop()
