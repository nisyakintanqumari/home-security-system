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
