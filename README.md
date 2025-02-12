# Cyber-Security
This is final Project of IBM edunet cybersecurity internship

## Project Title: SECURE DATA HIDING IMAGES USING STEGANOGRAPHY


---

### Overview

This project is a part of the IBM Edunet Foundation Cybersecurity internship, which lasted for six Weeks. Throughout this internship, I gained practical knowledge about various cybersecurity tools and techniques, including VeraCrypt and setting up Kali Linux. The main focus of this project is to develop a steganography system to securely hide text messages within digital images.

---

### Repository Name: Edunet_project

---

### Files in the Repository:

- `encryption.py`: Script for encoding secret messages into images.
- `decryption.py`: Script for decoding hidden messages from images.
- `Abishek_J_L.pptx`: PowerPoint presentation detailing the project.
- `encoded.jpg`: Sample encrypted image with a hidden message.

---

### Project Description

**SECURE DATA HIDING IMAGES USING STEGANOGRAPHY:**

This project involves creating a steganographic system to embed confidential text messages into digital images using advanced encryption techniques. The project ensures that the hidden data remains imperceptible to unauthorized users while maintaining the image quality.

---

### Project Components

1. **Encryption Script (`encryption.py`):**
   - Reads an input image.
   - Prompts the user for a secret message and password.
   - Uses SHA-256 hashing for password security.
   - Embeds the secret message into the image pixels.
   - Saves the encrypted image.

2. **Decryption Script (`decryption.py`):**
   - Reads the encrypted image.
   - Prompts the user for the password.
   - Uses SHA-256 hashing to validate the password.
   - Extracts and decodes the hidden message from the image.
   - Displays the decoded message.

---

### How to Use

1. **Encryption:**
   - Ensure `encryption.py` is in the same directory as your input image.
   - Run the script and follow the prompts to input your secret message and password.
   - The script will generate an `encryptedImage.jpg` file with the hidden message.

2. **Decryption:**
   - Ensure `decryption.py` is in the same directory as your encrypted image.
   - Run the script and follow the prompts to input your password.
   - The script will display the hidden message.

---

### Tools and Libraries

- Python
- OpenCV
- hashlib

---

### Cloning the Repository

To copy or clone this repository to your local machine, use the following commands:

```bash
# Clone the repository
git clone https://github.com/AbishekJL/Edunet_project.git

# Change directory to the cloned repository
cd Edunet_Project

