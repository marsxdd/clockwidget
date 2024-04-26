#12 hour format with gif

import tkinter as tk
from PIL import ImageTk, Image
from datetime import datetime, timedelta

class DesktopWidget(tk.Tk):
def __init__(self):
super().__init__()

self.overrideredirect(True) # no window decorations
self.geometry('200x100') # set window size

# Load the GIF image
self.gif_frames = []
gif = Image.open("background.gif")
gif.info['loop'] = 0 # set loop to 0 for infinite loop
self.load_gif_frames(gif)

# Create a label to hold the background image
self.background_label = tk.Label(self)
self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

self.label = tk.Label(self, font=('calibri', 16, 'bold'), background='black', foreground='yellow')
self.label.place(relx=0.5, rely=0.5, anchor='center')

self.current_frame = 0
self.update_background()
self.update_clock()

def load_gif_frames(self, gif):
try:
while True:
self.gif_frames.append(ImageTk.PhotoImage(gif))
gif.seek(gif.tell() + 1)
except EOFError:
pass

def update_background(self):
self.background_label.config(image=self.gif_frames[self.current_frame])
self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
self.after(100, self.update_background) # Update every 100 milliseconds

def update_clock(self):
# UTC
current_time_utc = datetime.utcnow()

# Convert to Atlantic Time Zone
atlantic_time = current_time_utc - timedelta(hours=4)

# Determine if it's AM or PM
am_pm = "AM" if atlantic_time.hour < 12 else "PM"

# Convert to 12-hour clock format
hour_12 = atlantic_time.hour % 12
if hour_12 == 0:
hour_12 = 12 # 12:00 AM instead of 0:00 AM

# Format the time as desired
time_str = "{:02d}:{:02d}:{:02d} {}".format(hour_12, atlantic_time.minute, atlantic_time.second, am_pm)

# Date string format
current_date = atlantic_time.strftime('%Y-%m-%d')

# Combine time and date
display_text = f" {time_str}\n {current_date}"

self.label.config(text=display_text)

# Schedule the next update in 1 second
self.after(1000, self.update_clock)

if __name__ == "__main__":
widget = DesktopWidget()
widget.mainloop()
