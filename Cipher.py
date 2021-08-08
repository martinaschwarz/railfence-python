def encrypt(plainText, key, offset):
    return doCipher(plainText, key, offset, True)

def decrypt(cipherText, key, offset):
    return doCipher(cipherText, key, offset, False)

def doCipher(s, key, offset, encrypt):
    global matrix
    matrix = [[0 for i in range(len(s))]
                  for j in range(key)]
    
    moveDown = True
    
    row = offset
    
    col = 0
    c = 0
    res = []
    
    for let in s:        
        matrix[row][col] = let
        col+=1
        
        if moveDown == True:
            row+=1
        else:
            row-=1
    
        if row == 0 or row == key-1:
            moveDown = not(moveDown)
            
    if encrypt == True:
        i = 0
        while i < key:
            j = 0
            while j < len(s):
                if matrix[i][j] != 0:
                    res.append(matrix[i][j])
                j+=1
            i+=1
    
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
                    c+=1
                j+=1
            i+=1
        
        i = 0
        while i < len(s):
            j = 0
            while j < key:
                if matrix[j][i] != 0:
                    res.append(matrix[j][i])
                j+=1
            i+=1
    
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
