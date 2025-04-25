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
