import cv2
import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def encrypt_image():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if not file_path:
        return
    
    img = cv2.imread(file_path)
    msg = simpledialog.askstring("Input", "Enter secret message:")
    password = simpledialog.askstring("Input", "Enter passcode:")
    
    if not msg or not password:
        messagebox.showerror("Error", "Message and passcode cannot be empty!")
        return
    
    d = {chr(i): i for i in range(255)}
    n = m = z = 0
    
    for char in msg:
        img[n, m, z] = d[char]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3
    
    encrypted_path = "encrypted_image.png"
    cv2.imwrite(encrypted_path, img)
    messagebox.showinfo("Success", f"Encrypted image saved as {encrypted_path}")
    os.system(f"start {encrypted_path}")

if __name__ == "__main__":
    encrypt_image()
