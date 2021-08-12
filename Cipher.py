class Cipher:
    
    # Call the Cipher function, pass in the plain text and the encryption key and offset
    # Set the encryption state to True to ensure encryption
    def encrypt(self, plainText, key, offset):
        return self.doCipher(plainText, key, offset, True)
    
    
    # Call the Cipher function, pass in the encrypted text and the encryption key and offset
    # Set the encryption state to False to ensure decryption
    def decrypt(self, cipherText, key, offset):
        return self.doCipher(cipherText, key, offset, False)
    
    
    # Main encryption function
    def doCipher(self, s, key, offset, encrypt):
        # Initialise the encryption matrix, ie. the rail fence
        global matrix
        matrix = [[0 for i in range(len(s))]
                      for j in range(key)]
        
        # Initialise variable to control whether to move up or down a row
        moveDown = True
        
        # Initialise starting row and column, row is set to offset passed in by user
        row = offset
        col = 0
        
        # Loop through each char in the string passed in by the user
        # Place the char into the current index of the matrix
        # Builds the matrix by creating a rail fence pattern
        for let in s: 
            matrix[row][col] = let
            
            # Move one column to the right
            col += 1
            
            # Move one row up or down, depending on the moveDown variable
            if moveDown == True:
                row += 1
            else:
                row -= 1
        
            # Flip the direction of the row increment/decrement when reaching the top or bottom row
            if row == 0 or row == key - 1:
                moveDown = not(moveDown)
                
        # Initialise empty array for encrypted message
        res = []
        
        # If boolean passed in = True -> Encrypt
        if encrypt == True:
            # Loop though each row
            i = 0
            while i < key:
                # Loop through each column
                j = 0
                while j < len(s):
                    # Check whether there is a char at each index
                    # If so, append to array
                    if matrix[i][j] != 0:
                        res.append(matrix[i][j])
                    j += 1
                i += 1
            
            # Initialise empty string for encrypted message
            # Loop through char array and append each char to string
            cipherText = ''
            for x in res:
                cipherText += x
                
            # Return string = encrypted message
            return cipherText
        
        # If boolean passed in = False -> Decrypt
        else:
            # Initialise variable to track index of passed in message
            c = 0
            # Loop through each row
            i = 0
            while i < key:
                # Loop through each column
                j = 0
                while j < len(s):
                    # Check whether there is a char at each index
                    # If so, replace it with the char at the current index of the encrypted message
                    if matrix[i][j] != 0:
                        matrix[i][j] = s[c]
                        c += 1
                    j += 1
                i += 1
            
            # Loop through each column
            i = 0
            while i < len(s):
                # Loop through each row
                j = 0
                while j < key:
                    # Check whether there is a char at each index
                    # If so, append to array
                    if matrix[j][i] != 0:
                        res.append(matrix[j][i])
                    j += 1
                i += 1
                
            # Initialise empty string for decrypted message
            # Loop through char array and append each char to string
            decrypText = ''
            for x in res:
                decrypText += x
            
            # Return string = decrypted message
            return decrypText
    
    
    # Function to display the rail fence pattern created for the matrix
    def showCipher(self):
        
        # Loop through each row
        for rows in matrix:
            
            # Initialise an empty array and string for output
            temp = []
            railFence = ''
            
            # Loop though each column in each row
            for col in rows:
                # If there is nothing at the index, replace it with a space
                if col == 0:
                    temp.append(' ')
                # If there is a char at the index, append it to the char array 
                else:
                    temp.append(col)
            # Loop through the char array and append each char to the string
            for x in temp:
                railFence += x
            
            # Print the string, creating the rail fence pattern
            print(railFence)
