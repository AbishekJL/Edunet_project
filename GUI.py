import tkinter as tk
from encrypt import encrypt_image
from decrypt import decrypt_image

root = tk.Tk()
root.title("Image Steganography")
root.geometry("300x200")

tk.Button(root, text="Encrypt Image", command=encrypt_image).pack(pady=10)
tk.Button(root, text="Decrypt Image", command=decrypt_image).pack(pady=10)

tk.Label(root, text="Secure Image Steganography").pack(pady=10)

root.mainloop()
