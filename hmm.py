import customtkinter as ctk
passcode="1234"
def get_entry_data():
    entry_data=entry.get()
    if entry_data==passcode:
        print("HMMMMMM")
    else:
        print("EWWWWW BROTHER WHAT'S THAT")

# Set appearance mode and default color theme
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Create the root window
root = ctk.CTk()
root.title("Login")
root.geometry("700x400")
root.resizable(False, False)  # Disable resizing

# Create the label
my_label = ctk.CTkLabel(root, text="Welcome", font=("Montserrat", 28))
my_label.place(relx=0.5, rely=0.2, anchor="center")  # Position the label

# Create the entry widget
entry = ctk.CTkEntry(root, font=("Montserrat", 18))
entry.place(relx=0.5, rely=0.4, anchor="center")  # Position the entry widget

# Create the login button
b1 = ctk.CTkButton(root, text="Login", font=("Montserrat", 18), width=15,command=get_entry_data)
b1.place(relx=0.5, rely=0.6, anchor="center")  # Position the button

root.mainloop()
