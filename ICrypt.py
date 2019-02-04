from os import listdir
from os.path import isfile, join
import random
import os
import pyAesCrypt


#here is the path of files to be encrypted make sure to add / at the end 
my_path = 'test_here/'

#generating password

characters = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
password = ''

for i in range(80):
     password += random.choice(characters)
save = input('The password to decrypt is\t'+password+'\nCOPY THIS PASSWORD YOU WILL NEED IT TO DECRYPT THE FILES(hit any key to continue)')

#encrypting files

only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]

for files in only_files:
    print('\nGOING TO ENCRYPT '+my_path+files)
    encrypted_file = 'locked.'+files
    print('ENCRYPTING...')
    pyAesCrypt.encryptFile(my_path+files, my_path+encrypted_file, password, bufferSize=64*1024)
    
#overwriting files

    print('OVERWRITING...')
    char = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!~@#$%^&*()_+=-{[}]":;?/>.<,|'
    only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
    file_size = os.path.getsize(my_path+files)
    new = ''
    for i in range(file_size):
        new += random.choice(char)
    os.remove(my_path+files)
    ran = open(my_path+files, 'w')
    ran.write(new)
    ran.close()
    print('[-]DONE!')
