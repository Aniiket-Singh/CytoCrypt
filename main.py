from PIL import Image
from src.image_dna_chaos.encryptor import encrypt
from src.image_dna_chaos.decryptor import decrypt

key = 0.123456

# Load image
image_path = "data/samples/lena.png"
image = Image.open(image_path)

# Encrypt
encrypted_image = encrypt(image, key)
encrypted_image.save("data/samples/encrypted.png")

# Decrypt
decrypted_image = decrypt(encrypted_image, key)
decrypted_image.save("data/samples/decrypted.png")
