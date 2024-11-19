import customtkinter as ctk

def save_workout(name, self):
    """Save user information to a file after the workout is completed."""
    total_time = self.time_elapsed  # Time elapsed in seconds
    hours, remaining_seconds = divmod(int(total_time), 3600)
    minutes, seconds = divmod(remaining_seconds, 60)
    formatted_time = f"{hours}:{minutes:02d}:{seconds:02d}"
    
    # Save the data to a file
    with open("workout_log.txt", "a") as file:
        file.write(f"6. {name}    Time: {formatted_time}\n")

