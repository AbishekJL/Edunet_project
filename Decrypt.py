import cv2
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def decrypt_image():
    file_path = filedialog.askopenfilename(title="Select Encrypted Image", filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if not file_path:
        return
    
    img = cv2.imread(file_path)
    pas = simpledialog.askstring("Input", "Enter passcode for Decryption")
    
    c = {i: chr(i) for i in range(255)}
    n = m = z = 0
    message = ""
    
    try:
        for _ in range(img.shape[0] * img.shape[1] // 3):
            message += c[img[n, m, z]]
            n = (n + 1) % img.shape[0]
            m = (m + 1) % img.shape[1]
            z = (z + 1) % 3
    except KeyError:
        messagebox.showerror("Error", "Decryption failed! Invalid passcode or image.")
        return
    
    messagebox.showinfo("Decryption", f"Decrypted Message: {message}")

if __name__ == "__main__":
    decrypt_image()
