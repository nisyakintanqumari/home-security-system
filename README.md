# Home Security System with Raspberry Pi and Cloud Camera Alert
🏠 Home Security System with Visual PIN Verification
This project is a smart home security solution developed using Raspberry Pi. It utilizes a keypad for PIN-based door access control and a camera for visual verification. When a wrong PIN is entered, the system captures an image and sends it to the user via a cloud service (e.g., email or cloud drive). If the PIN is correct, the door unlocks.
Smart Home Security System using Raspberry Pi and Python | Real-time intruder alert and cloud-based image capture system. A smart security system built using Raspberry Pi and Python. The system uses a pin code entry. If the wrong pin is entered, it will take a photo of the person and notify the user. If the correct pin is entered, the door will unlock.

## Technologies Used
- Python
- Raspberry Pi
- Camera Module

## 🔐 Features
- PIN-based keypad entry system
- Camera capture on incorrect PIN attempt
- Cloud/email-based photo alert
- Door control via solenoid lock
- Visual logging for unauthorized access

## 🧰 Components Used
- Raspberry Pi (Model 3 or 4)
- 4x4 Matrix Keypad
- Pi Camera
- Solenoid Lock
- Relay Module
- Power Adapter (12V for solenoid)
- Jumper Wires

## 💻 Technologies
- Python 3
- picamera
- smtplib (email sending)
- RPi.GPIO

## 📦 Repository Contents
```
home-security-system/
├── main.py
├── keypad.py
├── camera.py
├── email_sender.py
├── vigenere.py
├── requirements.txt
└── README.md
```

## 🚀 Getting Started
1. Wire all components based on Raspberry Pi GPIO pins.
2. Install dependencies: `pip3 install -r requirements.txt`
3. Update your email credentials in `email_sender.py`
4. Run the program: `python3 main.py`

## 👩‍💻 Author
**Nisya Kintan Qumari**  
Email: nisyakintanqumari@gmail.com  
LinkedIn: [Nisya Qumari](https://www.linkedin.com/in/nisya-kintan-qumari-%E5%80%AA%E8%89%BE%E8%8E%8E-52b202215/)
```

---

## 🧠 main.py
```python
from keypad import get_pin_input
from vigenere import decrypt
from email_sender import send_email
from camera import capture_photo
import RPi.GPIO as GPIO
import time

# Configurations
CORRECT_PIN = "1234"
ENCRYPTED = "7/261"  # Simulated encrypted value
KEY = "1234"
RELAY_PIN = 17

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.LOW)

def open_door():
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    print("✅ Access Granted. Door is unlocked.")
    time.sleep(10)
    GPIO.output(RELAY_PIN, GPIO.LOW)
    print("🔒 Door locked.")

try:
    while True:
        pin = get_pin_input()
        if pin == decrypt(ENCRYPTED, KEY):
            open_door()
        else:
            print("❌ Access Denied. Wrong PIN!")
            filename = "intruder.jpg"
            capture_photo(filename)
            send_email(filename)
except KeyboardInterrupt:
    GPIO.cleanup()
```

---

## 🔢 keypad.py
```python
def get_pin_input():
    return input("Enter PIN: ")
```

---

## 🔐 vigenere.py
```python
def decrypt(ciphertext, key):
    decrypted = ""
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i])
        k = ord(key[i % len(key)])
        decrypted += chr((c + int(key[i % len(key)])) % 127)
    return decrypted.lower()
```

---

## 📷 camera.py
```python
from picamera import PiCamera
from time import sleep

def capture_photo(filename):
    cam = PiCamera()
    cam.start_preview()
    sleep(2)
    cam.capture(filename)
    cam.stop_preview()
    cam.close()
```

---

## 📧 email_sender.py
```python
import smtplib
from email.message import EmailMessage

def send_email(image_path):
    msg = EmailMessage()
    msg['Subject'] = '🚨 Security Alert: Wrong PIN Detected'
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = 'destination_email@gmail.com'

    with open(image_path, 'rb') as img:
        msg.add_attachment(img.read(), maintype='image', subtype='jpeg', filename=image_path)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('your_email@gmail.com', 'your_password')
        smtp.send_message(msg)
```

---

## 📎 requirements.txt
```
picamera
RPi.GPIO
```

Let me know if you want this packaged into a downloadable `.zip` or help creating the GitHub repo with this structure! 🚀
