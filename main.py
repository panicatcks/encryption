import pyAesCrypt
from art import tprint
import string
import random

def randompassword():
  chars = string.ascii_letters + string.digits + string.punctuation
  size = 250
  return ''.join(random.choice(chars) for x in range(size))




class Encryption():
    def choose(self):
        self.choose = input('E/D (Encrypt/Decrypt) ')
        if self.choose == 'E' or 'e':
            Encryption().encrypt()
        elif self.choose == 'D' or 'd':
            Encryption().decrypt()
        else:
            print('Wrong choose')
            Encryption().choose()
        Encryption().choose()
    def encrypt(self):
        try:
            self.password = randompassword()
            self.file = input('File name ')
            pyAesCrypt.encryptFile(f'{self.file}.txt', 'encrypted.txt.aes', self.password)
            with open('key.txt','w+', encoding='utf-8') as key:
                key.write(self.password)
        except ValueError:
            print('No such file or directory')
            Encryption().encrypt()
    def decrypt(self):
        try:
            with open ('key.txt','r', encoding='utf-8') as key:
                self.password = key.read()
            self.file = input('File name ')
            pyAesCrypt.decryptFile(f'{self.file}.txt.aes','decrypted.txt', self.password)
            pass
        except ValueError:
            print('No such file or directory')
            Encryption().decrypt()


def main():
    start = Encryption()
    start.choose()



if __name__ == '__main__':
    tprint('panicatcks')
    main()
