import customtkinter as ctk
import random
import string
# Initialize CustomTkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

def generate_password():
    length = int(slider.get())
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    output_entry.delete(0, ctk.END)
    output_entry.insert(0, password)
    # By default hide password after generation
    if hide_password.get():
        output_entry.configure(show="*")
    else:
        output_entry.configure(show="")

def slider_event(value):
    length_label.configure(text=f"Password Length: {int(float(value))}")

def toggle_password_visibility():
    if hide_password.get():
        output_entry.configure(show="")
        eye_button.configure(text="🙈")  # Eye closed emoji
        hide_password.set(False)
    else:
        output_entry.configure(show="*")
        eye_button.configure(text="👁")  # Eye open emoji
        hide_password.set(True)

def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(output_entry.get())

def toggle_theme():
    current = ctk.get_appearance_mode()
    if current == "Dark":
        ctk.set_appearance_mode("Light")
        theme_button.configure(text="🌙")
    else:
        ctk.set_appearance_mode("Dark")
        theme_button.configure(text="🔆")

app = ctk.CTk()
app.title("ValidVault")
app.geometry("600x600")
app.resizable(False,False)


label = ctk.CTkLabel(app, text="Generate a Strong Password", font=ctk.CTkFont(size=18, weight="bold"))
label.pack(pady=15)

slider = ctk.CTkSlider(app, from_=6, to=12, number_of_steps=26)
slider.set(12)
slider.pack(pady=10)

length_label = ctk.CTkLabel(app, text="Password Length: 12")
length_label.pack()
slider.configure(command=slider_event)

# Entry for password output
output_entry = ctk.CTkEntry(app, width=230, font=ctk.CTkFont(size=14),border_width=2, border_color="black")
output_entry.pack(pady=15)

# Variable to track if password is hidden or shown
hide_password = ctk.BooleanVar(value=True)
output_entry.configure(show="*")  # Hide password initially



eye_button = ctk.CTkButton(app, text="👁", width=50, command=toggle_password_visibility)
eye_button.pack(pady=10)
copy_button = ctk.CTkButton(app, text="Copy", width=80, command=copy_to_clipboard)
copy_button.pack(pady=10)

generate_btn = ctk.CTkButton(app, text="Generate Password", command=generate_password)
generate_btn.pack(pady=15)

theme_button = ctk.CTkButton(app, text="🌙", command=toggle_theme)
theme_button.pack()

app.mainloop()