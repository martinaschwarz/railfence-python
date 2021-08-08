from Cipher import encrypt
from Cipher import decrypt
from Cipher import showCipher

plainText = ''
key = ''
offset = ''
cipherText = ''

def go():
    keepRunning = True
    printMenu()
    
    while keepRunning:    
        choice = raw_input('Select Option [1 - 6]')
            
        if choice == '1':
            enterText()
        elif choice == '2':     
            enterKey()
        elif choice == '3':
            encryption()
        elif choice == '4':
            decryption()
        elif choice == '5':
            railFence()
        elif choice == '6':
            print('Quitting...')
            keepRunning = False
        else:
            print('[ERROR] Invalid Selection!')
            
def printMenu():
    print('1. Enter Message')
    print('2. Enter Key and Offset')
    print('3. Encrypt')
    print('4. Decrypt')
    print('5. Display Rail Fence')
    print('6. Quit')
    print('')
    
def enterText():
    global plainText; plainText = raw_input('Enter Message >')
    print('')
        
def enterKey():
    global key; key = int(raw_input('Enter Rail Fence Key >'))
    global offset; offset = int(raw_input('Enter Offset >'))
    print('')
    
def encryption():
    if plainText == '':
        print('')
        print('[ALERT] Please enter a message for encryption!')
        print('')
    elif key == '' or offset == '':
        print('')
        print('[ALERT] Please set an encryption key and offset!')
        print('')
    else:
        global cipherText; cipherText = encrypt(plainText, key, offset)
        print('')
        print('Encrypted Message:')
        print(cipherText)
        print('')
    
def decryption():
    if cipherText == '':
        print('')
        print('[ERROR] No message found for decryption!')
        print('')
    else:
        global decrypText; decrypText = decrypt(cipherText, key, offset)
        print('')
        print('Decrypted Message:')
        print(decrypText)
        print('')

def railFence():
    if cipherText == '':
        print('')
        print('[ERROR] No message has been encrypted!')
        print('')
    else:
        print('')
        print('Rail Fence Cipher:')
        showCipher()
        print('')

    