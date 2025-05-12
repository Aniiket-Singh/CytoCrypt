from PIL import Image
from src.image_dna_chaos.encryptor import encrypt
from src.image_dna_chaos.decryptor import decrypt

def main():
    key = 0.3
    img = Image.open("data/samples/lena.png")
    cipher = encrypt(img, key)
    cipher.save("data/samples/encrypted.png")
    recovered = decrypt(cipher, key)
    recovered.save("data/samples/decrypted.png")

if __name__ == '__main__':
    main()