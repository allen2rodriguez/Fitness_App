# timer_module.py

def start_timer(self):
    """Start the timer when the button is clicked."""
    if not self.timer_running:
        self.timer_running = True
        self.update_timer()

def update_timer(self):
    """Update the timer every 10 milliseconds."""
    if self.timer_running:
        self.time_elapsed += 0.01  # Increment time by 10 ms
        total_seconds = int(self.time_elapsed)
        milliseconds = int((self.time_elapsed - total_seconds) * 1000) // 10  # Convert to 2 digits
        hours, remaining_seconds = divmod(total_seconds, 3600)  # Calculate hours and remaining seconds
        minutes, seconds = divmod(remaining_seconds, 60)  # Calculate minutes and seconds
        self.timer_label.configure(text=f"{hours}:{minutes:02d}:{seconds:02d}:{milliseconds:02d}")
        # Schedule the next update after 10 ms
        self.after(10, self.update_timer)


def stop_timer(self):
    self.timer_running = False
    hours, minutes, seconds, milliseconds = 0, 0, 0, 0
    self.timer_label.configure(text=f"{hours}:{minutes:02d}:{seconds:02d}:{milliseconds:02d}")
