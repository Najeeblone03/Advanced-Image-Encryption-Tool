 Overview
 
The Advanced Image Encryption Tool is a Python-based application that encrypts and decrypts images using a combination of SHA-256 password hashing, pixel shuffling, and XOR encryption. This project demonstrates basic image security concepts and file protection techniques.
 Features
 
Password-based image encryption
Secure key generation using SHA-256
Random pixel shuffling for added security
XOR-based image encryption and decryption
Restore original image with the correct password
Simple command-line interface
🛠️ Technologies Used
Python
Pillow (PIL)
NumPy
Hashlib

Installation
Clone the repository:
git clone https://github.com/your-username/image-encryption-tool.git
cd image-encryption-tool
Install dependencies:
pip install pillow numpy

Usage
Run the program:
python image_encryption.py

Menu:
===== ADVANCED IMAGE ENCRYPTION =====
1. Encrypt
2. Decrypt
3. Exit
Encrypt an Image
Select option 1.
Enter the image path.
Enter a password.
The encrypted image will be saved as encrypted.png.
Decrypt an Image
Select option 2.
Enter the encrypted image path.
Enter the same password used during encryption.
The decrypted image will be saved as decrypted.png.

Output Files

File Name	Description
encrypted.png	Encrypted image
decrypted.png	Decrypted image
shuffle_key.npy	Stores pixel shuffle indices

Encryption Process

Generate a secure key from the user password using SHA-256.
Convert the image into a NumPy array.
Shuffle pixel positions randomly.
Apply XOR encryption using the generated key.
Save the encrypted image and shuffle pattern.

Decryption Process

Load the encrypted image.
Generate the same key from the password.
Reverse the XOR operation.
Restore original pixel positions using the stored shuffle indices.
Save the recovered image.

 Example
 
Choice: 1
Image Path: photo.jpg
Password: mypassword

Image Encrypted Successfully!
Choice: 2
Encrypted Image Path: encrypted.png
Password: mypassword

Image Decrypted Successfully!

Learning Outcomes

Image processing with Pillow
Array manipulation using NumPy
Cryptographic hashing with SHA-256
XOR encryption techniques
File handling in Python

📜 License
