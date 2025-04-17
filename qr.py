import qrcode
import os
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw

# Create folder
if not os.path.exists("output"):
    os.makedirs("output")

# Theme colors
BG_COLOR = "#E8F0F2"      # Background (pastel cream)
BTN_COLOR = "#3D405B"     # Button color (dark blue/gray)
BTN_TEXT = "#F4F1DE"      # Button text (light color)
FONT = ("Segoe UI", 11)

# QR code generation function
def generate_qr_gui():
    text = entry.get()
    if not text:
        messagebox.showwarning("Warning", "Please enter some text!")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_path = "output/qr_code.png"
    img.save(img_path)

    img_tk = ImageTk.PhotoImage(Image.open(img_path).resize((200, 200)))
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

    messagebox.showinfo("Success", "QR code generated and displayed!")

# Save function
def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                    filetypes=[("PNG files", "*.png")])
    if file_path:
        img = Image.open("output/qr_code.png")
        img.save(file_path)
        messagebox.showinfo("Saved", f"QR code saved:\n{file_path}")

# GUI initialization
root = Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Style components
def styled_button(master, text, command):
    return Button(master, text=text, command=command, font=FONT,
                  bg=BTN_COLOR, fg=BTN_TEXT, activebackground="#6D6875",
                  activeforeground="white", relief="flat", bd=0, padx=10, pady=5)

Label(root, text="Enter Text or URL:", font=FONT, bg=BG_COLOR).pack(pady=(20, 5))

entry = Entry(root, width=35, font=FONT, relief="solid", bd=1)
entry.pack(pady=5)

styled_button(root, "Generate QR Code", generate_qr_gui).pack(pady=15)

qr_label = Label(root, bg=BG_COLOR)
qr_label.pack(pady=10)

styled_button(root, "Save", save_qr).pack(pady=10)

# Optional exit button
# styled_button(root, "Exit", root.quit).pack(pady=10)

root.mainloop()
