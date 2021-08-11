# Call the Cipher function, pass in the plain text and the encryption key and offset
# Set the encryption state to True to ensure encryption
def encrypt(plainText, key, offset):
    return doCipher(plainText, key, offset, True)


# Call the Cipher function, pass in the encrypted text and the encryption key and offset
# Set the encryption state to False to ensure decryption
def decrypt(cipherText, key, offset):
    return doCipher(cipherText, key, offset, False)


# Main encryption function
def doCipher(s, key, offset, encrypt):
    
    # Initiate the encryption matrix, ie. the Rail Fence
    global matrix
    matrix = [[0 for i in range(len(s))]
                  for j in range(key)]
    
    # Initiate variable to control whether to move up or down a row
    moveDown = True
    
    # Initiate starting row and column, row is set to offset passed in by user
    row = offset
    col = 0
    
    # Loop through each char in the string passed in by the user
    # Place the char into the current index of the matrix
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
            
    c = 0
    res = []
            
    if encrypt == True:
        i = 0
        while i < key:
            j = 0
            while j < len(s):
                if matrix[i][j] != 0:
                    res.append(matrix[i][j])
                j += 1
            i += 1
    
        cipherText = ''
        for x in res:
            cipherText += x
        
        return cipherText
        
    else:
        i = 0
        while i < key:
            j = 0
            while j < len(s):
                if matrix[i][j] != 0:
                    matrix[i][j] = s[c]
                    c += 1
                j += 1
            i += 1
        
        i = 0
        while i < len(s):
            j = 0
            while j < key:
                if matrix[j][i] != 0:
                    res.append(matrix[j][i])
                j += 1
            i += 1
    
        decrypText = ''
        for x in res:
            decrypText += x
        
        return decrypText

    
def showCipher():
    for rows in matrix:
        temp = []
        railFence = ''
        
        for col in rows:
            if col == 0:
                temp.append(' ')
            else:
                temp.append(col)
        for x in temp:
            railFence += x
        
        print(railFence)
