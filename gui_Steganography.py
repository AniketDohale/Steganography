import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os


def encrypt_Image(image_Path, secret_Message, password, output_Path):
    img = cv2.imread(image_Path)

    if img is None:
        messagebox.showerror("Error", "Image Not Found!")
        return False

    d = {}

    for i in range(256):
        d[chr(i)] = i

    m, n, z = 0, 0, 0
    message = password + secret_Message
    message_Length = f"{len(message):08d}"
    full_Message = message_Length + message

    for i in range(len(full_Message)):
        img[n, m, z] = d[full_Message[i]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    cv2.imwrite(output_Path, img)
    messagebox.showinfo("Success", f"Message Encrypted and Saved as {output_Path}")

    message_Entry.delete(0, tk.END)
    encrypt_Password_Entry.delete(0, tk.END)



def decrypt_Image(image_Path, password):
    img = cv2.imread(image_Path)

    if img is None:
        messagebox.showerror("Error", "Image Not Found!")
        return False

    c = {}

    for i in range(256):
        c[i] = chr(i)

    m, n, z = 0, 0, 0

    length_Str = ""
    for i in range(8):
        length_Str += c[img[n, m, z]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    try:
        message_Length = int(length_Str)
    except ValueError:
        messagebox.showerror("Error", "Decryption Failed: Invalid Length Header")
        return False

    message = ""
    for i in range(message_Length):
        message += c[img[n, m, z]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    embedded_Password = message[:len(password)]
    if embedded_Password != password:
        messagebox.showerror("Error", "Authentication Failed: Incorrect Password.")
        return False

    decrypted_Message = message[len(password):]
    messagebox.showinfo("Decrypted Message", decrypted_Message)

    decrypt_password_Entry.delete(0, tk.END)


def select_image():
    global image_Path
    file_Path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_Path:
        image_Path = file_Path
        img = Image.open(image_Path)
        img = img.resize((450, 400), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        image_Label.config(image=img)
        image_Label.image = img

        image_Name = os.path.basename(image_Path)
        image_Name_Label.config(text=f"{image_Name}")


def start_Encryption():
    secret_Message = message_Entry.get()
    password = encrypt_Password_Entry.get()
    output_Path = os.path.join(os.getcwd(), "encrypted_Image.png")

    if not image_Path:
        messagebox.showerror("Error", "Please select an image!")
        return

    if not secret_Message or not password:
        messagebox.showerror("Error", "Message and Password cannot be empty!")
        return

    encrypt_Image(image_Path, secret_Message, password, output_Path)


def start_Decryption():
    password = decrypt_password_Entry.get()

    if not image_Path:
        messagebox.showerror("Error", "Please Select an Image!")
        return

    if not password:
        messagebox.showerror("Error", "Password cannot be Empty!")
        return

    decrypt_Image(image_Path, password)


root = tk.Tk()
root.title("Steganography")
root.geometry("867x620")

root.resizable(False, False)

image_Path = ""

tk.Label(
    root, 
    bd=2, 
    relief=tk.GROOVE, 
    text="Steganography Tool", 
    font=("Arial", 16)
).pack(padx=20, pady=10, ipadx=10, ipady=10)

# Main Container Frames
left_Frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
left_Frame.pack(side=tk.LEFT, padx=(20, 10), pady=20, ipadx=10, ipady=10)

right_Frame = tk.Frame(root)
right_Frame.pack(side=tk.RIGHT, padx=(10, 20), pady=20)

# Left Frame - Image Input
image_Label = tk.Label(left_Frame)
image_Label.pack(pady=10)

image_Name_Label = tk.Label(left_Frame, text="", font=("Arial", 12))
image_Name_Label.pack(pady=5)

tk.Button(left_Frame, text="Select Image", command=select_image).pack(pady=5)

# Right Frame - Encryption Section
encryption_Frame = tk.Frame(right_Frame, bd=2, relief=tk.GROOVE)
encryption_Frame.pack(pady=10, ipadx=10, ipady=10)

tk.Label(encryption_Frame, text="Enter Secret Message:").pack(pady=5)
message_Entry = tk.Entry(encryption_Frame, width=50)
message_Entry.pack(pady=5)

tk.Label(encryption_Frame, text="Enter Password (Encryption):").pack(pady=5)
encrypt_Password_Entry = tk.Entry(encryption_Frame, width=50, show="*")
encrypt_Password_Entry.pack(pady=5)

tk.Button(encryption_Frame, text="Encrypt Image", command=start_Encryption).pack(pady=10)

# Right Frame - Decryption Section (Below Encryption)
decryption_Frame = tk.Frame(right_Frame, bd=2, relief=tk.GROOVE)
decryption_Frame.pack(pady=10, ipadx=10, ipady=10)

tk.Label(decryption_Frame, text="Enter Password (Decryption):").pack(pady=5)
decrypt_password_Entry = tk.Entry(decryption_Frame, width=50, show="*")
decrypt_password_Entry.pack(pady=5)
tk.Button(decryption_Frame, text="Decrypt Image", command=start_Decryption).pack(pady=10)

root.mainloop()
