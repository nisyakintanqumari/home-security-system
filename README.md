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
