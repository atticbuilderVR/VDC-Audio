import tkinter as tk
from tkinter import messagebox as msg
from tkinter import filedialog as fd
import pygame
import webbrowser

# Main application window
app = tk.Tk()
app.title("VDC Audio Player")
app.geometry("300x300")

# Initialize global name variable
name = "User"

# Show notice message
msg.showinfo("NOTICE", "As of 1.04.2025, your VDC Files will no longer save.")

# Function to open the name entry window
def open_name_entry():
    def submit_name():
        global name
        name = text.get()
        nameapp.destroy()  # Close the name entry window
        update_greeting()  # Update the greeting in the main window

    # Create a new Toplevel window for name entry
    nameapp = tk.Toplevel(app)
    nameapp.title("Enter your name")
    nameapp.geometry("300x100")
    nameapp.resizable(False, False)

    # Add widgets to the name entry window
    title = tk.Label(nameapp, text="Enter your name", font=("Arial", 14))
    title.pack()

    text = tk.Entry(nameapp, font=("Arial", 10), width=20)
    text.pack()

    submit = tk.Button(nameapp, text="SUBMIT", font=("Arial", 10), bg="green", fg="white", command=submit_name)
    submit.pack()

# Function to update the greeting in the main window
def update_greeting():
    greeting.config(text=f"Good Day, {name}!")

# Add a button to open the name entry window
open_name_entry()

# Placeholder for greeting label
greeting = tk.Label(app, text="Good Day!", font=("Arial", 14))
greeting.pack()

wdywd = tk.Label(app, text="What do you want to do?", font=("Arial", 10))
wdywd.pack()

def playaudio(inputfile):
    pygame.mixer.init()
    pygame.mixer.music.load(inputfile)

    def startmusic():
        pygame.mixer.music.play()

    def stopmusic():
        pygame.mixer.music.stop()

    def rewindmusic():
        rewinderapp = tk.Toplevel(fileplayer)
        rewinderapp.title("Rewind Sound")
        rewinderapp.geometry("250x150")
        rewinderapp.resizable(False, False)

        msg.showinfo("TIP", "Enter a number in seconds to rewind/fast-forward. Negative numbers rewind.")

        titleofrewinder = tk.Label(rewinderapp, text="Rewind Sound", font=("Arial", 14))
        titleofrewinder.pack()

        num = tk.Entry(rewinderapp, font=("Arial", 10), width=10)
        num.pack()

        def rewindsubmit():
            try:
                offset = int(num.get())  # Get user input
                current_time = pygame.mixer.music.get_pos() // 1000  # Get current time in seconds
                new_time = max(0, current_time + offset)  # Ensure time doesn't go negative
                pygame.mixer.music.play(start=new_time)
                rewinderapp.destroy()
            except ValueError:
                msg.showerror("Error", "Please enter a valid number.")

        submitrewind = tk.Button(rewinderapp, text="Submit", font=("Arial", 10), bg="green", command=rewindsubmit)
        submitrewind.pack()

    # Create audio player window
    fileplayer = tk.Toplevel(app)
    fileplayer.title(f"{inputfile} - VDC Audio Player")
    fileplayer.geometry("300x150")
    fileplayer.resizable(False, False)

    play = tk.Button(fileplayer, text="Play", font=("Arial", 10), bg="green", fg="white", width=10, command=startmusic)
    play.pack(pady=5)

    stop = tk.Button(fileplayer, text="Stop", font=("Arial", 10), bg="red", fg="white", width=10, command=stopmusic)
    stop.pack(pady=5)

    rewind = tk.Button(fileplayer, text="Rewind", font=("Arial", 10), bg="blue", fg="white", width=10, command=rewindmusic)
    rewind.pack(pady=5)

def openfromfilefunc():
    file = fd.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])  # Ask for an MP3 file
    if file:  # Ensure a file is selected
        playaudio(file)

openfromfile = tk.Button(app, text="Open From File", font=("Arial", 10), bg="Yellow", fg="black", command=openfromfilefunc)
openfromfile.pack(pady=10)
copyright = tk.Label(app, text="2025 AtticDev Productions")
copyright.pack()
# Run the main application loop
app.mainloop()
