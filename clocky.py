import tkinter as tk
import time
from datetime import datetime, timedelta


class DesktopWidget(tk.Tk):
    def __init__(self):
        super().__init__()

        self.overrideredirect(True)  # no window dec
        self.geometry('200x100')  # Set window size

        self.label = tk.Label(self, font=('calibri', 16, 'bold'), background='black', foreground='yellow')
        self.label.pack(expand=True, fill='both')

        self.update_clock()

    def update_clock(self):
        # UTC
        current_time_utc = datetime.utcnow()

        # Convert to Atlantic Time Zone (UTC-4)
        atlantic_time = current_time_utc - timedelta(hours=4)

        # Time string format
        current_time = atlantic_time.strftime('%H:%M:%S')

        # Date string format
        current_date = atlantic_time.strftime('%Y-%m-%d')

        # Combine time and date
        print ("I'M A CLOCK, YIPPIE");
        display_text = f"Time: {current_time}\nDate: {current_date}"

        self.label.config(text=display_text)

        self.after(1000, self.update_clock)  # Update every second


if __name__ == "__main__":
    widget = DesktopWidget()
    widget.mainloop()
