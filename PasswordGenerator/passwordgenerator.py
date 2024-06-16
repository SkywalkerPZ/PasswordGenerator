import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    if not characters:
        raise ValueError("At least one character set must be selected")
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def calculate_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    # Simple heuristic for password strength
    strength = 0
    if length >= 8:
        strength += 1
    if length >= 12:
        strength += 1
    if has_upper and has_lower:
        strength += 1
    if has_digits:
        strength += 1
    if has_special:
        strength += 1
    
    if strength == 5:
        return "Very Strong"
    elif strength >= 3:
        return "Strong"
    elif strength >= 2:
        return "Medium"
    else:
        return "Weak"

def on_generate_button_click():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be positive")
        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        result_label.config(text=f"Generated password: {password}")
        strength = calculate_password_strength(password)
        strength_label.config(text=f"Password Strength: {strength}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

def on_store_button_click():
    password = result_label.cget("text").replace("Generated password: ", "")
    if password:
        stored_passwords.append(password)
        messagebox.showinfo("Password Stored", "Password has been stored successfully!")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

def on_show_stored_passwords():
    if stored_passwords:
        stored_window = tk.Toplevel(root)
        stored_window.title("Stored Passwords")
        stored_listbox = tk.Listbox(stored_window, width=50, height=10)
        stored_listbox.pack(padx=10, pady=10)
        for pwd in stored_passwords:
            stored_listbox.insert(tk.END, pwd)
    else:
        messagebox.showinfo("No Stored Passwords", "There are no stored passwords.")

def on_copy_button_click():
    password = result_label.cget("text").replace("Generated password: ", "")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied to Clipboard", "Password has been copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

def on_save_to_file_click():
    if stored_passwords:
        with open("stored_passwords.txt", "w") as file:
            for pwd in stored_passwords:
                file.write(f"{pwd}\n")
        messagebox.showinfo("Saved to File", "Stored passwords have been saved to stored_passwords.txt")
    else:
        messagebox.showwarning("No Stored Passwords", "There are no stored passwords to save.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Set initial size of the window
root.geometry("900x500")

# Make the window resizable
root.resizable(True, True)

# Create and place the smaller communist symbol as a label
symbol_label = tk.Label(root, text="🗝", font=("Helvetica", 32))
symbol_label.pack()

# Create and place the entry for password length
length_label = tk.Label(root, text="Enter the desired password length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

# Character set options
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

upper_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var)
upper_check.pack()
lower_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var)
lower_check.pack()
digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack()
special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.pack()

# Create and place the generate button
generate_button = tk.Button(root, text="Generate Password", command=on_generate_button_click)
generate_button.pack()

# Create and place the store password button
store_button = tk.Button(root, text="Store Password", command=on_store_button_click)
store_button.pack()

# Create and place the show stored passwords button
show_stored_button = tk.Button(root, text="Show Stored Passwords", command=on_show_stored_passwords)
show_stored_button.pack()

# Create and place the copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=on_copy_button_click)
copy_button.pack()

# Create and place the save to file button
save_button = tk.Button(root, text="Save to File", command=on_save_to_file_click)
save_button.pack()

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.pack()

# Create and place the password strength label
strength_label = tk.Label(root, text="Password Strength: ")
strength_label.pack()

# Add footer with creator's name
footer_label = tk.Label(root, text="Made by SkywalkerPZ", font=("Helvetica", 10))
footer_label.pack(pady=10)

# Initialize the list to store passwords
stored_passwords = []

# Run the application
root.mainloop()
