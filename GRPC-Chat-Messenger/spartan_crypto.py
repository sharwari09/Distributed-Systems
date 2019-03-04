from Crypto.Cipher import AES

IV = 'SpartanMessenger'


def encrypt_message(key, message):
    padded_msg = message.ljust((int(len(message)/16) + 1) * 16)
    encryption_suite = AES.new(key.ljust(16), AES.MODE_CBC, IV)
    return encryption_suite.encrypt(padded_msg)


def decrypt_message(key, encrypted_message):
    decryption_suite = AES.new(key.ljust(16), AES.MODE_CBC, IV)
    return decryption_suite.decrypt(encrypted_message).strip(b' ')
