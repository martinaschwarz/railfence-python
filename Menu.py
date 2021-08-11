from Cipher import encrypt
from Cipher import decrypt
from Cipher import showCipher

# Initiate variables for user input (+ cipherText)
plainText = ''
key = ''
offset = ''
cipherText = ''


# Function to start the interactive menu and keep it alive until manually quit by the user
def go():
    keepRunning = True
    printMenu()
    
    # Check which menu option is selected by the user through input
    # Call a certain function depending on the chosen option
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
            # Quit the application
            keepRunning = False
        else:
            print('[ERROR] Invalid Selection!')


# Function to present the user with some choices
def printMenu():
    print('1. Enter Message')
    print('2. Enter Key and Offset')
    print('3. Encrypt')
    print('4. Decrypt')
    print('5. Display Rail Fence')
    print('6. Quit')
    print('')


# Ask the user to input the message to be encrypted
def enterText():
    global plainText; plainText = raw_input('Enter Message >')
    print('')


# Ask the user to input an encryption key ( = the number of rows) and offset ( = the starting row)        
def enterKey():
    global key; key = int(raw_input('Enter Rail Fence Key >'))
    global offset; offset = int(raw_input('Enter Offset >'))
    print('')


# Call the encryption function and pass in all user input
def encryption():
    # Check and alert the user if no message was passed in
    if plainText == '':
        print('')
        print('[ALERT] Please enter a message for encryption!')
        print('')
    # Check and alert the user if no key or offset were passed in
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


# Call the decryption function and pass in the encrypted message + key and offset
def decryption():
    # Check and alert the user if no message was encrypted
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


# Call the railFence function to display the encryption pattern used
def railFence():
    # Check and alert the user if no message was encrypted
    if cipherText == '':
        print('')
        print('[ERROR] No message has been encrypted!')
        print('')
    else:
        print('')
        print('Rail Fence Cipher:')
        showCipher()
        print('')
    
