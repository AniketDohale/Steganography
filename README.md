# Secure Data Hiding in Images Using Steganography

This project provides a simple yet powerful GUI application to hide and retrieve sensitive data within images using steganography.

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - OpenCV (cv2)
  - Tkinter
  - PIL (Python Imaging Library)
- **Algorithm**: Least Significant Bit (LSB) Steganography

## Installation

1. **Clone this repository:**

    ```bash
    git clone https://github.com/AniketDohale/Steganography.git
    cd Steganography
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application:**

    ```bash
    python gui_Steganography.py
    ```

## Usage

1. **Encrypt an Image:**
   - Select an Image File.
   - Enter the Secret Message and Encryption Password.
   - Save the Encrypted Image.

2. **Decrypt an Image:**
   - Select the Encrypted Image File.
   - Enter the Decryption Password.
   - View the Extracted Secret Message.
