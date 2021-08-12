from cipher import Cipher
 
class Menu:
   
    # Initialise variables for user input (+ cipherText)
    global plainText; plainText = ''
    global key; key = ''
    global offset; offset = ''
    global cipherText; cipherText = ''
    
    
    # Function to start the interactive menu and keep it alive until manually quit by the user
    def go(self):
        keepRunning = True
        self.printMenu()
        
        # Check which menu option is selected by the user through input
        # Call a certain function depending on the chosen option
        while keepRunning: 
            choice = raw_input('Select Option [1 - 6]')
                
            if choice == '1':
                self.enterText()
            elif choice == '2': 
                self.enterKey()
            elif choice == '3':
                self.encryption()
            elif choice == '4':
                self.decryption()
            elif choice == '5':
                self.railFence()
            elif choice == '6':
                print('Quitting...') 
                # Quit the application
                keepRunning = False
            else:
                print('[ERROR] Invalid Selection!')
    
    
    # Function to present the user with some choices
    def printMenu(self):
        print('1. Enter Message')
        print('2. Enter Key and Offset')
        print('3. Encrypt')
        print('4. Decrypt')
        print('5. Display Rail Fence')
        print('6. Quit')
        print('')
    
    
    # Ask the user to input the message to be encrypted
    def enterText(self):
        global plainText; plainText = raw_input('Enter Message >')
        print('')
    
    
    # Ask the user to input an encryption key ( = the number of rows) and offset ( = the starting row)        
    def enterKey(self):
        try:
            global key; key = int(raw_input('Enter Rail Fence Key >'))
            global offset; offset = int(raw_input('Enter Offset >'))
            print('')
            # Ensure offset isn't greater than encryption key
            if offset >= key-1:
                print('[ERROR] Max possible offset allowed for an encryption key of ' + str(key) + ' is ' + str(key-2) + '!')
                self.enterKey()
        except ValueError:
            print('[ERROR] Please enter numeric values for the encryption key and offset!')
            self.enterKey()
    
    
    # Call the encryption function and pass in all user input
    def encryption(self):
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
            global cipherText; cipherText = Cipher().encrypt(plainText, key, offset)
            print('')
            print('Encrypted Message:')
            print(cipherText)
            print('')
    
    
    # Call the decryption function and pass in the encrypted message + key and offset
    def decryption(self):
        # Check and alert the user if no message was encrypted
        if cipherText == '':
            print('')
            print('[ERROR] No message found for decryption!')
            print('')
        else:
            global decrypText; decrypText = Cipher().decrypt(cipherText, key, offset)
            print('')
            print('Decrypted Message:')
            print(decrypText)
            print('')
    
    
    # Call the railFence function to display the encryption pattern used
    def railFence(self):
        # Check and alert the user if no message was encrypted
        if cipherText == '':
            print('')
            print('[ERROR] No message has been encrypted!')
            print('')
        else:
            print('')
            print('Rail Fence cipher:')
            Cipher().showCipher()
            print('')
        
