import tkinter as tk

def encrypt_rail_fence(string):
    result = []
    tt = len(string)

    if tt % 2 == 0:
        for i in string:
            if string.index(i) % 2 == 0:
                result.append(i)

        for i in string:
            if string.index(i) % 2 != 0:
                result.append(i)
    else:
        for i in string:
            if string.index(i) % 2 == 0:
                result.append(i)

        for i in string:
            if string.index(i) % 2 != 0:
                result.append(i)

    return ''.join(result)

def on_encrypt_button_click():
    input_text = entry.get()
    encrypted_text = encrypt_rail_fence(input_text)
    result_label.config(text=f"Encrypted Text: {encrypted_text}")

# Create the main window
window = tk.Tk()
window.title("Rail Fence Cipher Encryption")

# Color Theme
bg_color = "Blue"  # Dark Gray
fg_color = "#FFFFFF"  # White
entry_bg_color = "#505050"  # Darker Gray
button_bg_color = "#007ACC"  # Blue

window.config(bg=bg_color)

# Create and place widgets
label = tk.Label(window, text="Enter the string:", bg=bg_color, fg=fg_color)
label.pack(pady=10)

entry = tk.Entry(window, bg=entry_bg_color, fg=fg_color)
entry.pack(pady=10)

encrypt_button = tk.Button(window, text="Encrypt", command=on_encrypt_button_click, bg=button_bg_color, fg=fg_color)
encrypt_button.pack(pady=10)

result_label = tk.Label(window, text="", bg=bg_color, fg=fg_color)
result_label.pack(pady=10)

# Start the GUI main loop
window.mainloop()
