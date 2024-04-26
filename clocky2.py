#24 hour format with GIf + Time: / Date:

import tkinter as tk
from PIL import ImageTk, Image
import time
from datetime import datetime, timedelta

class DesktopWidget(tk.Tk):
def __init__(self):
super().__init__()

self.overrideredirect(True) # no window decorations
self.geometry('200x100') # Set window size

# Load the GIF image
self.gif_frames = []
gif = Image.open("background.gif")
gif.info['loop'] = 0 # Set loop to 0 for infinite loop
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

# Convert to Atlantic Time Zone (UTC-4)
atlantic_time = current_time_utc - timedelta(hours=4)

# Time string format
current_time = atlantic_time.strftime('%H:%M:%S')

# Date string format
current_date = atlantic_time.strftime('%Y-%m-%d')

# Combine time and date
display_text = f"Time: {current_time}\nDate: {current_date}"

self.label.config(text=display_text)

self.after(1000, self.update_clock) # Update every second

if __name__ == "__main__":
widget = DesktopWidget()
widget.mainloop()
