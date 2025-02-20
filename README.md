# StegoProject
This project is for my IBM online intership.

**Program Description: Image Steganography with AES Encryption**  

This program implements an **image steganography** technique combined with **AES encryption** to securely hide messages within images. It allows users to encode a secret message into an image, ensuring that even if the image is intercepted, the message remains protected due to encryption.  

### **Key Features:**  
- **AES Encryption:** The secret message is first encrypted using the **Advanced Encryption Standard (AES)** to prevent unauthorized access.  
- **Image Encoding:** The encrypted message is embedded into an image by modifying pixel values.  
- **Secure Decoding:** Only users with the correct passcode can retrieve and decrypt the hidden message.  
- **User-Friendly Interface:** The program provides an interactive console-based experience for encoding and decoding messages.  

### **How It Works:**  
1. **Encoding:**  
   - The user provides an image, a secret message, and a passcode.  
   - The message is encrypted using AES encryption.  
   - The encrypted message is embedded into the image pixels.  
   - The modified image is saved as an output file.  

2. **Decoding:**  
   - The user provides the encoded image and the passcode.  
   - The program extracts the hidden message from the image.  
   - The extracted message is decrypted using AES.  
   - If the correct passcode is provided, the original secret message is revealed.  

### **Requirements:**  
- OpenCV (`pip install opencv-python`) for image processing.  
- NumPy (`pip install numpy`) for numerical operations.  
- PyCryptodome (`pip install pycryptodome`) for AES encryption.  

This program is ideal for users who require a **secure and covert method of communication** by embedding messages into images, making it suitable for privacy-focused applications, watermarking, and digital security.
