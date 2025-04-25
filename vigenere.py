```python
def decrypt(ciphertext, key):
    decrypted = ""
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i])
        k = ord(key[i % len(key)])
        decrypted += chr((c + int(key[i % len(key)])) % 127)
    return decrypted.lower()
```
