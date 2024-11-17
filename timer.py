# timer_module.py

def start_timer(self):
    """Start the timer when the button is clicked."""
    if not self.timer_running:
        self.timer_running = True
        self.update_timer()

def update_timer(self):
    """Update the timer every second."""
    if self.timer_running:
        self.time_elapsed += 1
        minutes, seconds = divmod(self.time_elapsed, 60)
        self.timer_label.configure(text=f"{minutes}:{seconds:02d}")
        # Schedule the next update after 1000 ms (1 second)
        self.after(1000, self.update_timer)
