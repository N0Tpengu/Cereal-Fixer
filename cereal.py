import tkinter as tk
import webbrowser

def download_file():
    url = "https://store5.gofile.io/download/bfd672b5-e4aa-4781-8513-3fccd53d96a2/Cereal%20Fixer.exe"
    webbrowser.open(url)

# Create the main window
root = tk.Tk()
root.title("Download App")
root.geometry("400x300")
root.configure(bg='#23272A')  # Dark gray background color

# Function to change button color on hover
def on_enter(e):
    canvas.itemconfigure(button, fill='#7289DA')  # Change button color on hover

def on_leave(e):
    canvas.itemconfigure(button, fill='#2C2F33')  # Change button color on leave

# Create and place the canvas for the round button
canvas = tk.Canvas(root, width=150, height=150, bg='#23272A', highlightthickness=0)
canvas.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Draw a round button on the canvas
button = canvas.create_oval(10, 10, 140, 140, outline='#7289DA', width=4, fill='#2C2F33')
canvas.tag_bind(button, '<Button-1>', lambda event: download_file())  # Bind button click to download_file function
canvas.tag_bind(button, '<Enter>', on_enter)
canvas.tag_bind(button, '<Leave>', on_leave)

# Add text inside the round button with color #9969C7
canvas.create_text(75, 75, text="Click", fill='#9969C7', font=("Arial", 14, "bold"))

# Create a label for the message
message_label = tk.Label(root, text="Click the button below to download the file", fg='#7289DA', bg='#23272A', font=("Arial", 12))
message_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

root.mainloop()
