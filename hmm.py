import customtkinter as ctk
passcode="1234"



def get_entry_data():
    entry_data=entry.get()
    if entry_data==passcode:
        my_tab.pack(expand=True, fill="both")
    else:
        error_label.configure(text="Incorrect passcode. Please try again.")


def collect_scrape_lead_data():
    niche = entry2.get()
    num_leads = entry3.get()
    
    # Check if the data is appropriate
    if niche and num_leads.isdigit():
        # Perform further actions with the collected data
        pass
    else:
        # Handle inappropriate data
        error_label.configure(text="Please enter appropriate data for Niche and No. of Leads.")

def collect_outreach_data():
    num_repetitions = entry5.get()
    
    # Check if the data is appropriate
    if num_repetitions.isdigit():
        # Perform further actions with the collected data
        pass
    else:
        # Handle inappropriate data
        error_label.configure(text="Please enter appropriate data for Number of Repetitions.")

def collect_scrape_and_outreach_data():
    niche = entry7.get()
    num_leads = entry8.get()
    num_outreach = entry9.get()
    
    # Check if the data is appropriate
    if niche and num_leads.isdigit() and num_outreach.isdigit():
        # Perform further actions with the collected data
        pass
    else:
        # Handle inappropriate data
        error_label.configure(text="Please enter appropriate data for Niche, No. of Leads, and Number of Outreach.")



leads_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# Set appearance mode and default color theme
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Create the root window
root = ctk.CTk()
root.title("Outreach Automation")
root.geometry("700x400")
root.resizable(False, False)  # Disable resizing

#Create Frame
frame=ctk.CTkFrame(master=root)
frame.pack(fill="both",expand=True,pady=3)

error_label = ctk.CTkLabel(master=frame, text="", font=("Montserrat", 12),padx=10,pady=10)
error_label.place(relx=0.5, rely=0.75, anchor="center")


# Create the label
my_label = ctk.CTkLabel(master=frame, text="Login Page", font=("Montserrat", 28))
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

#TAB 1
tab_1=my_tab.add("Scrape Lead")
l1=ctk.CTkLabel(master=tab_1,text="Niche",font=("Montserrat", 18))
l1.place(relx=0.25,rely=0.2)

entry2 = ctk.CTkEntry(master=tab_1, font=("Montserrat", 18))
entry2.place(relx=0.47, rely=0.2)

l2=ctk.CTkLabel(master=tab_1,text="No. of Leads",font=("Montserrat", 18))
l2.place(relx=0.25,rely=0.35)

entry3 = ctk.CTkEntry(master=tab_1, font=("Montserrat", 18))
entry3.place(relx=0.47, rely=0.35)

save_file_1=ctk.CTkButton(master=tab_1,text="Save the File",font=("Montserrat", 18))
save_file_1.place(relx=0.25,rely=0.5)

entry4= ctk.CTkEntry(master=tab_1, font=("Montserrat", 18),state='disabled')
entry4.place(relx=0.47, rely=0.5)

start_tab1=ctk.CTkButton(master=tab_1,font=("Montserrat", 18),text="START➡️",command=collect_scrape_lead_data)
start_tab1.place(relx=0.36,rely=0.7)

#TAB 2
tab_2=my_tab.add("Outreach")
l3=ctk.CTkLabel(master=tab_2,text="Number of repetition",font=("Montserrat", 18))
l3.place(relx=0.25,rely=0.2)

entry5= ctk.CTkEntry(master=tab_2, font=("Montserrat", 18))
entry5.place(relx=0.55, rely=0.2)

save_file_2=ctk.CTkButton(master=tab_2,text="Save the File",font=("Montserrat", 18))
save_file_2.place(relx=0.25,rely=0.35)

entry6= ctk.CTkEntry(master=tab_2, font=("Montserrat", 18),state='disabled')
entry6.place(relx=0.55, rely=0.35)

start_tab2=ctk.CTkButton(master=tab_2,font=("Montserrat", 18),text="START➡️")
start_tab2.place(relx=0.36,rely=0.55)

#TAB 3
tab_3=my_tab.add("Scrape and Outreach")

l4=ctk.CTkLabel(master=tab_3,text="Niche",font=("Montserrat", 18))
l4.place(relx=0.25,rely=0.2)

entry7 = ctk.CTkEntry(master=tab_3, font=("Montserrat", 18))
entry7.place(relx=0.55, rely=0.2)

l5=ctk.CTkLabel(master=tab_3,text="No. of Leads",font=("Montserrat", 18))
l5.place(relx=0.25,rely=0.35)

entry8 = ctk.CTkEntry(master=tab_3, font=("Montserrat", 18))
entry8.place(relx=0.55, rely=0.35)

l6=ctk.CTkLabel(master=tab_3,font=("Montserrat", 18),text="Number of Outreach")
l6.place(relx=0.25,rely=0.5)

entry9= ctk.CTkEntry(master=tab_3, font=("Montserrat", 18))
entry9.place(relx=0.55, rely=0.5)

save_file_3=ctk.CTkButton(master=tab_3,text="Save the File",font=("Montserrat", 18))
save_file_3.place(relx=0.25,rely=0.65)

entry_10=ctk.CTkEntry(master=tab_3, font=("Montserrat", 18),state='disabled')
entry_10.place(relx=0.55,rely=0.65)







root.mainloop()
