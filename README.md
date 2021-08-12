# railfence-python
Encryption Application, using a Rail Fence Cipher, in Python

* This application takes in a string of any length and returns it in encrypted form, by placing each character into a matrix in a zig-zag (ie. a rail fence) pattern, and putting it back together row by row. The matrix is defined by the length of the string passed in (-> number of columns) and the encryption key, which is also input by the user (-> number of rows). Additionally, an offset value can be passed in, which changes the starting row of the encryption.

* To start the application, run the class Runner.
* A menu will be initialised and options are presented to the user:
  - Option 1: Enter a message to be encrypted
  - Option 2: Set the encryption key and the offset value
  - Option 3: Encrypt the given message and display the encrypted string
  - Option 4: Decrypt the encrypted message and display the decrypted string
  - Option 5: Display the rail fence, ie. the string in its encryption matrix
  - Option 6: Quit the application
