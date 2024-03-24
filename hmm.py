import customtkinter as ctk
passcode="1234"
def get_entry_data():
    entry_data=entry.get()
    if entry_data==passcode:
        print("HMMMMMM")
        my_tab.pack(expand=True, fill="both")
        
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

frame=ctk.CTkFrame(master=root)
frame.pack(padx=60,pady=20,fill="both",expand=True)

# Create the label
my_label = ctk.CTkLabel(master=frame, text="Welcome", font=("Montserrat", 28))
my_label.place(relx=0.5, rely=0.2, anchor="center")  # Position the label

# Create the entry widget
entry = ctk.CTkEntry(master=frame, font=("Montserrat", 18),placeholder_text="Passcode")
entry.place(relx=0.5, rely=0.4, anchor="center")  # Position the entry widget

# Create the login button
b1 = ctk.CTkButton(master=frame, text="Login", font=("Montserrat", 18), width=15,command=get_entry_data)
b1.place(relx=0.5, rely=0.6, anchor="center")  # Position the button

#Create the Tab View
my_tab=ctk.CTkTabview(master=frame)

#Create Tabs
tab_1=my_tab.add("Scrape")
b2=ctk.CTkButton(master=tab_1,text="BUTTON 2")
b2.pack()
tab_2=my_tab.add("Outreach")
b3=ctk.CTkButton(master=tab_2,text="BUTTON 3")
b3.pack()
tab_3=my_tab.add("Scrape and Outreach")
b4=ctk.CTkButton(master=tab_3,text="BUTTON 4")
b4.pack()

root.mainloop()
