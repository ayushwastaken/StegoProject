import cv2
import numpy as np
import os
from Crypto.Cipher import AES
import base64
import hashlib

def pad(text):
    return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)

def unpad(text):
    return text[:-ord(text[-1])]

def encrypt_text(text, passcode):
    key = hashlib.sha256(passcode.encode()).digest()
    cipher = AES.new(key, AES.MODE_CBC, iv=key[:16])
    encrypted = cipher.encrypt(pad(text).encode())
    return base64.b64encode(encrypted).decode()

def decrypt_text(encrypted_text, passcode):
    key = hashlib.sha256(passcode.encode()).digest()
    cipher = AES.new(key, AES.MODE_CBC, iv=key[:16])
    decrypted = cipher.decrypt(base64.b64decode(encrypted_text)).decode()
    return unpad(decrypted)

def encode_message(image_path, message, passcode, output_image="encoded_image.png"):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    height, width, _ = img.shape
    encrypted_msg = encrypt_text(message, passcode)
    ascii_values = [ord(char) for char in encrypted_msg]
    
    if len(ascii_values) + 1 > height * width:
        print("Error: Message too long for image size.")
        return
    
    flat_img = img[:, :, 0].flatten()
    flat_img[:len(ascii_values)] = ascii_values  # Embed message
    flat_img[len(ascii_values)] = 255  # End marker
    img[:, :, 0] = flat_img.reshape((height, width))
    
    cv2.imwrite(output_image, img)
    print(f"Message encoded and saved as {output_image}")

def decode_message(image_path, passcode):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    flat_img = img[:, :, 0].flatten()
    
    extracted_values = []
    for val in flat_img:
        if val == 255:  # End marker
            break
        extracted_values.append(val)
    
    encrypted_msg = ''.join(chr(val) for val in extracted_values)
    try:
        decrypted_msg = decrypt_text(encrypted_msg, passcode)
        print("Decrypted Message:", decrypted_msg)
    except Exception as e:
        print("Decryption failed: Incorrect passcode or corrupted data.")

if __name__ == "__main__":
    choice = input("Do you want to (E)ncode or (D)ecode a message? ").strip().lower()
    if choice == 'e':
        image_path = input("Enter the image filename: ")
        message = input("Enter the secret message: ")
        passcode = input("Enter a passcode: ")
        encode_message(image_path, message, passcode)
    elif choice == 'd':
        image_path = input("Enter the encoded image filename: ")
        passcode = input("Enter the passcode for decryption: ")
        decode_message(image_path, passcode)
    else:
        print("Invalid choice. Please enter 'E' to encode or 'D' to decode.")
