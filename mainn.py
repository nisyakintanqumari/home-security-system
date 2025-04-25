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
