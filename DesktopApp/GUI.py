import tkinter as tk
from main import main

def proceed(name,limit,platform):
    main(name,limit,platform)


window = tk.Tk()
window.title("Remind Me to take a break")
window.geometry("400x400")
label = tk.Label(
    text="Remind Me to take a break",
    foreground="black",  # Set the text color to white
    # background="black"  # Set the background color to black,
    font=("Helvetica", 16)  # Set the font to Helvetica, size 16
)
label2 = tk.Label(
    text="Time limit:",
    foreground="black",  # Set the text color to white
    # background="black"  # Set the background color to black,
    font=("Helvetica", 12)  # Set the font to Helvetica, size 16
)

entry = tk.Entry(fg="black", bg="orange", width=30, font=("Helvetica", 14), borderwidth=1)
label3 = tk.Label(
    text="What to watch:",
    foreground="black",  # Set the text color to white
    # background="black"  # Set the background color to black,
    font=("Helvetica", 12)  # Set the font to Helvetica, size 16
)
entry2 = tk.Entry(fg="black", bg="orange", width=30, font=("Helvetica", 14), borderwidth=1)


btn1 = tk.Button(
    text="Netflix",
    fg="black",  # Set the text color to white
    bg="orange",  # Set the background color to black,
    font=("Helvetica", 12),  # Set the font to Helvetica, size 16
    command=lambda: proceed(entry2.get(), entry.get(), "netflix")
)
btn2 = tk.Button(
    text="Youtube",
    fg="black",  # Set the text color to white
    bg="orange",  # Set the background color to black,
    font=("Helvetica", 12),  # Set the font to Helvetica, size 16
    command=lambda: proceed(entry2.get(), entry.get(), "youtube")
)


label.pack()
label2.pack()
entry.pack()
label3.pack()
entry2.pack()
btn1.pack(padx=10, pady=10)
btn2.pack(padx=10, pady=10)

window.mainloop()
# web = WebAccess()

