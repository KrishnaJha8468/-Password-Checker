import re  # For checking password patterns
import bcrypt  # For secure password hashing
import tkinter as tk  # For GUI
from tkinter import messagebox  # For pop-up messages

def check_password_strength(password):
    """Checks the strength of a password based on security rules."""
    
    strength_score = 0  

    # Rule 1: Minimum 12 characters
    if len(password) >= 12:
        strength_score += 1
    else:
        return "❌ Password too short! Use at least 12 characters."

    # Rule 2: Uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength_score += 1
    else:
        return "❌ Include both UPPER and lower case letters."

    # Rule 3: At least one number
    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        return "❌ Add some numbers."

    # Rule 4: At least one special character
    if re.search(r'[@$!%*?&]', password):
        strength_score += 1
    else:
        return "❌ Use special characters (@, $, %, etc.)."

    # Final strength evaluation
    if strength_score == 4:
        return "✅ Strong Password! 🔥"
    elif strength_score == 3:
        return "⚠️ Medium Strength Password."
    else:
        return "🚨 Weak Password! Improve security."

def hash_password(password):
    """Hashes the password using bcrypt for security."""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed

def check_password():
    """Checks password strength and displays results in a pop-up."""
    password = entry.get()  # Get user input from the text box
    result = check_password_strength(password)  
    hashed_pw = hash_password(password)  # Hash the password
    messagebox.showinfo("Password Strength", result + f"\n🔐 Hashed Password:\n{hashed_pw}")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")

# UI Elements
tk.Label(root, text="Enter Password:").pack()
entry = tk.Entry(root, show="*", width=30)
entry.pack()

tk.Button(root, text="Check Strength", command=check_password).pack()

# Run the GUI
root.mainloop()
