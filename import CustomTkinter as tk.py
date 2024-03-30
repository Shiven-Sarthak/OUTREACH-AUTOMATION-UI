import customtkinter as tk
from customtkinter import filedialog

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            # Here you can write content to the file if needed
            pass
        print("File saved successfully at:", file_path)

# Create the main window
root = tk.CTk()
root.title("Save File Example")

# Create a button to trigger file save
save_button = tk.CTkButton(root, text="Save File", command=save_file)
save_button.pack(pady=20)

# Run the main event loop
root.mainloop()
